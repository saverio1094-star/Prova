#!/usr/bin/env python3
"""Timing del parlato di un reel: quanto dura ogni clip, quanto dura il montato, quanti crediti costa.

Uso:
    python3 timing.py copione.txt --voce lipsync --obiettivo 50-55
    python3 timing.py copione.txt --voce voiceover
    python3 timing.py copione.txt --voce lipsync --lento S3,S7
    python3 timing.py copione.txt --voce lipsync --obiettivo 20-30   # il loop del mercoledì ha la sua misura

Il copione: una riga per scena. Prefissi ammessi e ignorati nel conteggio: "S1:", "S1 |", "S1 -", "1.".

Misure prese dalla produzione, non inventate:
  lip-sync in campo     = 2.5 parole/sec
  voiceover fuori campo = 2.6 parole/sec
  delivery lento        = 1.6 parole/sec
  montato               = circa 2.0 parole/sec (solo controllo veloce: la durata vera è la SOMMA DELLE CLIP)
Tagli di Omni Flash: 4, 6, 8, 10 s, sempre per eccesso.
L'ultima scena è la CTA: si aggiungono 2 s prima di arrotondare (keyword che compare + firma + saluto muto).
Senza CTA nell'ultima scena: --senza-cta.
Crediti (9:16, 720p, x1): 4s=7 · 6s=10 · 8s=12 · 10s=15.
Durata obiettivo: quella dichiarata nel filo del master (--obiettivo), 48-56 s se non si passa (la fascia dei reel migliori).

Blocca (exit 1) solo per: una scena oltre i 10 s (limite di Flow).
Avvisi, che si guardano e non bloccano: montato fuori obiettivo (o si stringe il caso o si scrive il motivo in § Deviazioni);
frasi corte e lunghe; durata uguale al reel uscito prima (--precedente: lo usa Vessel per informare Saverio, non chi scrive,
e non è un motivo per togliere contenuto).
"""
import argparse
import re
import sys

RITMI = {"lipsync": 2.5, "voiceover": 2.6, "lento": 1.6}
RITMO_MONTATO = 2.0
TAGLI = [4, 6, 8, 10]
CREDITI = {4: 7, 6: 10, 8: 12, 10: 15}
CTA_EXTRA = 2.0
PREFISSO = re.compile(r"^\s*(?:[Ss]\s?\d+|\d+)\s*[:.|\-–]\s*")


def parole(testo):
    # i puntini di sospensione e la punteggiatura non sono parole
    return len([p for p in re.split(r"\s+", testo.strip()) if re.search(r"\w", p)])


def frasi(testo):
    pezzi = re.split(r"(?<=[.!?…])\s+", testo.strip())
    return [f for f in pezzi if parole(f) > 0]


def taglio(secondi):
    for t in TAGLI:
        if secondi <= t:
            return t
    return None  # oltre i 10 s: la scena va riscritta più corta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("copione", help="file di testo, una riga per scena")
    ap.add_argument("--voce", choices=["lipsync", "voiceover"], required=True)
    ap.add_argument("--lento", default="", help="scene con delivery lento, es. S3,S7")
    ap.add_argument("--obiettivo", default="48-56", help="durata obiettivo del montato dal filo, es. 50-55 (default 48-56)")
    ap.add_argument("--precedente", type=int, default=0, help="durata del reel uscito subito prima, in secondi")
    ap.add_argument("--bumper", type=int, default=0, help="secondi di asset riusabili (bumper, card) da sommare")
    ap.add_argument("--senza-cta", action="store_true", help="l'ultima scena non è la CTA: niente 2 s in più")
    args = ap.parse_args()

    lente = {s.strip().upper().lstrip("S") for s in args.lento.split(",") if s.strip()}
    try:
        minimo, tetto = (int(x) for x in args.obiettivo.split("-"))
    except ValueError:
        ap.error("--obiettivo va scritto come MIN-MAX, es. 50-55")

    with open(args.copione, encoding="utf-8") as fh:
        righe = [r for r in (l.rstrip() for l in fh) if r.strip()]

    scene, sfori, battute = [], [], []
    for i, riga in enumerate(righe, 1):
        battuta = PREFISSO.sub("", riga).strip()
        n = parole(battuta)
        ritmo = RITMI["lento"] if str(i) in lente else RITMI[args.voce]
        sec = n / ritmo
        extra = CTA_EXTRA if (i == len(righe) and not args.senza_cta) else 0.0
        clip = taglio(sec + extra)
        if clip is None:
            sfori.append((i, n, sec))
        scene.append((i, n, ritmo, sec, extra, clip))
        battute.append(battuta)

    print(f"─── TIMING · voce: {args.voce} ───")
    print(f"{'scena':>5} {'parole':>7} {'p/sec':>6} {'sec':>6} {'clip':>5} {'crediti':>8}")
    tot_sec = tot_cred = 0
    for i, n, ritmo, sec, extra, clip in scene:
        c = CREDITI[clip] if clip else 0
        tot_sec += clip or 0
        tot_cred += c
        nota = "  ⛔ OLTRE 10 s — riscrivere più corta" if not clip else ("  (+2 s CTA)" if extra else "")
        print(f"{'S'+str(i):>5} {n:>7} {ritmo:>6.1f} {sec:>6.1f} {str(clip or '-'):>5} {c:>8}{nota}")
    print(f"{'TOT':>5} {sum(s[1] for s in scene):>7} {'':>6} {'':>6} {tot_sec:>5} {tot_cred:>8}")

    tot_parole = sum(s[1] for s in scene)
    finale = tot_sec + args.bumper
    # stesso conto senza i 2 s della CTA: serve a non bloccare un reel che sfora solo per quelli
    senza_extra = sum((taglio(sec) or 10) for _, _, _, sec, _, _ in scene) + args.bumper
    print(f"\n─── DURATA ───")
    print(f"somma delle clip: {tot_sec} s + asset riusabili {args.bumper} s = {finale} s di montato")
    print(f"controllo veloce (parole ÷ {RITMO_MONTATO}): {tot_parole / RITMO_MONTATO:.0f} s — se si scosta di molto, ricontare")

    lung = [parole(f) for f in frasi(" ".join(battute))]
    corte = [n for n in lung if n < 6]
    lunghe = [n for n in lung if n > 25]
    print(f"\n─── SPIA DI MESTIERE (non blocca) ───")
    print(f"frasi: {len(lung)} · sotto le 6 parole: {len(corte)} · sopra le 25 parole: {len(lunghe)}"
          f" — nei parlati approvati ci sono frasi corte e nessuna sopra le 25")

    esiti = [("nessuna scena oltre i 10 s", not sfori)]
    print(f"\n─── OBIETTIVO {minimo}-{tetto} s (avviso, non blocca) ───")
    if minimo <= finale <= tetto:
        print(f"  ✅ {finale} s, dentro l'obiettivo")
    elif minimo <= senza_extra <= tetto:
        print(f"  ⚠️ {finale} s: fuori solo per i 2 s della CTA ({senza_extra} s senza) — si guarda se la CTA ci sta nella clip più corta")
    else:
        print(f"  ⚠️ {finale} s, fuori obiettivo — o si stringe il caso (un'idea in meno, non frasi compresse) "
              f"o si scrive il motivo in § Deviazioni")
    if args.precedente:
        diff = abs(finale - args.precedente)
        print(f"\ninformazione per Saverio: {diff} s di differenza dal reel uscito prima ({args.precedente} s)"
              " — non è un motivo per togliere contenuto")

    print("\n─── ESITO ───")
    for testo, ok in esiti:
        print(f"  {'✅' if ok else '❌'} {testo}")
    verde = all(ok for _, ok in esiti)
    print(f"\n{'🟢 VERDE' if verde else '🔴 ROSSO — si sistema il parlato prima delle immagini'}")
    print(f"Costo animazione: {tot_cred} crediti su {len(scene)} clip")
    return 0 if verde else 1


if __name__ == "__main__":
    sys.exit(main())
