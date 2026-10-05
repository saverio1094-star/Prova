#!/usr/bin/env python3
"""PIANO DI LANCIO in PDF per chi pubblica (Serafino) — 26/9/2026.
Saverio: «un PDF facile da leggere, senza muri di testo, con le azioni subito da fare, tabelle, titoli ben visibili».
Il testo lo scrive Offering in markdown semplice; questo script lo impagina (HTML + Chrome headless → PDF).

Uso:
    python3 lancio-pdf.py <slug>_PIANO-LANCIO.md [-o <uscita.pdf>]

Sintassi della sorgente (solo questa, niente altro):
    # Titolo del documento           -> testata scura
    > riga                          -> riquadro arancione (avvisi, "in breve")
    ## 1 · ⏱️ SUBITO · Titolo azione -> scheda azione (numero · quando · cosa)
    ### Sottotitolo                  -> sottotitolo dentro la scheda
    - punto  /  - [ ] da spuntare   -> elenco / casella
    | a | b |  (tabella markdown)    -> tabella
    ```copia Etichetta               -> blocco COPIA E INCOLLA (fino a ```)
    **grassetto**, righe normali     -> testo
Senza -o l'uscita è <sorgente>.pdf (senza _PIANO-LANCIO.md → _PIANO-LANCIO.pdf) nella stessa cartella.
Verifica dopo: `mdls -name kMDItemNumberOfPages <pdf>` + aprire il PDF.
"""
import argparse
import html
import os
import re
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 14mm 13mm 14mm 13mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 13.5pt; line-height: 1.4;
       color: #151515; margin: 0; }
.head { background: #0D0D0D; color: #fff; border-radius: 10px; padding: 16px 20px; margin-bottom: 14px; }
.head h1 { margin: 0; font-size: 24pt; line-height: 1.15; letter-spacing: .2px; }
.head .ma { color: #FF6A00; font-weight: 800; font-size: 11pt; letter-spacing: 2px; margin-bottom: 4px; }
.note { background: #FFF1E6; border-left: 6px solid #FF6A00; border-radius: 6px; padding: 9px 14px; margin: 10px 0;
        font-size: 13pt; }
.note p { margin: 2px 0; }
.card { border: 2px solid #E3E3E3; border-radius: 10px; margin: 14px 0; overflow: hidden; break-inside: avoid; }
.card .bar { display: flex; align-items: stretch; background: #0D0D0D; color: #fff; }
.card .num { background: #FF6A00; color: #fff; font-weight: 900; font-size: 22pt; padding: 6px 16px;
             display: flex; align-items: center; }
.card .when { font-weight: 800; font-size: 12pt; color: #FFB27A; padding: 0 0 0 14px; display: flex; align-items: center;
              white-space: nowrap; }
.card .what { font-weight: 800; font-size: 16pt; padding: 8px 14px; display: flex; align-items: center; }
.card .body { padding: 8px 16px 10px 16px; }
h3 { font-size: 13.5pt; margin: 10px 0 4px 0; color: #0D0D0D; text-transform: uppercase; letter-spacing: .5px; }
h2.plain { font-size: 16pt; margin: 18px 0 6px 0; border-bottom: 3px solid #FF6A00; padding-bottom: 3px; }
ul { margin: 4px 0 6px 0; padding-left: 22px; }
li { margin: 3px 0; }
li.check { list-style: none; margin-left: -22px; }
li.check::before { content: "☐"; font-size: 16pt; color: #FF6A00; margin-right: 8px; vertical-align: -2px; }
p { margin: 5px 0; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 12.5pt; break-inside: avoid; }
th { background: #0D0D0D; color: #fff; text-align: left; padding: 7px 9px; }
td { border-bottom: 1px solid #DDD; padding: 7px 9px; vertical-align: top; }
tr:nth-child(even) td { background: #F6F6F6; }
.copy { border: 2px dashed #FF6A00; border-radius: 8px; margin: 8px 0 10px 0; background: #FAFAFA; break-inside: avoid; }
.copy .lab { background: #FF6A00; color: #fff; font-weight: 800; font-size: 11pt; padding: 4px 10px;
             letter-spacing: .5px; border-radius: 5px 5px 0 0; }
.copy pre { margin: 0; padding: 10px 12px; font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
            font-size: 13.5pt; white-space: pre-wrap; word-wrap: break-word; }
.foot { margin-top: 16px; font-size: 10pt; color: #777; text-align: center; }
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
    out = ["<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr>"]
    for r in cells[1:]:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    return "".join(out) + "</table>"


def card_head(t):
    # "1 · ⏱️ SUBITO · Pubblica e ripubblica"  -> numero · quando · cosa
    parts = [p.strip() for p in t.split("·")]
    if len(parts) >= 3 and parts[0].isdigit():
        return (f'<div class="bar"><div class="num">{inline(parts[0])}</div>'
                f'<div class="when">{inline(parts[1])}</div>'
                f'<div class="what">{inline(" · ".join(parts[2:]))}</div></div>')
    return f'<div class="bar"><div class="what">{inline(t)}</div></div>'


def render(md):
    lines = md.splitlines()
    out, i, in_card, lst = [], 0, False, None

    def close_list():
        nonlocal lst
        if lst:
            out.append("</ul>")
            lst = None

    def close_card():
        nonlocal in_card
        close_list()
        if in_card:
            out.append("</div></div>")
            in_card = False

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("```"):
            close_list()
            lab = s[3:].strip()
            lab = lab[5:].strip() if lab.lower().startswith("copia") else lab
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            out.append(f'<div class="copy"><div class="lab">📋 COPIA E INCOLLA{" · " + inline(lab) if lab else ""}'
                       f'</div><pre>{html.escape(chr(10).join(buf).strip())}</pre></div>')
        elif s.startswith("# "):
            close_card()
            out.append(f'<div class="head"><div class="ma">MR. AUTOMATION ITALIA</div><h1>{inline(s[2:])}</h1></div>')
        elif s.startswith("## "):
            close_card()
            t = s[3:]
            if re.match(r"^\d+\s*·", t):
                out.append(f'<div class="card">{card_head(t)}<div class="body">')
                in_card = True
            else:
                out.append(f'<h2 class="plain">{inline(t)}</h2>')
        elif s.startswith("### "):
            close_list()
            out.append(f"<h3>{inline(s[4:])}</h3>")
        elif s.startswith(">"):
            close_list()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            out.append('<div class="note">' + "".join(f"<p>{inline(b)}</p>" for b in buf if b) + "</div>")
            continue
        elif s.startswith("|"):
            close_list()
            buf = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i])
                i += 1
            out.append(table(buf))
            continue
        elif re.match(r"^[-*] ", s):
            if not lst:
                out.append("<ul>")
                lst = True
            m = re.match(r"^[-*] \[[ xX]?\] (.*)", s)
            if m:
                out.append(f'<li class="check">{inline(m.group(1))}</li>')
            else:
                out.append(f"<li>{inline(s[2:])}</li>")
        elif s in ("", "---"):
            close_list()
        else:
            close_list()
            out.append(f"<p>{inline(s)}</p>")
        i += 1
    close_card()
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    src = os.path.abspath(a.src)
    md = open(src, encoding="utf-8").read()
    out = a.out or re.sub(r"\.md$", "", src) + ".pdf"
    doc = (f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
           f'{render(md)}<div class="foot">Piano di lancio · Mr. Automation Italia</div></body></html>')
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
        tmp = f.name
    if not os.path.exists(CHROME):
        sys.exit(f"Chrome non trovato: {CHROME}. HTML lasciato in {tmp}")
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={os.path.abspath(out)}", "file://" + tmp],
                       capture_output=True, text=True, timeout=120)
    if not os.path.exists(out):
        sys.exit(f"PDF non creato.\n{r.stderr[-800:]}\nHTML in {tmp}")
    os.unlink(tmp)
    print(out)


if __name__ == "__main__":
    main()
