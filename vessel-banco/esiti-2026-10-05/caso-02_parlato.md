# Caso 02 · «Ho perso un nodo. Tutta la rete lo sta cercando» · passo 3 · Vessel (giro di prova 5/10)

Slot lunedì 18:30 → componente con la faccia in panico: parla **il PLC** (la CPU con la faccia), al tu, a chi ha montato il
ricambio. Mister Automation è in scena e fa i gesti, non parla. Keyword NOME. Fonte unica: `esiti-2026-10-04/caso-02_fatti.md`.

## 1 · Filo, errore, durata
**Filo:** il PLC un nodo PROFINET lo riconosce dal **nome**, non dall'IP (l'IP glielo dà lui, dopo); un ricambio nuovo di
fabbrica nasce senza nome, quindi se il PLC non glielo ridà da solo, il nome glielo dai tu dal PC: quello del progetto.

**Errore plausibile** (scheda, errori 1 e 2): «il nodo è identico e l'IP gliel'ho messo uguale: deve funzionare» e, quando non
va, «allora è guasto anche il ricambio». L'errore 3 della scheda (allargare il filo a «senza nome non viene mai trovato») è
tenuto fuori: S4 dice «se non glielo do io da solo».

**Durata obiettivo: 52-58 s.** Motivo: un caso solo, ma **due** errori plausibili da chiudere a voce, perché portano a due
decisioni sbagliate diverse (ordinare un altro ricambio · insistere sull'IP); più la correzione col gesto pratico.

## 2 · Il discorso (scritto di fila)
- **B1** Ho perso un nodo! L'hanno sostituito con uno identico. Lo cerco su tutta la rete… e non risponde.
- **B2** «È guasto anche il nuovo?» No. Il PC non dice «non raggiungibile», dice «pronto per l'assegnazione»: il MAC c'è, il nome no.
- **B3** «Il nome? Ma l'IP gliel'ho messo uguale!» Non basta: io i nodi li riconosco dal nome. L'IP glielo do io, dopo.
- **B4** Ma nuovo di fabbrica, il nome non ce l'ha. Se non glielo do io da solo, glielo dai tu.
- **B5** Lo scegli dal MAC, fai lampeggiare il suo LED per sicurezza, e gli assegni il nome che ha nel progetto.
- **B6** Eccolo! Lo riconosco e gli do l'IP. Prima il nome, poi l'IP.
- **B7** Vuoi imparare le reti? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

Controllo MA/QUINDI: B1→B2 *quindi* (non risponde → guasto?) · B2→B3 *ma* (riprende «il nome») · B3→B4 *ma* (lo riconosco dal
nome, ma il nuovo non ce l'ha) · B4→B5 *quindi* (glielo dai tu: ecco come) · B5→B6 *quindi* · B6→B7 chiusa + CTA.
Il dubbio di chi guarda entra due volte dove nasce l'errore (B2 «guasto», B3 «l'IP»), e la risposta riprende la parola
(«il nome no» → «Il nome?»; «l'IP» → «L'IP glielo do io»).

## 3 · Il taglio
| Battuta | Clip | Parole | Nota |
|---|---:|---:|---|
| B1 → S1 | 8 s | 18 | |
| B2 → S2 | 10 s | 22 | |
| B3 → S3 | 10 s | 21 | |
| B4 → S4 | 8 s | 19 | |
| B5 → S5 | 8 s | 20 | |
| B6 → S6 | 6 s | 12 | |
| B7 → S7 | 8 s | 14 | CTA (+2 s) |
Una battuta per clip, nessuna da dividere. Ridondanze tolte per stare nell'obiettivo (prima misura 60 s): «nuovo di fabbrica»
detto due volte (resta solo in B4, B1 dice «identico»); nella CTA «come ragiona una rete» → «le reti». Tolta come idea
intera, già nella prima stesura: la frase su topologia/«mappa delle porte» (vedi Deviazioni).

## 4 · Il piano scena per scena (forma corta)
**Mondo:** IBRIDO — quadro vero + ologrammi mai toccati (onde di ricerca, etichette coi nomi sopra i nodi).
**Set (uno solo):** quadro elettrico a bordo linea, lato manutenzione, sportello aperto. In alto nella zona logica il PLC con
la faccia su guida DIN; **in basso**, sulla stessa guida, switch e tre nodi di I/O identici collegati con cavo di rete RJ45
(connessi ai due capi). Il terzo è il ricambio, appena montato, cavo nella sua porta. Davanti al quadro Mister Automation col
portatile sul carrello, cavo di rete dal portatile allo switch. Linea ferma per tutto il reel (beacon rosso): nessuna parte in moto.
| S | Si vede | Stato | Gesto (parola) |
|---|---|---|---|
| S1 | PLC in panico; onde olografiche scendono dal PLC lungo i cavi verso i nodi; due nodi hanno sopra un'etichetta olografica col nome, il terzo niente | LED di link verdi su tutte le porte; beacon rosso | onde che partono su «cerco» |
| S2 | Mister Automation apre il portatile; sullo schermo (senza marchi) la riga del nodo: «pronto per l'assegnazione», MAC sì, nome vuoto | come S1 | il PLC scuote la testa su «No» |
| S3 | ologramma «IP» sopra il nodo nuovo; il PLC indica le etichette-nome sopra gli altri due | come S1 | il PLC indica su «nome» |
| S4 | primo piano sul nodo nuovo: il posto dell'etichetta olografica è vuoto | LED di link verde | il PLC allarga le braccia/guarda il tecnico su «tu» |
| S5 | dita sul touchpad; sul nodo nuovo il LED di link lampeggia | LED che lampeggia | lampeggio su «lampeggiare» |
| S6 | compare l'etichetta-nome sopra il nodo, poi l'IP; pacchetti di dati olografici corrono sul cavo; il PLC tira il fiato | LED di link verde fisso; beacon ancora rosso (la ripartenza la decide l'operatore) | sospiro su «Eccolo!» |
| S7 | PLC calmo, ammicca in camera; keyword NOME a schermo, firma | come S6 | ammiccare su «NOME» |

## 5 · Verità battuta per battuta
| S | Affermazione | Fatto |
|---|---|---|
| S1 | il PLC cerca il nodo sulla rete e non lo trova («perso») | F4 (cerca i dispositivi configurati, col nome) · F5 (guasto stazione = nodo perso) · F1 (senza nome non scambia dati) |
| S2 | dal PC: «non raggiungibile» vs «pronto per l'assegnazione» = MAC presente, nome assente | F8 · F10 (stato letto dal PC, senza il controller) · F9 per il LED verde che si vede (dice solo «cavo») |
| S3 | il PLC riconosce i nodi dal nome; l'IP lo assegna lui | F3 |
| S4 | nuovo di fabbrica = senza nome; il PLC a volte lo ridà da solo, se no lo dai tu | F2 · F11 (esiste, con condizioni) · F12 |
| S5 | scelto per MAC, LED che lampeggia per riconoscerlo, nome del progetto | F6 · F7 · F16 |
| S6 | riconosciuto dal nome, poi l'IP | F3 · F6 |
| S7 | CTA | — |
Limiti arrivati a voce: «nuovo di fabbrica» (F2: un ricambio usato può avere un nome vecchio) · «se non glielo do io da solo»
(F11: il filo vale solo quando il PLC non lo nomina). Limiti **non** detti, con il perché (regola 8: non cambiano la decisione
davanti al nodo): F8 sono gli stati di un software preciso (altri costruttori non verificati) → il parlato dice «il PC»;
F3 alcuni dispositivi prendono l'IP via DHCP; condizioni di F11 (topologia porta per porta, supporto, funzione attiva) e
F13 (porta sbagliata = nome sbagliato) → descrizione/canale. Da guardare nel controllo dei limiti: **S2** (stati di un
solo software detti come generali) e **S4** («se non glielo do io da solo» senza dire quando).
Nessun fatto usato fuori scheda; nessun «non confermato» usato (le spie del nodo senza nome non compaiono: si vede solo il LED di link, F9).

## Deviazioni
- **Durata 52-58 s** invece di 48-56: due errori plausibili da chiudere entrambi (motivo in §1). Montato 58 s.
- **Topologia non spiegata a voce.** Nella prima stesura c'era «senza la topologia nel progetto, da solo non posso darglielo»:
  tolta per stare nel tempo, perché non cambia cosa fa il tecnico (il gesto resta: se il PLC non l'ha nominato, lo nomini tu).
  Il caso è delimitato con «se non glielo do io da solo».
- **Processo:** ho fatto un grep su `scripts/timing.py` della copia per capire perché la CTA risultava oltre i 10 s (aggiunge
  2 s alla scena finale). Tre misure col timing, sullo stesso testo che si accorciava: non sono giri di revisione del tono.
- Controlli lettore fresco e limiti non lanciati (li fa chi ha lanciato il giro).

## Uscita del timing
```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      18    2.5    7.2     8       12
   S2      22    2.5    8.8    10       15
   S3      21    2.5    8.4    10       15
   S4      19    2.5    7.6     8       12
   S5      20    2.5    8.0     8       12
   S6      12    2.5    4.8     6       10
   S7      14    2.5    5.6     8       12  (+2 s CTA)
  TOT     126                  58       88

─── DURATA ───
somma delle clip: 58 s + asset riusabili 0 s = 58 s di montato
controllo veloce (parole ÷ 2.0): 63 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 19 · sotto le 6 parole: 10 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 52-58 s (avviso, non blocca) ───
  ✅ 58 s, dentro l'obiettivo

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 88 crediti su 7 clip
```
(Misure precedenti: 1ª stesura con obiettivo 48-56 → ROSSO, CTA oltre 10 s; 2ª → 60 s, fuori obiettivo.)
