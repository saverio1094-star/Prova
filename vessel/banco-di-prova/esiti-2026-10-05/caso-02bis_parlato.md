# Caso 02bis · «Ho perso un nodo. Tutta la rete lo sta cercando» · passo 3 · Vessel (copia PROVA 2026-10-05)
Slot lunedì 18:30 → componente con la faccia, in panico: parla **il PLC** (lip-sync), al tu. Keyword NOME.
Fonte unica: `esiti-2026-10-04/caso-02_fatti.md` (F1-F16). Quaderno: 0 voci, nessun contatore da aggiornare.
Primo passaggio, una versione sola.

## 1 · Filo
**Filo:** in PROFINET il PLC il nodo lo cerca **per nome, non per IP**; un nodo nuovo di fabbrica esce senza nome, quindi
finché non gli dai il nome del progetto il PLC non lo trova — **in questo progetto**, dove il PLC non sa chi è collegato a
quale porta e quindi non può darglielo da solo.
**Errore plausibile (scheda, n. 1):** «il ricambio è identico e l'IP è lo stesso: deve funzionare».
**Limite che va detto a voce (scheda, n. 3):** il filo allargato diventa falso («un nodo nuovo non viene mai trovato»): con
la topologia configurata il PLC il nome lo dà da solo (F11). Si dice in una frase (B4) e si nomina il caso («in questo progetto»).
**Durata obiettivo: 50-56 s.** Motivo: un caso, una causa (nome, non IP), il limite del caso, il gesto che lo risolve. Le
altre idee della scheda (guasto vs senza nome dal PC, porta giusta, ricambio usato) restano fuori: ognuna costava una clip.

## 2 · Il discorso
B1. Ho perso un nodo! Il tecnico ha cambiato quello guasto con uno nuovo, identico. E io non lo trovo.
B2. Tu dici: è identico, e l'IP è lo stesso. Ma io non lo cerco per IP. Lo cerco per nome.
B3. All'avvio chiamo ogni nodo col nome del progetto, e solo dopo gli assegno io l'IP. Ma un nodo nuovo di fabbrica esce senza nome.
B4. E il nome, da solo, non posso darglielo: in questo progetto non so chi è collegato a quale porta.
B5. Glielo dai tu dal PC: lo scegli dal MAC, fai lampeggiare il LED per essere sicuro che è lui, e scrivi il nome del progetto.
B6. Eccolo! Per me un nodo è il suo nome. Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

Controllo MA/QUINDI: B1→B2 MA (tu dici identico… ma non per IP) · B2→B3 QUINDI (come lo cerco) · B3→B4 MA (perché allora non
glielo dai tu?) · B4→B5 QUINDI (glielo dai tu) · B5→B6 QUINDI (risponde).

## 3 · Il taglio
| Battuta | Clip | Note |
|---|---:|---|
| B1 → S1 | 8 s | |
| B2 → S2 | 8 s | |
| B3 → S3 | 10 s | |
| B4 → S4 | 8 s | |
| B5 → S5 | 10 s | al limite (10,0 s): se Flow taglia, si toglie «dal PC» (il portatile si vede) |
| B6 → S6 | 10 s | CTA (+2 s) |

Ridondanze tolte arrivando qui: «Quindi lo chiamo, e lui non risponde» (ripeteva B1); «di prima» dopo «l'IP è lo stesso»;
«già» e «ancora» in B1; «Vuoi impararlo?» e «risponde» in B6. Idea tolta per stringere il caso (non frasi compresse): il
dubbio «allora è guasto anche il ricambio?» con la risposta dal PC (F8) — prima versione 58 s con una clip oltre i 10 s.
Nessuna battuta divisa.

## 4 · Piano scena per scena (forma corta)
**Mondo IBRIDO**: linea di una fabbrica di oggi, ferma; quadro elettrico sul lato manutenzione, sportello aperto. Ologrammi
sovrapposti (mai toccati): i **cartellini del nome** sopra ogni nodo, scritte di scena generiche senza marchi (es. «nodo-03»).
**Set A** · dentro il quadro: in basso nella zona logica, su guida DIN, il PLC con la faccia (monogramma MA), lo switch e i
nodi di I/O, cavi di rete RJ45 connessi ai due capi. **Set B** · davanti al quadro aperto: carrello col portatile, cavo di rete
dal portatile a una porta libera dello switch. Si passa da A a B seguendo il cavo che esce dallo switch.
Stato fisso S1-S5: linea ferma, nessuna parte in moto, beacon rosso; LED di link verde sulle porte collegate (il cavo c'è, F9).

| Scena | Set · cosa si vede | Acceso / spento | Gesto ↔ parola |
|---|---|---|---|
| S1 | A · primo piano del PLC in panico; accanto, il nodo nuovo al posto di quello vecchio; sopra gli altri nodi i cartellini col nome, sopra il nuovo un cartellino vuoto | beacon rosso riflesso nel quadro; link verde | il PLC guarda a destra e sinistra su «non lo trovo» |
| S2 | A · accanto al nodo nuovo galleggiano due ologrammi: un numero IP e il cartellino del nome (vuoto) | idem | su «per nome» il PLC fissa il cartellino vuoto; l'IP sbiadisce |
| S3 | A, più largo · fila di nodi: dal PLC parte un impulso lungo i cavi, ogni cartellino col nome si illumina e risponde; quello del nuovo resta grigio | cartellini verdi tranne il nuovo | su «senza nome» il cartellino vuoto tremola |
| S4 | A · fra le porte dello switch e dei nodi, linee tratteggiate con punti di domanda: la mappa porta per porta che manca | idem | il PLC aggrotta le sopracciglia su «non so» |
| S5 | B · Mister Automation al carrello col portatile (schermo: elenco dispositivi con indirizzi MAC, senza marchi); il PLC in primo piano a sinistra nel quadro | il LED di link del nodo nuovo lampeggia | il tecnico preme un tasto su «lampeggiare» |
| S6 | A → linea · il cartellino del nodo si accende col nome; dietro, attraverso lo sportello, la linea riparte (persone fuori dalle parti in moto) | beacon verde, cartellini tutti verdi | il PLC sospira sollevato su «Eccolo!» |

## 5 · Verità battuta per battuta
| Battuta | Affermazione | Fatti |
|---|---|---|
| B1 | «ho perso un nodo»: il PLC non trova il nodo / guasto stazione; il ricambio è nuovo e identico | F4, F5 (termine «guasto stazione» → «nodo perso»); premessa del caso |
| B2 | non lo cerca per IP, lo cerca per nome | F3, F4 · errore plausibile n. 1 |
| B3 | all'avvio chiama ogni nodo configurato col nome del progetto; poi gli assegna lui l'IP; nuovo di fabbrica = senza nome | F4, F3, F16, F2, F1 |
| B4 | in questo progetto il PLC non può dare il nome da solo perché non sa chi è collegato a quale porta (topologia non configurata) | F11 (limite) · errore n. 3 |
| B5 | nome dato a mano dal PC, dispositivo scelto dal MAC, LED fatto lampeggiare per riconoscerlo, nome = quello del progetto | F6, F7, F16 |
| B6 | il PLC lo ritrova (dal nome, poi gli dà l'IP); sintesi «un nodo è il suo nome» | F3, F6 |
Limiti non detti e perché: F11 ha anche altre condizioni (il dispositivo deve supportare la funzione, funzione attiva):
B4 nomina una condizione sufficiente a far fallire il nome automatico, quindi resta vera. F6/F7/F8 sono procedure di un
software preciso: il parlato dice solo il principio (MAC, LED, nome), che è anche in PI §2.5. F13, F14, F15 non servono alla
decisione davanti a questo nodo nuovo con nome dato a mano: restano nella scheda. Nessun «non confermato» usato (le spie
del nodo non dicono «senza nome»: in scena il LED di link è solo verde = cavo).

## Controlli
- **Tempo**: fatto, uscita sotto (VERDE, 54 s, dentro 50-56).
- **Lettore fresco** e **controllo dei limiti**: non lanciati (consegna del giro di prova: niente subagenti).

```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      19    2.5    7.6     8       12
   S2      20    2.5    8.0     8       12
   S3      24    2.5    9.6    10       15
   S4      19    2.5    7.6     8       12
   S5      25    2.5   10.0    10       15
   S6      19    2.5    7.6    10       15  (+2 s CTA)
  TOT     126                  54       81

─── DURATA ───
somma delle clip: 54 s + asset riusabili 0 s = 54 s di montato
controllo veloce (parole ÷ 2.0): 63 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 15 · sotto le 6 parole: 6 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 50-56 s (avviso, non blocca) ───
  ✅ 54 s, dentro l'obiettivo

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 81 crediti su 6 clip
```

## Deviazioni
- **S3 (24 parole) e S5 (25 parole) oltre le ~22 parole in 10 s**: B3 tiene insieme causa e conseguenza (nome prima, IP dopo,
  nuovo = senza nome) e B5 è il gesto completo; dividerle avrebbe portato a 7 clip e fuori obiettivo. S5 è a 10,0 s: riserva
  pronta, togliere «dal PC».
- **Il tecnico non parla, parla solo il PLC** (anche in S5, dove agisce il tecnico): una voce per tutto il reel, come vuole
  lo slot del lunedì; il tecnico fa il gesto.
- **Obiettivo 50-56 invece di 48-56**: motivo scritto nel filo.
