# FOGLIO DI EDITING — Reel «Due PLC che non si parlano. Il permesso passa da me.»
**Progetto:** `2026-09-28_rele-interfaccia-comando-muore` · Reel Instagram 9:16 · **56s** · 7 clip Omni 1.1 Flash (voce già dentro le clip)
**Personaggio:** Mr. Relè d'interfaccia (modulo sottile antropomorfo, lucina verde sullo zoccolo, logo MA) · voce in campo con lip-sync in tutte le clip · Serafino è sempre muto (faccia, occhi, mani: mai la voce)
**Musica:** traccia Lyria «INTERBLOCCO — Mr Automation Academy (bed)», strumentale, 120 BPM (1 battuta = 2s) — prompt al §3
**Chiusura in LOOP:** la S7 finisce esattamente sul primo fotogramma della S1 (`S1_madre.png`). Niente fade in, niente fade a nero: il reel riparte da solo.

> Questo documento è la regia di montaggio completa. Va eseguito nell'ordine: 0 → 1 → 2 → 3 → 4 → 5.
> Le clip si usano **intere, senza tagli interni** (la voce, i silenzi e i gesti sono già temporizzati dentro ogni clip).
> Ogni riga di timing è in **secondi assoluti della timeline** (00:00 = primo frame di S1), frame a 30 fps.
> I tempi interni delle clip (`t`) vengono dai prompt di regia: se in una clip la voce è slittata di qualche decimo,
> **spostare i sottotitoli sulla voce reale**, mai tagliare la clip.
> ⚠️ **S2, S3 e S6 hanno il parlato fitto** (27, 24 e 29 parole in 8, 6 e 8 secondi): lì la voce scivolerà quasi di sicuro. Si spostano le card, mai la clip.
> Clip S7 = **versione v2** (Serafino fermo, relè che rientra nel quadro A).

---

## 0. SPECIFICHE DEL PROGETTO

| Parametro | Valore |
|---|---|
| Risoluzione | 1080 × 1920 px (9:16), verticale. Le clip escono da Flow a 720p: scalarle a 1080 × 1920 |
| Frame rate | 30 fps (conformare le clip a 30 fps con frame blending OFF, optical flow OFF: durata invariata) |
| Durata totale | 56,0s = 1680 frame |
| Audio | 48 kHz, stereo, mix finale −14 LUFS integrati, true peak −1 dBTP |
| Codec export | H.264 High, 14 Mbps VBR 2-pass, AAC 192 kbps, MOV o MP4 |
| Nome file | `2026-09-28_rele-interfaccia-comando-muore.mp4` |

### 0.1 SAFE ZONE — dove il testo NON può stare (overlay di Instagram Reels)
Su un frame 1080 × 1920:
- **Alto: y 0 → 250 px** → nome account, "Reels", audio. **Vietato.**
- **Basso: y 1500 → 1920 px** → caption, nome audio, barra di navigazione. **Vietato.**
- **Destra: x 940 → 1080 px, da y 900 in giù** → colonna like / commenti / condividi / salva. **Vietato.**
- **Sinistra: x 0 → 60 px** → margine di sicurezza.

✅ **Zona sicura per i sottotitoli:** blocco di testo **centrato orizzontalmente**, larghezza massima **860 px** (x 110 → 970),
**centro verticale a y ≈ 1160 px** (60% dell'altezza; il testo occupa circa y 1100 → 1220). Mai più in basso di **y 1440**, mai più in alto di **y 300**.
⚠️ **La lucina verde è la storia del reel e in quattro scene sta proprio a y ≈ 1100-1150** (verificato sui plate): lì le card **scendono a y 1330**, altrimenti la coprono.
| Scena | Centro card | Perché |
|---|---|---|
| S1 | **y 1330** | lucina sullo zoccolo a y ≈ 1110 |
| S2 | y 1160 | lucina a y ≈ 1040, sopra le card |
| S3 | y 1160 | a y 1330 la card coprirebbe la bobina, che la battuta nomina |
| S4 | **y 1330** | lucina grande a y ≈ 1140 |
| S5 | y 1160 | l'impulso che si spegne sta più in alto, verso B |
| S6 | **y 1330** | lucina a y ≈ 1140: è l'AHA, deve restare scoperta |
| S7 | **y 1330** | la clip finisce sul fotogramma di S1 (lucina a y ≈ 1110); l'ologramma INTERBLOCCO sta a y ≈ 700-900, non lo tocca |

### 0.2 STILE DEI SOTTOTITOLI — uguale al reel IO-Link già pubblicato (riferimento)
| Parametro | Valore |
|---|---|
| Testo | **TUTTO MAIUSCOLO**, una riga sola, 3-5 parole per card (mai due righe: se non entra, si spezza la card) |
| Font | bold condensato, tipo Impact / Bebas Neue / Anton |
| Colore | bianco, ombra scura morbida (o contorno nero sottile) per leggerlo su ogni sfondo |
| Parola chiave | **ARANCIONE Mr Automation** (lo stesso del logo MA), **una per card** — nel §2 è la parola in `**grassetto**` |
| Posizione | centrata, centro a y ≈ 1160 (y 1330 in S1, S4, S6, S7: vedi 0.1) |
| Animazione | nessuna: la card appare e sparisce secca sui tempi del §2. Niente karaoke parola per parola, niente pop |
| Card 9 (“HO IL CONSENSO PER PARTIRE?”) | è la domanda della linea B citata dal relè: stesso stile, fra virgolette “ ”, CONSENSO in arancione |
| Card 33 | nel copione c'è «é probabile»: nel sottotitolo si scrive **È** (è il verbo, e la voce lo dice così) |
| Card 41 (`COMMENTA INTERBLOCCO 👇`) | INTERBLOCCO in arancione + emoji 👇 alla fine |
Nessun altro testo o grafica in post: la keyword INTERBLOCCO (S7, ologramma) e la tagline (detta dal relè) sono **già dentro le clip**: l'ologramma non si ridisegna, la tagline non si scrive a schermo oltre alla sua card.

---

## 1. TIMELINE MASTER

| Scena | Clip | IN | OUT | Durata | Transizione IN | Note |
|---|---|---|---|---|---|---|
| S1 | clip S1 (madre: relè sulla canalina del quadro A, lucina verde, Serafino allo sportello, colonna rossa di B in fondo) | 00:00.0 | 00:10.0 | 10,0s | **Nessuna**: primo frame pieno | Niente fade in: il primo frame è anche l'ultimo della S7 (loop) |
| S2 | clip S2 (quadro A grandangolo verso il corridoio, arco ambra da B, impulso verde su «Ok!») | 00:10.0 | 00:18.0 | 8,0s | **Taglio secco**, cade sul beat drop | Parlato fitto: la frase finisce sull'ultimo frame |
| S3 | clip S3 (dentro il relè in sezione: bobina arancione sotto, contatto verde sopra) | 00:18.0 | 00:24.0 | 6,0s | **Taglio secco** + whoosh "dentro" | Clip fitta, **non stringere** |
| S4 | clip S4 (quadro A dal basso: lucina grande, filo verde che sale, occhio sfocato di Serafino) | 00:24.0 | 00:30.0 | 6,0s | **Taglio secco** su battuta musicale | La domanda «Ma PLC B l'ha ricevuto?» |
| S5 | clip S5 (passerella a terra: relè in equilibrio sul cavo, impulsi verdi che si spengono prima di B) | 00:30.0 | 00:38.0 | 8,0s | **Taglio secco** su battuta musicale | La clip ha già il suo push-in lento |
| S6 | clip S6 (quadro B: LED del PLC B tutti spenti, unica luce verde = la lucina del relè) | 00:38.0 | 00:46.0 | 8,0s | **Taglio secco + accento** (vedi SFX) | Qui sta l'AHA: unico punch-in del reel |
| S7 | clip S7 v2 (dall'alto sul cavo → ologramma INTERBLOCCO → rientro nel quadro A = frame di S1) | 00:46.0 | 00:56.0 | 10,0s | **Taglio secco** su battuta musicale | L'ultimo frame è il primo di S1: **nessun fade**, nessun fermo immagine |

**Regola dei tagli:** tutti i tagli cadono su multipli di 2s (10 · 18 · 24 · 30 · 38 · 46 · 56) = sempre sull'inizio di una battuta musicale a 120 BPM.
**Non tagliare mai** dentro una clip per "stringere": i silenzi dentro le clip sono recitazione, non tempo morto.

---

## 2. REGIA SCENA PER SCENA

Legenda: `T` = tempo assoluto timeline · `t` = tempo interno della clip · 🎙 voce · 🔤 sottotitolo · ✂️ taglio/transizione · 🎥 movimento in post · 🔊 SFX · 🎵 musica

### S1 — HOOK · SÈGUIMI · T 00:00.0 → 00:10.0 · relè sulla canalina del quadro A, mano aperta verso lo sportello, lucina verde accesa, PLC A a sinistra, Serafino perplesso sul bordo, colonna rossa di B lontana
🎙 **Script:** «La macchina B non parte? I due PLC non si parlano: il consenso passa da me, Sèguimi sono il relè d’interfaccia.»
| T | t | Cosa succede |
|---|---|---|
| 00:00.0–00:01.6 | 0,0–1,6 | 🎙 «La macchina B non parte?» — gli occhi vanno dallo sportello alla camera |
| 00:01.6–00:02.1 | 1,6–2,1 | SILENZIO, occhi in camera. **Non riempire.** |
| 00:02.1–00:03.9 | 2,1–3,9 | 🎙 «I due PLC non si parlano:» |
| 00:03.9–00:05.5 | 3,9–5,5 | 🎙 «il consenso passa da me,» |
| 00:05.5–00:06.3 | 5,5–6,3 | 🎙 «Sèguimi» — la mano fa il cenno «vieni» verso Serafino |
| 00:06.3–00:08.4 | 6,3–8,4 | 🎙 «sono il relè d’interfaccia.» |
| 00:08.4–00:10.0 | 8,4–10,0 | Nessuna parola: sorride in camera, bocca chiusa; Serafino sbatte le palpebre |

🔤 **Sottotitoli** (centro y 1330)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 1 | 00:00.1 | 00:01.7 | LA MACCHINA B NON **PARTE**? |
| 2 | 00:02.1 | 00:02.9 | I DUE PLC |
| 3 | 00:02.9 | 00:04.0 | NON SI **PARLANO**: |
| 4 | 00:04.0 | 00:05.5 | IL **CONSENSO** PASSA DA ME, |
| 5 | 00:05.5 | 00:06.3 | **SÈGUIMI** |
| 6 | 00:06.3 | 00:08.5 | SONO IL RELÈ **D’INTERFACCIA**. |
*(Card 2 senza parola arancione: la parola forte della frase è in card 3. Dal 08,5 al 10,0 nessun testo: il sorriso in silenzio chiude la scena.)*

🎥 **Movimento in post:** la clip è a camera bloccata. **Push-in lentissimo dal 100% al 103% su tutta la clip** (10s, lineare), che **parte dal 100%**: il primo frame resta identico all'ultimo della S7.
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:00.0 → 00:10.0 | Ventilazione d'impianto + ronzio elettrico del quadro aperto | −30 dB | **la clip ha già il suo hum** (è nel prompt): se si sente, usa quello |
| 00:05.6 | "Swish" morbido (0,3s) sul cenno «vieni» | −26 dB | opzionale |

🎵 **Musica:** `[Intro]` da 00:00.0, **−26 dB**, quasi impercettibile: solo pulse e pad. Nessun elemento ritmico prima di 00:10.0.

---

### S2 — INTERBLOCCO · T 00:10.0 → 00:18.0 · grandangolo basso dal fianco del relè verso il corridoio: braccia alzate, filo in alto verde, arco ambra da B verso A, Serafino intero nel corridoio
🎙 **Script:** «Si chiama interblocco: la linea B chiede “ho il consenso per partire?”, la linea A risponde “Ok!”. Quel consenso da A a B lo faccio passare io.»
| T | t | Cosa succede |
|---|---|---|
| 00:10.0 | 0,0 | ✂️ Taglio secco. **Beat drop della musica esattamente qui.** |
| 00:10.0–00:11.2 | 0,0–1,2 | 🎙 «Si chiama interblocco:» — occhi in camera, le braccia scendono all'altezza del petto |
| 00:11.2–00:13.8 | 1,2–3,8 | 🎙 «la linea B chiede “ho il consenso per partire?”,» — la testa si gira un po' verso la colonna rossa |
| 00:13.8–00:15.0 | 3,8–5,0 | 🎙 «la linea A risponde “Ok!”.» — **su «Ok!» (T ≈ 00:14.6) l'impulso verde parte dal filo e corre lungo l'arco verso B** |
| 00:15.0–00:18.0 | 5,0–8,0 | 🎙 «Quel consenso da A a B lo faccio passare io.» — su «io» si batte una mano sul petto; bocca chiusa sull'ultimo frame |

🔤 **Sottotitoli** (centro y 1160)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 7 | 00:10.0 | 00:11.2 | SI CHIAMA **INTERBLOCCO**: |
| 8 | 00:11.2 | 00:12.2 | LA LINEA B CHIEDE |
| 9 | 00:12.2 | 00:13.8 | “HO IL **CONSENSO** PER PARTIRE?” |
| 10 | 00:13.8 | 00:15.0 | LA LINEA A RISPONDE “**OK!**” |
| 11 | 00:15.0 | 00:15.8 | QUEL CONSENSO |
| 12 | 00:15.8 | 00:16.6 | DA A A B |
| 13 | 00:16.6 | 00:18.0 | LO FACCIO PASSARE **IO**. |
*(Card 8, 11 e 12 senza parola arancione. Parlato fitto: se la voce corre avanti o resta indietro, si spostano le card sulla voce reale.)*

🎥 **Movimento in post:** la clip è a camera bloccata. **Push-in lentissimo dal 100% al 103% su tutta la clip** (8s, lineare).
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:10.0 | Whoosh corto e secco (0,25s) sul taglio, a sostegno del beat drop | −18 dB | |
| 00:10.0 → 00:18.0 | Hum d'impianto continuo | −30 dB | |
| 00:14.6 | Chime morbido ascendente sull'impulso verde che parte | −22 dB | **già nella clip** (è nel prompt): se si sente, usa quello e non raddoppiare |
| 00:17.4 | "Tock" morbido sulla mano che batte il petto | −26 dB | opzionale |

🎵 **Musica:** `[Beat Drop]` **parte a 00:10.0**, −22 dB sotto la voce (ducking −6 dB quando parla).

---

### S3 — DENTRO DI ME · T 00:18.0 → 00:24.0 · il relè in sezione su fondo scuro: bobina di rame arancione sotto, contatto verde sopra, molla e ancora a sinistra, il relè piccolo in mezzo a braccia aperte
🎙 **Script:** «In reparto mi chiamate relè d’appoggio: la bobina sta nel circuito della Linea A e il mio contatto porta il consenso al PLC B.»
| T | t | Cosa succede |
|---|---|---|
| 00:18.0 | 0,0 | ✂️ Taglio secco sulla battuta musicale: **si entra nel relè** |
| 00:18.0–00:19.8 | 0,0–1,8 | 🎙 «In reparto mi chiamate relè d’appoggio:» — occhi in camera |
| 00:19.8–00:21.8 | 1,8–3,8 | 🎙 «la bobina sta nel circuito della Linea A» — occhiata giù alla bobina arancione e ritorno |
| 00:21.8–00:24.0 | 3,8–6,0 | 🎙 «e il mio contatto porta il consenso al PLC B.» — su «contatto» una piccola spinta del palmo verso il contatto verde; bocca chiusa sull'ultimo frame |

🔤 **Sottotitoli** (centro y 1160)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 14 | 00:18.0 | 00:18.8 | IN REPARTO MI CHIAMATE |
| 15 | 00:18.8 | 00:19.8 | RELÈ **D’APPOGGIO**: |
| 16 | 00:19.8 | 00:20.8 | LA **BOBINA** STA NEL CIRCUITO |
| 17 | 00:20.8 | 00:21.8 | DELLA LINEA A |
| 18 | 00:21.8 | 00:22.8 | E IL MIO **CONTATTO** PORTA |
| 19 | 00:22.8 | 00:24.0 | IL CONSENSO AL PLC **B**. |
*(Card 14 e 17 senza parola arancione. Clip fitta: le card durano circa 1s, se la voce slitta si spostano, non si allungano oltre il taglio.)*

🎥 **Movimento in post:** la clip è a camera bloccata. **Push-in lentissimo dal 100% al 103% su tutta la clip** (6s, lineare).
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:18.0 | Whoosh "dentro" (0,3s, leggermente ovattato) sul taglio | −18 dB | |
| 00:18.0 → 00:24.0 | Ronzio basso e costante della bobina eccitata | −30 dB | **già nella clip** (è nel prompt): se si sente, usa quello |
| 00:22.0 | "Tic" metallico leggero sulla spinta del palmo verso il contatto | −26 dB | opzionale |

🎵 **Musica:** `[Groove]` da 00:18.0 a 00:24.0, −22 dB, ducking −6 dB sotto la voce.

---

### S4 — LA LUCINA · T 00:24.0 → 00:30.0 · quadro A dal basso, vicinissimo: relè con la mano a visiera, lucina verde grande, filo verde che sale in canalina, volto gigante sfocato di Serafino a destra
🎙 **Script:** «Qui la lucina è accesa: PLC A ha dato il consenso. Ma PLC B l’ha ricevuto?»
| T | t | Cosa succede |
|---|---|---|
| 00:24.0 | 0,0 | ✂️ Taglio secco sulla battuta musicale |
| 00:24.0–00:25.6 | 0,0–1,6 | 🎙 «Qui la lucina è accesa:» — la mano scende dalla visiera e si apre, palmo in su, verso la lucina |
| 00:25.6–00:27.4 | 1,6–3,4 | 🎙 «PLC A ha dato il consenso.» — occhi in camera |
| 00:27.4–00:27.7 | 3,4–3,7 | SILENZIO. **Non riempire.** |
| 00:27.7–00:29.8 | 3,7–5,8 | 🎙 «Ma PLC B l’ha ricevuto?» — gli occhi salgono al filo verde; dietro, anche gli occhi di Serafino salgono |
| 00:29.8–00:30.0 | 5,8–6,0 | Nessuna parola, bocca chiusa |

🔤 **Sottotitoli** (centro y 1330)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 20 | 00:24.0 | 00:25.6 | QUI LA **LUCINA** È ACCESA: |
| 21 | 00:25.6 | 00:26.5 | PLC A HA DATO |
| 22 | 00:26.5 | 00:27.4 | IL **CONSENSO**. |
| 23 | 00:27.7 | 00:29.8 | MA PLC B L’HA **RICEVUTO**? |
*(Card 21 senza parola arancione. Fra card 22 e 23 lo schermo resta senza testo: il silenzio si vede anche nel sottotitolo.)*

🎥 **Movimento in post:** la clip è a camera bloccata. **Push-in lentissimo dal 100% al 103% su tutta la clip** (6s, lineare).
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:24.0 | Whoosh leggero (0,2s) sul taglio | −20 dB | |
| 00:24.0 → 00:30.0 | Hum d'impianto + ronzio del quadro | −30 dB | già nella clip: non raddoppiare |
| 00:27.7 | Micro "hm?" strumentale: tono corto ascendente (glissando 0,3s, tipo marimba) sul «Ma» | −24 dB | opzionale |

🎵 **Musica:** `[Tension]` da 00:24.0 a 00:30.0: **solo basso pulsante e il tick**, −24 dB. Nel silenzio la musica **resta**, non sale.

---

### S5 — NEL CAVO · T 00:30.0 → 00:38.0 · rasoterra lungo la passerella a rete: il relè in equilibrio sul cavo grigio, impulsi verdi nella guaina che si spengono prima del quadro B, Serafino accovacciato, colonna rossa in fondo
🎙 **Script:** «Allora seguiamo il consenso nel cavo, fino a B: se il segnale arriva, il LED d’ingresso del PLC B si accende.»
| T | t | Cosa succede |
|---|---|---|
| 00:30.0 | 0,0 | ✂️ Taglio secco sulla battuta musicale: **si esce dal quadro** |
| 00:30.0–00:32.4 | 0,0–2,4 | 🎙 «Allora seguiamo il consenso nel cavo,» — ondeggia sul cavo, braccia in equilibrio |
| 00:32.4–00:33.4 | 2,4–3,4 | 🎙 «fino a B:» — la mano indica all'indietro la colonna rossa di B, la testa si gira di 3/4 |
| 00:33.4–00:38.0 | 3,4–8,0 | 🎙 «se il segnale arriva, il LED d’ingresso del PLC B si accende.» — gli impulsi verdi corrono verso B e **si spengono prima di arrivarci**; bocca chiusa sull'ultimo frame |

🔤 **Sottotitoli** (centro y 1160)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 24 | 00:30.0 | 00:31.2 | ALLORA SEGUIAMO IL CONSENSO |
| 25 | 00:31.2 | 00:33.4 | NEL **CAVO**, FINO A B: |
| 26 | 00:33.4 | 00:34.6 | SE IL **SEGNALE** ARRIVA, |
| 27 | 00:34.6 | 00:35.9 | IL **LED** D’INGRESSO |
| 28 | 00:35.9 | 00:38.0 | DEL PLC B SI **ACCENDE**. |
*(Card 24 senza parola arancione.)*

🎥 **Movimento in post:** nessuno (push-in lento già nella clip). Scala 100%.
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:30.0 | Whoosh leggero (0,2s) sul taglio | −20 dB | |
| 00:30.0 → 00:38.0 | Hum del capannone + sussurro elettrico lungo il cavo | −30 dB | **già nella clip** (è nel prompt): se si sente, usa quello |
| 00:35.0 → 00:37.0 | Due-tre "blip" soffici (40 ms) che calano di volume, sugli impulsi che si spengono verso B | −28 → −34 dB | opzionale |

🎵 **Musica:** `[Chase]` da 00:30.0 a 00:38.0, −22 dB, ducking −6 dB sotto la voce.

---

### S6 — LED SPENTO (AHA) · T 00:38.0 → 00:46.0 · quadro B: il relè con le mani in testa, i LED del PLC B tutti spenti, l'unica luce verde è la sua lucina; faccia sfocata di Serafino allo sportello, colonna rossa dietro
🎙 **Script:** «Se qui il LED è spento e la lucina di A è accesa é probabile che il segnale si è interrotto tra il relè e l’ingresso del PLC B.»
| T | t | Cosa succede |
|---|---|---|
| 00:38.0 | 0,0 | ✂️ Taglio secco: **l'AHA arriva di colpo**, punch-in + accento sonoro (vedi 🎥 e SFX) |
| 00:38.0–00:39.6 | 0,0–1,6 | 🎙 «Se qui il LED è spento» — le mani lasciano la testa, un palmo si apre verso i moduli spenti del PLC B |
| 00:39.6–00:41.0 | 1,6–3,0 | 🎙 «e la lucina di A è accesa» — occhi giù sulla sua lucina e ritorno in camera |
| 00:41.0–00:46.0 | 3,0–8,0 | 🎙 «é probabile che il segnale si è interrotto tra il relè e l’ingresso del PLC B.» — bocca chiusa sull'ultimo frame |

🔤 **Sottotitoli** (centro y 1330)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 29 | 00:38.0 | 00:38.8 | SE QUI IL LED |
| 30 | 00:38.8 | 00:39.6 | È **SPENTO** |
| 31 | 00:39.6 | 00:40.3 | E LA LUCINA DI A |
| 32 | 00:40.3 | 00:41.0 | È **ACCESA** |
| 33 | 00:41.0 | 00:42.2 | È **PROBABILE** CHE IL SEGNALE |
| 34 | 00:42.2 | 00:43.4 | SI È **INTERROTTO** |
| 35 | 00:43.4 | 00:44.3 | TRA IL RELÈ |
| 36 | 00:44.3 | 00:46.0 | E L’INGRESSO DEL PLC B. |
*(Card 29, 31, 35 e 36 senza parola arancione. Parlato fitto: si spostano le card sulla voce reale. La lucina verde in basso deve restare **scoperta** per tutta la scena.)*

🎥 **Movimento in post:** **punch-in secco del 5%** (scala 100 → 105) a **00:38.0**, esatto sul taglio, in 2 frame; tenere 105% fino alla fine della clip. È l'unico punch-in del reel: serve a dire "qui sta la prova". ⚠️ Al 105% la lucina del relè e i moduli del PLC B restano in campo; il volto di Serafino al bordo destro si taglia appena: va bene.
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:38.0 | "Thump" sub (80 Hz, 0,25s) + impatto corto e secco sul taglio, sotto il punch-in | −16 dB | |
| 00:38.0 → 00:46.0 | Hum d'impianto + ronzio del quadro | −30 dB | già nella clip: non raddoppiare |
| 00:38.9 | Micro "uh-oh" strumentale: due note discendenti corte (0,25s) su «spento» | −24 dB | opzionale |

🎵 **Musica:** `[Reveal]` da 00:38.0 a 00:46.0: via tutto tranne il basso pulsante, entra il pad sospeso, −24 dB; ducking −6 dB sotto la voce.

---

### S7 — CTA INTERBLOCCO · loop · T 00:46.0 → 00:56.0 · dall'alto sul cavo: il relè con la mano aperta verso camera, Serafino accovacciato e fermo; ologramma INTERBLOCCO; la camera rientra nel quadro A e si posa sul fotogramma di S1
🎙 **Script:** «Quindi controlli il cavo, poi il mio contatto. Vuoi imparare come creare un interblocco? Commenta INTERBLOCCO. Mr. Automation Italia: dove la curiosità diventa competenza.»
| T | t | Cosa succede |
|---|---|---|
| 00:46.0 | 0,0 | ✂️ Taglio secco sulla battuta musicale |
| 00:46.0–00:48.6 | 0,0–2,6 | 🎙 «Quindi controlli il cavo, poi il mio contatto.» — su «contatto» gli occhi del relè scendono sul proprio corpo |
| 00:48.6–00:50.6 | 2,6–4,6 | 🎙 «Vuoi imparare come creare un interblocco?» — occhi in camera |
| 00:50.6–00:51.8 | 4,6–5,8 | 🎙 «Commenta INTERBLOCCO.» — **a T ≈ 00:51.3 l'ologramma INTERBLOCCO appare sopra la mano aperta** (già nella clip: non aggiungere grafica) |
| 00:51.8–00:53.0 | 5,8–7,0 | L'ologramma fluttua, poi si dissolve in scintille |
| 00:52.0–00:55.4 | 6,0–9,4 | 🎙 «Mr. Automation Italia: dove la curiosità diventa competenza.» |
| 00:53.0–00:55.6 | 7,0–9,6 | La camera scorre lungo il cavo, entra nel quadro A e si posa sul fotogramma di S1 |
| 00:55.4–00:56.0 | 9,4–10,0 | Nessuna parola: fotogramma di S1, bocca chiusa. **Il reel riparte da qui: niente fade, niente fermo immagine** |

🔤 **Sottotitoli** (centro y 1330)
| Card | IN | OUT | Testo |
|---|---|---|---|
| 37 | 00:46.0 | 00:47.3 | QUINDI CONTROLLI IL **CAVO**, |
| 38 | 00:47.3 | 00:48.6 | POI IL MIO **CONTATTO**. |
| 39 | 00:48.6 | 00:49.6 | VUOI IMPARARE COME |
| 40 | 00:49.6 | 00:50.6 | CREARE UN **INTERBLOCCO**? |
| 41 | 00:50.6 | 00:51.8 | COMMENTA **INTERBLOCCO** 👇 |
| 42 | 00:52.0 | 00:53.4 | MR. AUTOMATION ITALIA: |
| 43 | 00:53.4 | 00:55.4 | DOVE LA CURIOSITÀ DIVENTA **COMPETENZA**. |
*(Card 39 e 42 senza parola arancione. Dal 55,4 al 56,0 nessun testo: l'ultimo fotogramma deve essere identico al primo della S1, che non ha card.)*

🎥 **Movimento in post:** nessuno (il movimento di camera è già nella clip). Scala 100%.
🔊 **SFX**
| T | Suono | Livello | Nota |
|---|---|---|---|
| 00:46.0 | Whoosh morbido e "aperto" (0,3s) sul taglio, senza thump | −20 dB | |
| 00:51.3 | Shimmer olografico (chime cristallino, 0,5s) sull'apparire di INTERBLOCCO | −18 dB | **già nella clip** (è nel prompt): se si sente, usa quello e non raddoppiare |
| 00:52.6 | Shimmer più soffice e discendente (0,4s) sulla dissolvenza | −22 dB | idem |
| 00:53.0 → 00:55.6 | Whoosh arioso sul rientro nel quadro A | −24 dB | idem |

🎵 **Musica:** `[Resolution]` da 00:46.0 (−22 dB), poi `[End]` da 00:52.0: il groove si ritira e **torna il solo pulse + pad dell'Intro**, così al riavvio del reel la musica si riaggancia senza salto. Taglio netto a 00:56.0 sul downbeat, **nessuna coda di riverbero**.

---

## 3. MUSICA — prompt Lyria + foglio tagli

**Nome traccia:** `INTERBLOCCO — Mr Automation Academy (bed)` · generare **2-3 take**, scegliere quello con il beat drop più pulito.

```
Instrumental only, no vocals, no lead melody. Light, curious electronic bed for a short technical explainer — the feeling of an expert guide leading a colleague along a signal, a small investigation that ends with a clear answer. Slightly sly, never comic, never dramatic. 120 BPM, straight 4/4, steady. Palette: soft sub-bass pulse, muted analog kick, a dry tick/rimshot on the off-beats, a gentle low-register synth plucks pattern, airy wide pad far in the background. Keep the whole arrangement OUT of the 300 Hz – 3 kHz band: no melody, no bright synths, no hi-hats in that range — the human voice must sit on top untouched. Low density, lots of air.
[Intro] pulse and pad only, almost subliminal
[Beat Drop] kick and tick enter cleanly on the downbeat, the plucks pattern starts
[Groove] the pattern settles, a little warmer and closer
[Tension] plucks and pad drop out, only the sub-bass pulse and the tick remain, slightly darker
[Chase] the pattern returns with a light forward-driving bass line, like following something along a path
[Reveal] everything stops except the sub-bass pulse, a suspended pad enters alone
[Resolution] full groove, warm and relieved
[End] the groove leaves, back to the pulse and pad of the intro, ready to start again, clean stop with no reverb tail
```

**Foglio tagli (si fa in montaggio, non nel prompt):**
| Sezione | T IN | T OUT | Livello | Nota |
|---|---|---|---|---|
| `[Intro]` | 00:00.0 | 00:10.0 | −26 dB | solo pulse + pad |
| `[Beat Drop]` | 00:10.0 | 00:18.0 | −22 dB | il kick entra **esattamente** a 00:10.0 (allineare il downbeat del take al frame 300) |
| `[Groove]` | 00:18.0 | 00:24.0 | −22 dB | ducking −6 dB sotto la voce |
| `[Tension]` | 00:24.0 | 00:30.0 | −24 dB | taglio secco dentro il take sul downbeat più vicino; solo basso + tick |
| `[Chase]` | 00:30.0 | 00:38.0 | −22 dB | il pattern torna e spinge in avanti; ducking −6 dB sotto la voce |
| `[Reveal]` | 00:38.0 | 00:46.0 | −24 dB | solo basso + pad sospeso, sotto il punch-in |
| `[Resolution]` | 00:46.0 | 00:52.0 | −22 dB | groove pieno |
| `[End]` | 00:52.0 | 00:56.0 | −22 → −26 dB | torna al pulse + pad dell'Intro, stop netto a 00:56.0 (frame 1680), nessuna coda |
Tutti i tagli interni al take vanno sui **downbeat** (multipli di 2s dal beat drop): se il take non ha una sezione dove serve, si taglia e si incolla il take sul downbeat, con crossfade di 2 frame. **Prova del loop:** metti in play gli ultimi 2s e i primi 2s di seguito: niente salto di volume né di texture.

---

## 4. MIX AUDIO — ordine delle tracce e livelli

| Traccia | Contenuto | Livello di riferimento | Note |
|---|---|---|---|
| A1 | Voce + audio originale delle 7 clip | −16 LUFS short-term sulla voce | **Non separare la voce dall'ambiente della clip**: sono nello stesso file. EQ: high-pass 80 Hz, de-esser leggero se serve. Nessun compressore aggressivo. |
| A2 | SFX aggiunti (§2) | come indicato riga per riga | Se la clip ha già un suono equivalente (chime S2, ronzio bobina S3, chime e whoosh S7), l'SFX aggiunto si **omette**: mai raddoppiare |
| A3 | Hum d'impianto continuo (un solo loop per tutto il reel) | −30 dB | Serve a mascherare i cambi di rumore di fondo fra clip; crossfade di 10 frame su ogni taglio. In S3 (dentro il relè) scende a −36 dB |
| A4 | Musica (§3) | come da foglio tagli | Sidechain/ducking −6 dB dalla A1 (attacco 30 ms, rilascio 250 ms) |
| Master | | −14 LUFS integrati, −1 dBTP | Limiter trasparente, niente maximizer |

---

## 5. CHECKLIST PRIMA DELL'EXPORT
- [ ] 7 clip intere, nessun taglio interno; durata totale **56,0s = 1680 frame**; S7 = versione v2
- [ ] Tagli a 10 · 18 · 24 · 30 · 38 · 46 · 56 — tutti su downbeat della musica
- [ ] **Nessun fade** né all'inizio né alla fine: l'ultimo frame della S7 è il primo della S1 (loop); nessun fermo immagine
- [ ] Punch-in **solo** a 00:38.0 (S6); push-in in post **solo** su S1 (che parte dal 100%), S2, S3, S4; S5 e S7 a scala 100%
- [ ] 43 card di sottotitoli, MAIUSCOLE, bold condensato, bianco + parola chiave arancione MA, larghezza ≤ 860 px; centro **y 1160** in S2, S3, S5 e **y 1330** in S1, S4, S6, S7 (la lucina verde resta sempre scoperta); **nessun testo** nei silenzi (1,7-2,1 · 8,5-10,0 · 27,4-27,7 · 29,8-30,0 · 51,8-52,0 · 55,4-56,0)
- [ ] Card 33 scritta **È PROBABILE** (con l'accento giusto)
- [ ] Nessuna grafica aggiunta su INTERBLOCCO (S7): l'ologramma è nella clip; la tagline solo come card, nessuna scritta finale
- [ ] Il thump di S6 sta **sul taglio** a 00:38.0, sotto il punch-in
- [ ] Musica: beat drop allineato al frame 300; stop netto al frame 1680; prova del loop fatta
- [ ] Loudness −14 LUFS / −1 dBTP; export H.264 1080×1920 30 fps; nome file `2026-09-28_rele-interfaccia-comando-muore.mp4`
- [ ] Copertina: `04_Riferimenti_Visivi/2026-09-28_rele-interfaccia-comando-muore/copertina.png` (statica, già pronta)
