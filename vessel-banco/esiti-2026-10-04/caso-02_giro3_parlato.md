# Caso 02 · giro 3 · «Ho perso un nodo. Tutta la rete lo sta cercando» · storia e parlato
Scritto da Vessel il 4/10/2026 (passo 3). Slot lunedì 18:30 → componente con la faccia, in panico. Keyword NOME.
Fonti lette: SKILL.md, fasi/3-storia-parlato.md, quaderno.md (vuoto, nessun contatore da aggiornare), esempi 01-03-05-07,
caso-02_profinet.md, caso-02_fatti.md, LIBRERIA-CTA.md, SET-TIPO.md.

## 1 · Il filo e l'errore plausibile
**Filo:** il PLC trova un nodo PROFINET dal suo **nome**, non dal modello né dall'IP; un nodo nuovo di fabbrica non ha nome,
quindi va trovato dal PC e gli si dà il nome del progetto.
**Errore plausibile (scheda, errori 1 e 2):** «È identico e ha lo stesso IP: deve andare» → no, il PLC cerca il nome e l'IP lo
dà lui (F1-F3). «Non lo trova, quindi è guasto anche il ricambio» → il LED verde dice solo che il cavo c'è; dal PC si legge
«pronto per l'assegnazione», non «non raggiungibile» (F8, F9).
**Caso delimitato (mossa 8):** progetto **senza topologia configurata**, nodo nuovo di fabbrica. È il caso in cui il PLC non
dà il nome da solo (F11). La sostituzione automatica (F11-F14) non si dice a voce: va nella descrizione / messaggio del canale.

## 3 · Il parlato
Voce: il PLC con la faccia (prima persona, in panico all'inizio). Mister Automation è in scena ma non parla (una sola voce per clip).

| Scena | Clip | Battuta | Fatti |
|---|---:|---|---|
| S1 | 6 s | «Ho perso un nodo! Il tecnico l'ha cambiato con uno nuovo, identico. Non lo trovo.» | F5 (nodo perso = guasto stazione), F2, F4 |
| S2 | 8 s | «Lui pensa: stesso modello, stesso IP, deve andare. Ma l'IP glielo do io. Io il nodo lo cerco per nome.» | errore plausibile 1; F3 |
| S3 | 8 s | «All'avvio cerco ogni nodo del mio progetto col suo nome. E uno nuovo di fabbrica un nome non ce l'ha.» | F4, F2 (F1 sotto: senza nome niente dati) |
| S4 | 8 s | «Eppure il LED della porta è verde! È guasto anche lui? No: quel verde dice solo che il cavo c'è.» | errore plausibile 2; F9 |
| S5 | 6 s | «Sul PC leggi "pronto per l'assegnazione", non "non raggiungibile". Gli manca solo il nome.» | F8, F10 |
| S6 | 8 s | «Il tecnico lo sceglie dal MAC, lo fa lampeggiare e gli dà il nome del mio progetto. Eccolo! Lo ritrovo.» | F6, F7, F16, F3 |
| S7 | 10 s | «Stesso modello non basta: serve lo stesso nome. Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.» | F16, F1 · CTA corsi/webinar + tagline |

Legami fra battute: S1→S2 MA (perché non lo trova?) · S2→S3 QUINDI · S3→S4 MA (eppure il LED…) · S4→S5 QUINDI (come lo
distingui) · S5→S6 QUINDI · S6→S7 QUINDI. Gancio («Ho perso un nodo») chiuso in S6 («Lo ritrovo»).

## 4 · Piano scena per scena (corto)
**Mondo IBRIDO**: fabbrica vera + ologrammi mai toccati (cartellini di luce col nome sopra ogni nodo, impulsi lungo i cavi).
**Set** (SET-TIPO §1 imbottigliamento + §0-bis): quadro di bordo linea a parete, lato manutenzione, sportello aperto verso il
corridoio. In basso su guida DIN: il PLC con la faccia, lo switch, la fila dei nodi di I/O; il nodo nuovo all'estremità, cavo
RJ45 dallo switch inserito ai due capi. Accanto, a 1 m, carrello col portatile collegato allo switch. Dietro: nastro con
bottiglie ferme, beacon in cima alla riempitrice. ⛔ Non c'è: robot, nodi sul campo, marchi, codici diagnostici.

| Scena | Cosa si vede | Stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | Quadro aperto, PLC in primo piano, Mister Automation davanti al quadro | nastro fermo, beacon rosso; cartellini olografici accesi sui nodi, quello nuovo vuoto | PLC sgrana gli occhi su «perso» |
| S2 | PLC stretto, Mister Automation sicuro in secondo piano | come S1; ologramma «IP» sopra il nodo nuovo che si spegne | PLC scuote la testa su «Ma» |
| S3 | Impulsi di luce dal PLC lungo i cavi, i cartellini si accendono uno a uno; al nodo nuovo l'impulso torna indietro | nastro fermo | PLC guarda il nodo nuovo su «non ce l'ha» |
| S4 | Primo piano del nodo nuovo, PLC a lato | LED di link della porta verde fisso | Mister Automation sfiora il connettore su «cavo» |
| S5 | Carrello col portatile; tabella generica senza marchi, riga «pronto per l'assegnazione» | LED verde, nastro fermo | PLC indica lo schermo su «nome» |
| S6 | Mister Automation al portatile; il nodo nuovo | LED di link che lampeggia, poi il cartellino olografico si riempie col nome | PLC sorride su «Eccolo!» |
| S7 | Quadro intero, linea dietro | beacon verde, nastro in moto, persone fuori dalle parti in moto | PLC rilassato, pollice di Mister Automation su «stesso nome» |

## Deviazioni (con motivo)
- Nessuna sul mestiere: 7 scene, 54 s, una voce per clip, battute ≤ 20 parole.
- Il tecnico in scena è nominato «il tecnico» (non «Mister Automation»): la voce è del PLC e il nome lungo non entra nelle clip da 8 s.
- Lettore fresco (Aqua Regia) **non lanciato**: il giro di prova vietava i subagenti. Controllo da fare prima di consegnare a Saverio.
- Visivo non coperto dalla scheda: beacon rosso/verde e nastro fermo/in moto sono scelte di scena, non affermazioni del
  parlato (il blocco della linea per guasto stazione è «non confermato» nella scheda). Le spie del nodo oltre il LED di link
  non si mostrano (non confermato).

## Esito dei controlli
- **Verità:** ogni affermazione del parlato rimanda a un F della scheda (colonna Fatti). Non usati: F11-F15 (scelta del caso), «non confermato».
- **Tempo** (`timing.py caso-02_giro3_parlato.txt --voce lipsync --precedente 52`): clip 6+8+8+8+6+8+10 = **54 s** di montato,
  nessuna scena oltre i 10 s, **🟢 VERDE**, 83 crediti su 7 clip. Spia: 2 s dal reel precedente (52 s), meglio ≥ 4 s ma non blocca.
- **Lettore fresco:** non eseguito (vedi Deviazioni).
