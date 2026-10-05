# Caso 01 · «Sensore induttivo o capacitivo: quale scegliere per rilevare il pezzo?» · passo 3 · giro del 5/10

Scritto da Vessel (prima versione, nessun giro di revisione) dalla copia PROVA, con la scheda `caso-01_fatti.md`.
Quaderno letto: 0 voci, nessun contatore da aggiornare.

## 1 · Filo

**Filo:** il materiale del pezzo decide il sensore *e* la distanza: l'induttivo vede solo il metallo, e se è uno standard la
sua distanza dichiarata vale per l'acciaio (sull'alluminio meno della metà); l'acqua dietro al vetro la vede il capacitivo,
perché ha una permittività molto più alta del vetro.

**Errore plausibile di chi guarda:** il pezzo di alluminio passa e il LED dell'induttivo resta spento → «l'induttivo
l'alluminio non lo vede, ci vuole il capacitivo». Invece lo vede, ma più vicino: la distanza di intervento dichiarata vale
per l'acciaio, sull'alluminio è 0,35-0,45 volte (F1).

**Durata obiettivo: 52-56 s.** Motivo: un caso col percorso completo (prova ok con la chiave, prova ko col pezzo, dubbio,
correzione che si vede) più il secondo materiale, che serve a chiudere la domanda del titolo («induttivo *o* capacitivo»):
sta nella parte alta della fascia 48-56, senza un'idea in più.

## 2 · Il discorso

B1. Questo pezzo passa sul nastro, e il PLC deve saperlo senza toccarlo. Induttivo o capacitivo?
B2. È metallo, quindi induttivo: fa un campo magnetico. Ci passo una chiave d'acciaio, ne assorbe energia, e lui si accende.
B3. Ma passa il pezzo… spento. È alluminio. Allora non lo vede: ci vuole il capacitivo?
B4. No: lo vede, ma più vicino. Su un induttivo standard, la distanza di intervento dichiarata vale per l'acciaio. Sull'alluminio è meno della metà.
B5. Quindi non lo cambio: lo avvicino. Stesso pezzo… acceso.
B6. In lavatrice serve il livello dell'acqua, e l'acqua non è metallo: quindi capacitivo. La sente attraverso questo vetro: ha una permittività molto più alta.
B7. Prima il materiale, poi sensore e distanza. Vuoi impararlo? Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

Legami (MA / QUINDI): B1→B2 quindi (è metallo) · B2→B3 ma (il pezzo non lo accende) · B3→B4 ma (il dubbio è sbagliato:
«non lo vede» → «lo vede») · B4→B5 quindi · B5→B6 ma (dove non c'è metallo l'induttivo non basta) · B6→B7 quindi (sintesi).

## 3 · Il taglio

| Battuta | Clip | Parole |
|---|---:|---:|
| B1 → S1 | 6 s | 15 |
| B2 → S2 | 8 s | 20 |
| B3 → S3 | 6 s | 15 |
| B4 → S4 | 10 s | 23 |
| B5 → S5 | 4 s | 9 |
| B6 → S6 | 10 s | 24 |
| B7 → S7 (CTA) | 10 s | 19 (+2 s CTA) |

Una battuta per clip, nessuna divisa. Ridondanze tolte prima del taglio (il discorso di partenza era ~66 s su 8 scene):
- la scena-ponte «Il pezzo va in lavatrice…» è entrata in B6 (il passaggio di set lo mostra il fondo di S5/inizio S6);
- in B6 i valori 5 e 80 sono diventati «molto più alta» (i numeri restano nella scheda e vanno in descrizione);
- la regolazione della sensibilità del capacitivo (F3) è uscita dal parlato: è un'idea in più, non la scelta del sensore;
- in B5 «Passa il pezzo» → «Stesso pezzo», perché la correzione avviene a nastro fermo col pezzo davanti (vedi piano).

## 4 · Piano scena per scena (forma corta)

**Mondo:** REALE. Una linea di pezzi in alluminio: nastro trasportatore che scarica in una lavatrice industriale a vasca.
**Set A** – sponda del nastro, induttivo su staffa asolata fissata alla sponda, faccia verso il passaggio del pezzo, cavo
nella canalina. **Set B** – fianco della lavatrice, vasca con finestra di vetro, capacitivo montato all'esterno del vetro
all'altezza del livello da rilevare. Altezze e lato esatti: da verificare su SET-TIPO (la scheda non li ha). Colore dei LED:
non confermato, si scrive solo acceso/spento. Mister Automation sempre fuori dalle parti in moto.

| Scena | Set | Cosa si vede | Stato dell'impianto | Gesto ↔ parola |
|---|---|---|---|---|
| S1 | A, mezza figura | M.A. accanto al nastro, un pezzo di alluminio passa davanti alla staffa | nastro in marcia; LED induttivo spento | indica il pezzo senza toccarlo ↔ «senza toccarlo» |
| S2 | A, mani da vicino | M.A. tiene una chiave d'acciaio davanti alla faccia del sensore | nastro fermo; LED si accende quando entra la chiave | passa la chiave ↔ «ci passo» |
| S3 | A, primo piano radente sul LED | il pezzo di alluminio passa davanti alla faccia | nastro in marcia; LED resta spento | M.A. guarda il LED e alza un sopracciglio ↔ «spento» |
| S4 | A, mezza figura | nastro fermo, un pezzo di alluminio fermo davanti al sensore, lo spazio fra faccia e pezzo ben visibile | nastro fermo; LED spento | indica lo spazio fra faccia e pezzo ↔ «più vicino» |
| S5 | A, mani da vicino (stesso asse di S4) | M.A. fa scorrere il sensore lungo l'asola verso il pezzo | nastro fermo; LED si accende quando arriva vicino | fa scorrere il sensore ↔ «lo avvicino» |
| S6 | B, primo piano di lato | finestra della vasca, acqua al livello del sensore, capacitivo sul vetro | lavatrice in marcia; LED capacitivo acceso | sfiora il vetro accanto al sensore ↔ «attraverso questo vetro» |
| S7 | B, campo largo | il nastro scarica il pezzo nella lavatrice; entrambi i sensori in vista; scritta SENSORE in post | linea in marcia; LED induttivo e capacitivo accesi | M.A. si gira verso camera ↔ «Commenta SENSORE» |

Fra S5 e S6 c'è il taglio di set; la causa che si vede: in S5 il nastro è la stessa linea che finisce nella lavatrice (sullo
sfondo della mezza figura di S4 si vede l'ingresso della vasca).

## 5 · Verità battuta per battuta

| Battuta | Affermazione | Fatto | Limite detto a voce |
|---|---|---|---|
| B1 | rilevare il pezzo senza contatto, induttivo o capacitivo | F2, F3 (sensori di prossimità: campo davanti alla faccia) | — |
| B2 | metallo → induttivo; campo magnetico; il metallo ne assorbe energia e l'uscita commuta | F2 | «solo metalli» arriva per contrasto in B6 («non è metallo: quindi capacitivo») |
| B3 | l'alluminio a quella distanza non lo fa commutare | F1 (conseguenza) | — (è il dubbio, viene corretto in B4) |
| B4 | lo vede; distanza dichiarata riferita all'acciaio; sull'alluminio meno della metà | F1 | «su un induttivo standard» (esclude i modelli a fattore 1) |
| B5 | avvicinato, commuta | F1 (conseguenza) | «stesso pezzo» |
| B6 | acqua non è metallo → capacitivo; rileva attraverso il vetro perché la permittività dell'acqua è molto più alta | F2 (solo metalli), F3, F4 (vetro ~5, acqua ~80) | «questo vetro» (dipende da spessore e materiale della parete e dal modello) |
| B7 | sintesi: materiale → sensore e distanza | F1, F2, F3 | — |

Non usati: F5 (non confermato) · colore del LED (non confermato) · regolazione della sensibilità di F3 · «il capacitivo rileva
anche i metalli» di F4 (non detto e non contraddetto: il «No» di B4 risponde a «ci vuole», non a «funzionerebbe»).
Eccezione di F1 non detta come eccezione: i modelli a fattore 1. Basta delimitare «standard»: chi ha un fattore 1 e lo
avvicina non decide male.

## Deviazioni
- **S4 e S6 hanno 23 e 24 parole in 10 s** (il mestiere dice ~22): stanno nella clip secondo `timing.py`, ma vanno lette
  nel tono; se Flow le stringe, in B6 si toglie «questo» prima di tagliare un'idea.
- **S1, S2, S3 sono esattamente al bordo della clip** (6,0 · 8,0 · 6,0 s): il conto dice che entrano, una consegna più lenta no.
  Lo segnalo, non lo correggo (prima versione).
- **Stato del nastro che cambia fra le scene** (marcia S1 → fermo S2 → marcia S3 → fermo S4-S5 → marcia S6-S7): serve alla
  sicurezza (la mano col sensore e la chiave lavora a nastro fermo) e ogni cambio sta su un taglio, mai dentro una clip.

## Uscita del timing
`python3 …/prova-2026-10-05/vessel/scripts/timing.py caso-01_parlato.txt --voce lipsync --obiettivo 52-56`

```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      15    2.5    6.0     6       10
   S2      20    2.5    8.0     8       12
   S3      15    2.5    6.0     6       10
   S4      23    2.5    9.2    10       15
   S5       9    2.5    3.6     4        7
   S6      24    2.5    9.6    10       15
   S7      19    2.5    7.6    10       15  (+2 s CTA)
  TOT     125                  54       84

─── DURATA ───
somma delle clip: 54 s + asset riusabili 0 s = 54 s di montato
controllo veloce (parole ÷ 2.0): 62 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 21 · sotto le 6 parole: 10 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 52-56 s (avviso, non blocca) ───
  ✅ 54 s, dentro l'obiettivo

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 84 crediti su 7 clip
```
Nota: il controllo veloce (62 s) si scosta di 8 s dalla somma delle clip; ricontato a mano, le parole per scena sono giuste.
Lo scarto c'è perché quasi tutte le clip sono piene fino al bordo (125 parole ÷ 2,5 = 50 s di voce in 54 s di clip): il
montato a 2,0 parole/s presume più respiro di quello che queste clip hanno. È lo stesso rischio di S1-S3 al bordo.

Controlli non fatti da me (come da consegna del giro): lettore fresco e controllo dei limiti.
