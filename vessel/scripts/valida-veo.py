#!/usr/bin/env python3
"""Validatore della FORMA dei JSON per Google Flow (Omni Flash), prima di spendere crediti.

Uso:
    python3 valida-veo.py <file>                    # .md con i blocchi json, oppure .json
    python3 valida-veo.py <file> --keyword SENSORE  # dichiara la keyword CTA del reel
    python3 valida-veo.py <file> --tetto 56         # controlla anche la durata totale

Controlla, in modo deterministico, le cose che sono costate crediti:
  * chiavi obbligatorie presenti e nell'ordine della forma (modelli/lock-flow.md)
  * `duration_s` fra i tagli di Omni Flash (4/6/8/10), tetto 10 s
  * `voice` e `voice_lock` identici parola per parola in tutte le clip (una sola voce)
  * `hard_constraint` presente e non vuoto
  * niente negativi di STATO in `negative` (negare uno stato fa vibrare l'inquadratura)
  * `camera` = un solo movimento (due movimenti deformano il plate)
  * una sola keyword CTA nel reel (con --keyword, le altre parole in maiuscolo sono solo un avviso)
  * avvisi sui negativi che dipendono dal plate, riusati da un reel vecchio

Non guarda i plate: controlla la forma, non il contenuto. Esce 0 se è verde, 1 se è rosso.
"""
import argparse
import json
import re
import sys

# Ordine della forma (modelli/lock-flow.md).
ORDINE = ["clip", "duration_s", "locked_plate", "character_lock", "voice", "voice_lock", "lip_sync", "line_it",
          "delivery", "timing", "action", "camera", "lights", "sound_design", "hard_constraint", "negative"]
OBBLIGATORIE = ["clip", "duration_s", "locked_plate", "character_lock", "action",
                "camera", "hard_constraint", "negative"]
# Chiavi ammesse in più, senza vincolo d'ordine.
EXTRA = {"voice_placement", "mascot_face", "badge_integrity",
         "reference_usage", "aspect_change", "format", "style", "text_labels"}

TAGLI = [4, 6, 8, 10]
CREDITI = {4: 7, 6: 10, 8: 12, 10: 15}

# Negare uno STATO fa vibrare l'inquadratura: si negano le AZIONI, non gli stati.
NEGATIVI_DI_STATO = ["static shot", "static frame", "frozen frame", "still frame",
                     "no movement", "nothing moves", "motionless camera", "immobile camera"]
# Negativi che dipendono dal PLATE: giusti sul 4/9, distruttivi su plate con occhiali o ologrammi.
NEGATIVI_PLATE_DEPENDENT = ["safety glasses", "hard hat", "on-screen text", "subtitles", "helmet"]
# Un movimento di camera per clip: due o più = plate 2D deformata.
MOVIMENTI_CAMERA = ["push-in", "push in", "pull-out", "pull out", "dolly", "truck", "pan ",
                    "tilt", "orbit", "zoom", "drift", "parallax", "crane", "handheld"]


def blocchi_json(testo):
    """Estrae gli oggetti JSON: dai fence ```json ... ``` o dal file JSON puro."""
    trovati = re.findall(r"```json\s*(.*?)```", testo, re.S)
    if trovati:
        return trovati
    return [testo]


# Alias della forma vecchia (prompt di inizio settembre).
ALIAS = {"source_frame": "locked_plate", "plate": "locked_plate", "acting": "delivery"}


def normalizza(scena, comuni):
    """Fonde il blocco `global` nella scena e traduce gli alias della forma vecchia."""
    unito = dict(comuni)
    unito.update(scena)
    fuori = {}
    for k, v in unito.items():
        fuori[ALIAS.get(k, k)] = v
    if "clip" not in fuori:
        etichetta = " — ".join(str(fuori[k]) for k in ("id", "label") if fuori.get(k))
        if etichetta:
            fuori["clip"] = etichetta
    return fuori


def carica(percorso):
    with open(percorso, encoding="utf-8") as fh:
        testo = fh.read()
    clip, rotti, globale = [], [], False
    for i, blocco in enumerate(blocchi_json(testo), 1):
        blocco = blocco.strip()
        if not blocco:
            continue
        try:
            dato = json.loads(blocco)
        except json.JSONDecodeError as err:
            rotti.append((i, str(err)))
            continue
        for oggetto in (dato if isinstance(dato, list) else [dato]):
            if not isinstance(oggetto, dict):
                continue
            scene = oggetto.get("scenes")
            if isinstance(scene, list):
                globale = True
                comuni = oggetto.get("global") or {}
                clip.extend(normalizza(s, comuni) for s in scene if isinstance(s, dict))
            else:
                clip.append(normalizza(oggetto, {}))
    return [c for c in clip if "clip" in c], rotti, globale


def testo_di(valore):
    if isinstance(valore, list):
        return " ".join(str(v) for v in valore)
    return str(valore or "")


def nome(clip, i):
    return str(clip.get("clip") or f"clip #{i}")


def controlla(clip, i, errori, avvisi, globale):
    et = nome(clip, i)

    mancanti = [k for k in OBBLIGATORIE if k not in clip]
    if mancanti:
        errori.append(f"{et}: chiavi mancanti → {', '.join(mancanti)}")

    if not globale:
        presenti = [k for k in clip if k in ORDINE]
        atteso = [k for k in ORDINE if k in clip]
        if presenti != atteso:
            errori.append(f"{et}: chiavi fuori ordine → {' · '.join(presenti)}"
                          f"\n        atteso: {' · '.join(atteso)}")
        sconosciute = [k for k in clip if k not in ORDINE and k not in EXTRA]
        if sconosciute:
            avvisi.append(f"{et}: chiavi non previste dalla forma → {', '.join(sconosciute)}")

    dur = clip.get("duration_s")
    if not isinstance(dur, (int, float)):
        errori.append(f"{et}: `duration_s` mancante o non numerica")
    elif dur > 10:
        errori.append(f"{et}: durata {dur}s — il tetto rigido è 10s, il menù di Omni Flash si ferma lì")
    elif dur not in TAGLI:
        errori.append(f"{et}: durata {dur}s — i tagli reali sono 4/6/8/10, si arrotonda per ECCESSO")

    if not testo_di(clip.get("hard_constraint")).strip():
        errori.append(f"{et}: `hard_constraint` vuoto — è la chiave che chiude sempre il prompt")

    neg = testo_di(clip.get("negative")).lower()
    stato = [n for n in NEGATIVI_DI_STATO if n in neg]
    if stato:
        errori.append(f"{et}: negativi di STATO → {', '.join(stato)} — negare uno stato fa VIBRARE l'inquadratura")
    plate_dep = [n for n in NEGATIVI_PLATE_DEPENDENT if n in neg]
    if plate_dep:
        avvisi.append(("plate_dep", ", ".join(plate_dep), et))

    cam = testo_di(clip.get("camera")).lower()
    mossi = sorted({m.strip() for m in MOVIMENTI_CAMERA if m in cam})
    if len(mossi) > 1:
        errori.append(f"{et}: `camera` con più movimenti ({', '.join(mossi)}) — deve essere UNA istruzione sola")


def main():
    ap = argparse.ArgumentParser(description="Valida la forma dei JSON per Flow prima di spendere crediti.")
    ap.add_argument("file", help="il .md col master/i prompt, oppure un .json")
    ap.add_argument("--tetto", type=int, default=0, help="durata massima del reel in secondi")
    ap.add_argument("--keyword", default="", help="la keyword CTA del reel (es. SENSORE)")
    args = ap.parse_args()

    clip, rotti, globale = carica(args.file)
    errori, avvisi = [], []

    for i, err in rotti:
        errori.append(f"blocco json #{i} non si legge: {err}")
    if not clip:
        print("Nessun prompt Veo trovato (servono blocchi ```json con la chiave \"clip\").")
        return 1

    for i, c in enumerate(clip, 1):
        controlla(c, i, errori, avvisi, globale)

    # Voce: un motore solo, e stesse parole in tutte le clip che parlano (7/9).
    for campo in ("voice", "voice_lock"):
        valori = {testo_di(c[campo]).strip() for c in clip if c.get(campo)}
        if len(valori) > 1:
            errori.append(f"`{campo}` diverso fra le clip ({len(valori)} versioni) — "
                          f"il motore non ha memoria: un aggettivo diverso = timbro reinterpretato")

    # Keyword CTA: una sola per reel.
    parlate = [(nome(c, i), testo_di(c.get("line_it"))) for i, c in enumerate(clip, 1)]
    kw = {}
    for et, riga in parlate:
        for parola in re.findall(r"\b[A-ZÀ-Ù]{4,}\b", riga):
            kw.setdefault(parola, []).append(et)
    if args.keyword:
        chiave = args.keyword.upper()
        if chiave not in kw:
            errori.append(f"la keyword {chiave} non compare in nessun `line_it`")
        altre = {k: v for k, v in kw.items() if k != chiave}
        if altre:
            avvisi.append("altre parole in maiuscolo nelle battute (sigle?) → " +
                          " · ".join(f"{k} ({', '.join(v)})" for k, v in altre.items()) +
                          " — se una è una seconda CTA, va tolta")
    elif len(kw) > 1:
        errori.append("più keyword CTA in maiuscolo nel reel → " +
                      " · ".join(f"{k} ({', '.join(v)})" for k, v in kw.items()) +
                      " — una sola per reel; se le altre sono sigle (PROFINET, PLC…) passa --keyword")

    durate = [c.get("duration_s") for c in clip if isinstance(c.get("duration_s"), (int, float))]
    totale = sum(durate)
    crediti = sum(CREDITI.get(d, 0) for d in durate)

    forma = "blocco `global` + `scenes` (forma vecchia)" if globale else "un JSON autonomo per clip"
    print(f"─── VALIDAZIONE JSON FLOW · {len(clip)} clip · {forma} ───")
    for i, c in enumerate(clip, 1):
        d = c.get("duration_s")
        voce = "parlata" if c.get("line_it") else "muta"
        print(f"  {nome(c, i):<34} {str(d)+'s':>5} · {voce}")
    print(f"  {'TOTALE':<34} {str(totale)+'s':>5} · {crediti} crediti")

    if args.tetto:
        if totale > args.tetto:
            errori.append(f"durata totale {totale}s oltre il tetto di {args.tetto}s "
                          f"(la durata è la SOMMA DEI CLIP, mai dei secondi di parlato)")

    # I plate-dependent si raggruppano: se vengono dal blocco `global` sono UNA cosa sola, non nove.
    gruppi, sciolti = {}, []
    for a in avvisi:
        if isinstance(a, tuple) and a[0] == "plate_dep":
            gruppi.setdefault(a[1], []).append(a[2])
        else:
            sciolti.append(a)
    righe = list(sciolti)
    for elenco, clips in gruppi.items():
        dove = "in tutte le clip" if len(clips) == len(clip) else " · ".join(clips)
        righe.append(f"negativi che dipendono dal plate ({dove}) → {elenco}. "
                     f"Giusti dove non c'è testo bakeato, distruttivi su un plate con occhiali o scritte "
                     f"olografiche: si riscrivono su QUESTO plate, non si riusano")
    if righe:
        print("\n─── DA GUARDARE (non blocca) ───")
        for a in righe:
            print(f"  ⚠️  {a}")

    print("\n─── ESITO (forma dei JSON) ───")
    if errori:
        for e in errori:
            print(f"  ❌ {e}")
        print("\n🔴 ROSSO — si sistema PRIMA di generare")
        return 1
    print("  ✅ chiavi, ordine e durate a norma")
    print("  ✅ una voce sola, identica in tutte le clip")
    print("  ✅ hard_constraint presente ovunque")
    print("  ✅ nessun negativo di stato · camera = una istruzione")
    print("  ✅ keyword CTA unica")
    if globale:
        print("  ℹ️  ordine delle chiavi non controllato: in forma `global` + `scenes` lo decide l'espansione")
    print("\n🟢 VERDE — la forma è a posto. Il contenuto si controlla sui plate, a occhio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
