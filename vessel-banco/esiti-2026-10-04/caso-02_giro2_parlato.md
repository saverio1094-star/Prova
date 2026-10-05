# Caso 02 · giro 2 · «Ho perso un nodo. Tutta la rete lo sta cercando» · storia e parlato
Vessel, 4/10/2026 · slot lunedì 18:30 (componente con la faccia, in guasto) · keyword NOME · fonte unica: `caso-02_fatti.md` (Granite)
Copione per il timing: `caso-02_giro2_parlato.txt`

## 1 · Filo ed errore plausibile
**Filo:** il PLC un nodo PROFINET lo riconosce dal nome, non dall'IP né dal LED verde; un ricambio nuovo di fabbrica il nome
non ce l'ha, e se il PLC non può darglielo da solo (niente topologia nel progetto) glielo dai tu dal PC.
**Errore plausibile** (scheda, errori 1 e 2): «il nodo nuovo è identico, il LED è verde, l'IP lo metto io: deve andare; se non
va, è rotto anche il ricambio». **Il limite che lo tiene stretto** (errore 3): con la topologia configurata e un nodo che lo
supporta il PLC il nome lo ridà da solo → il parlato lo dice in S4 e poi chiude il caso («Qui no»).

## 3 · Parlato
Voce unica: il PLC con la faccia (prima persona, al tu), lip-sync. Mister Automation è in scena e non parla.

| Scena | Clip | Battuta | Fatti |
|---|---:|---|---|
| S1 | 6 s | «Ho perso un nodo! Non mi arrivano più i suoi dati: guasto stazione.» | F5 + Termini («guasto stazione» = il controller non riceve più i dati) |
| S2 | 8 s | «Il tecnico l'ha cambiato con uno identico, e la porta ha il LED verde. Quindi lo ritrovo… No. Cosa manca?» | F9 (LED verde = connessione) · premessa di storia: ricambio identico |
| S3 | 8 s | «Manca il nome. Quel verde dice solo che il cavo c'è: io un nodo lo riconosco dal nome, non dall'IP.» | F9 + suo limite («dice se c'è il cavo, non se c'è il nome») · F3 · F1 |
| S4 | 10 s | «E uno nuovo di fabbrica il nome non ce l'ha. Con certi nodi glielo do io, se nel progetto c'è la topologia. Qui no.» | F2 · F11 («certi nodi» = il dispositivo deve supportarlo) · F12 implicito |
| S5 | 10 s | «Allora tocca a te. Il PC lo vede pronto per l'assegnazione: c'è, gli manca solo il nome. Lo scegli dal MAC e glielo dai.» | F8 · F6 · F10 (letto dal PC) |
| S6 | 6 s | «Eccolo! Lo riconosco dal nome e l'IP glielo do io. Nodo nuovo? Prima il nome.» | F6 («poi il controller lo riconosce dal nome e gli dà l'IP») · F3 · F1 |
| S7 | 8 s | «Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.» | CTA (LIBRERIA-CTA, forma dell'esempio 01) + tagline |

Le mosse: S2 prova che dovrebbe andare e non va → dubbio di chi guarda alla fine di S2 («Cosa manca?», il LED verde è
l'«eppure») → S3 risponde riprendendo la parola («Manca il nome») → S4 il perché + il limite onesto → S5 il gesto del tecnico
→ S6 effetto visibile e sintesi in tre parole («Prima il nome»). Fra le battute ci sta sempre MA o QUINDI.

## 4 · Piano scena per scena (corto)
**Mondo IBRIDO**: reparto di oggi, quadro elettrico di bordo linea sul lato manutenzione, sportello aperto verso il corridoio
(SET-TIPO §0, §0-bis). Un set solo: davanti al quadro aperto, con un carrello e il portatile accanto. Ologrammi sovrapposti, mai
toccati: le linee di rete fra PLC e nodi e, sopra ogni nodo, un cartellino col suo nome.
**Componenti:** PLC (con la faccia, logo MA) e moduli I/O su guida DIN **in basso**, zona logica; il nodo nuovo è **già montato**
sulla guida, cavo di rete RJ45 connesso ai due capi (switch/PLC → nodo). Inquadrare del nodo solo le porte coi LED di link;
le altre spie del nodo fuori inquadratura (come appaiono senza nome è non confermato). Nessuna spia della CPU in primo piano
(il suo stato col guasto stazione non è confermato). Linea ferma, niente in moto fino a S6.

| Scena | Cosa si vede · stato | Gesto legato alla parola |
|---|---|---|
| S1 | Primo piano del PLC in panico; ologramma della rete con una linea interrotta verso un nodo | il PLC si guarda attorno su «perso» |
| S2 | Il nodo nuovo al suo posto sulla guida; LED di link **verde** sulla porta; ologramma: il PLC «cerca» lungo la linea e torna indietro vuoto | Mister Automation sfiora il connettore RJ45 su «identico»; il PLC si gela su «No» |
| S3 | Dettaglio della porta col LED verde; sopra gli altri nodi il cartellino col nome, sopra il nuovo il cartellino è **vuoto** | il PLC indica il cartellino vuoto su «nome» |
| S4 | Ologramma della mappa porta per porta che si accende tratteggiata e si spegne su «Qui no» | il PLC scuote la testa su «Qui no» |
| S5 | Mister Automation al portatile sul carrello, cavo verso lo switch; a schermo una tabella senza marchi con la riga «pronto per l'assegnazione»; il LED di link del nodo **lampeggia** (comando dal PC, F7) | preme il tasto su «glielo dai» |
| S6 | Il cartellino sopra il nodo si riempie col nome; la linea olografica si chiude e i dati scorrono verso il PLC; la linea riparte | il PLC sorride su «Eccolo» |
| S7 | Il PLC verso camera, il quadro alle spalle; parola NOME in ologramma | — |

## Deviazioni dal mestiere (con motivo)
- **S4 e S5 a 24 parole in 10 s** (il consiglio dice ~22): S4 porta il limite dell'errore 3 (topologia), S5 la procedura;
  togliendo parole si perdono i verbi o la condizione. timing.py le misura 9,6 s: entrano, senza margine.
- **56 s, al bordo alto della fascia**: era la via per avere 4 s di distanza dai 52 s del reel prima senza tagliare il
  limite di S4 (a 48 s non entrava con frasi intere).
- **Il dubbio di chi guarda lo dice il PLC** («Cosa manca?»), non il tecnico: una sola voce per tutto il reel.
- **Il titolo non si ripete a voce**: «tutta la rete lo sta cercando» non è nella scheda (F4 dice solo che il controller cerca
  i dispositivi configurati, all'avvio). Il parlato apre su «Ho perso un nodo» e sul guasto stazione.
- **«Pronto per l'assegnazione»** è il nome dello stato nel software di un costruttore (limite di F8): detto senza marchio.
- **F7 (far lampeggiare il LED) è solo nell'immagine**, non nel parlato: non entrava in S5.

## Esito dei controlli
- **Verità**: ogni affermazione ha il suo F (colonna Fatti). Nessun «non confermato» usato. Premessa di storia («l'ha cambiato con
  uno identico», «Qui no» = topologia assente in questo impianto) dichiarata come scelta, non come fatto.
- **Tempo** (`timing.py caso-02_giro2_parlato.txt --voce lipsync --precedente 52`): 🟢 VERDE · clip 6+8+8+10+10+6+8 = **56 s**
  di montato (CTA +2 s compresa) · nessuna scena oltre 10 s · 4 s dai 52 s del reel prima · 86 crediti su 7 clip.
  Note: S2 e S3 a 8,0 s e S4-S5 a 9,6 s, tutte al limite della loro clip; il controllo veloce (parole ÷ 2) dà 64 s.
- **Lettore fresco**: non lanciato (in questo giro niente subagenti).
