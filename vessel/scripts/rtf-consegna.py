#!/usr/bin/env python3
"""Consegna in RTF nel formato voluto da Saverio (dal 15/9/2026):
ogni blocco = TITOLO in grassetto (con emoji) + corpo in carattere monospaziato su sfondo chiaro.
Il collega apre l'RTF e copia i blocchi uno per uno.

Uso:
    python3 rtf-consegna.py <sorgente.md> [-o <uscita.rtf>] [--editing]

Sorgente = markdown con UN blocco per intestazione:
    ## 📄 Nome file            -> titolo del blocco
    2026-09-15_slug.mp4        -> corpo del blocco (fino alla prossima intestazione)
Le righe `---` e `===` si ignorano. `# Titolo` (H1) diventa il primo blocco solo con --editing.
--editing: anche le `###` diventano blocchi (prefisso ▸), le `##` prendono il prefisso 🎬.
Senza -o l'uscita è <sorgente>.rtf nella stessa cartella.
Verifica dopo: `textutil -convert txt -stdout <uscita.rtf> | head -40`.
"""
import argparse
import os
import re
import sys


def rtf_esc(s):
    out = []
    for ch in s:
        o = ord(ch)
        if ch == '\\':
            out.append('\\\\')
        elif ch == '{':
            out.append('\\{')
        elif ch == '}':
            out.append('\\}')
        elif ch == '\n':
            out.append('\\\n')
        elif o < 128:
            out.append(ch)
        elif o < 0x10000:
            v = o if o < 32768 else o - 65536
            out.append('\\uc0\\u%d ' % v)
        else:  # emoji fuori dal BMP: coppia surrogata
            o -= 0x10000
            hi = 0xD800 + (o >> 10)
            lo = 0xDC00 + (o & 0x3FF)
            out.append('\\uc0\\u%d \\u%d ' % (hi - 65536, lo - 65536))
    return ''.join(out)


HEAD = r"""{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNS-Regular_wdth_opsz110000_GRAD_wght2300000;\f1\fnil\fcharset0 HelveticaNeue;\f2\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;
}
{\colortbl;\red255\green255\blue255;\red236\green235\blue231;\red17\green17\blue17;\red136\green137\blue139;
\red20\green20\blue19;\red229\green231\blue236;}
{\*\expandedcolortbl;;\cssrgb\c94118\c93725\c92549;\cssrgb\c8235\c8235\c8235;\cssrgb\c60392\c60784\c61569;
\cssrgb\c10196\c10196\c9804;\cssrgb\c91765\c92549\c94118;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
"""


def block(title, body):
    # fine riga RTF = UNA barra + a capo (con due barre la barra si stampa nel testo: difetto corretto il 4/10/2026)
    return (r"\pard\pardeftab720\partightenfactor0" + "\n\n"
            r"\f0\b\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0" + "\n"
            r"\outl0\strokewidth0 \strokec2 " + rtf_esc(title) + "\n"
            "\\f1\\b0 \\" + "\n"
            r"\pard\pardeftab720\qr\partightenfactor0" + "\n\n"
            "\\f2\\fs24 \\cf4 \\cb5 \\strokec4 \\" + "\n"
            r"\pard\pardeftab720\partightenfactor0" + "\n"
            r"\cf6 \strokec6 " + rtf_esc(body) + "\\\n"
            r"\pard\pardeftab720\partightenfactor0" + "\n\n"
            "\\f1\\fs28 \\cf2 \\cb1 \\strokec2 \\" + "\n")


def parse(text, editing):
    blocks, title, body = [], None, []

    def flush():
        if title is not None:
            b = re.sub(r'\n{3,}', '\n\n', '\n'.join(body)).strip('\n')
            if b:
                blocks.append((title, b))

    for line in text.split('\n'):
        if re.match(r'^(-{3,}|={3,})\s*$', line):
            continue
        m = re.match(r'^(#{1,3})\s+(.*)$', line)
        if m:
            level, t = len(m.group(1)), m.group(2).strip()
            if level == 1:
                if editing:
                    flush(); title, body = '🎬 ' + t, []
                continue
            if level == 3 and not editing:
                body.append(line); continue
            flush()
            prefix = ('🎬 ' if level == 2 else '▸ ') if editing else ''
            title, body = prefix + t, []
            continue
        if title is None:
            if line.strip():
                title, body = '📄 Intestazione', [line]
            continue
        body.append(line)
    flush()
    return blocks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sorgente')
    ap.add_argument('-o', '--out')
    ap.add_argument('--editing', action='store_true')
    a = ap.parse_args()
    text = open(a.sorgente, encoding='utf-8').read()
    blocks = parse(text, a.editing)
    if not blocks:
        sys.exit('nessun blocco: servono intestazioni `## titolo`')
    out = a.out or os.path.splitext(a.sorgente)[0] + '.rtf'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(HEAD + ''.join(block(t, b) for t, b in blocks) + '}')
    print('%s · %d blocchi' % (out, len(blocks)))
    for t, _ in blocks:
        print('  -', t)


if __name__ == '__main__':
    main()
