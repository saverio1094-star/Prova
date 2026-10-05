# Caso 03 · «Stanotte questa linea si è fermata tre volte. E io so a che ora.» · passo 3 · Vessel · 2026-10-05b
Slot lunedì 18:30 → componente con la faccia (il PLC parla in prima persona, lip-sync). Keyword DIAGNOSI.
Input: `casi/caso-03_web-server.md` + `esiti-2026-10-04/caso-03_fatti.md`. Quaderno: vuoto (0/10), nessuna voce da applicare.

## 1 · Prima della prima battuta
**Cosa deve saper distinguere chi guarda:** la riga in cima al buffer di diagnostica **non è per forza la prima cosa successa**:
per trovare la prima fermata si legge la colonna dell'ora, non la posizione. E quell'ora è l'ora del PLC, giusta solo se il suo orologio è regolato.

**Il caso preciso:** un PLC che stanotte è **andato in STOP tre volte** (tre voci di passaggio a STOP), letto la mattina dal
browser del portatile collegato alla rete del quadro, con il web server già attivato.

**L'indispensabile** (4 pezzi):
| # | Pezzo | Errore che evita | Fatti |
|---|---|---|---|
| P1 | Ogni volta che la CPU va in STOP scrive una riga nel buffer di diagnostica, con data e ora | ricostruire la notte a memoria del turno; e (caso nominato «vado in STOP») cercare lì fermate in cui la CPU è rimasta in RUN | F1, F2 |
| P2 | Il buffer si legge dal browser con l'IP della CPU, ma solo se il web server è stato attivato prima col software (di fabbrica è spento) | errore 4 «basta il browser» | F5, F7, F8 |
| P3 | La riga in cima può essere l'ultima cosa successa: si legge l'ora, non la posizione | errore 1 «la prima riga è l'origine» | F3, F6, F1 |
| P4 | L'ora è quella del PLC: vale se l'orologio è regolato; senza cookie la pagina mostra l'UTC | errore 3 «l'ora sulla riga è l'ora a muro» — ed è il limite della promessa del titolo («so a che ora») | F9, F10 |

**Durata obiettivo: 54-60 s.** Motivo: gancio 6 s + quattro pezzi, due dei quali portano con sé il loro limite (web server
spento, orologio/UTC) + dubbio di chi guarda + CTA 10 s. Quattro pezzi con limite non stanno in 48-56: vedi § Deviazioni.

**La chiusura che il contenuto autorizza:** «la prima fermata ha l'ora più vecchia» e «l'ora, non la posizione». **Non** «ecco la
causa»: nessuna fonte dà una regola per riconoscere la causa, né dice che la voce di STOP contenga il motivo (scheda, Non confermato).

## 2 · Il discorso
B1 Stanotte questa linea si è fermata tre volte. E io so a che ora.
B2 Sono il PLC. Ogni volta che vado in STOP, lo scrivo nel mio buffer di diagnostica, con data e ora.
B3 Per leggermi apri il browser e scrivi il mio indirizzo IP. Ma di fabbrica il mio web server è spento: va attivato prima, dal software.
B4 Ecco le mie tre righe di STOP. Quella in cima è la prima fermata, no?
B5 Non per forza: in cima può esserci l'ultima. Leggi l'ora, non la posizione: la prima fermata ha l'ora più vecchia.
B6 Ma l'ora è la mia: vale se il mio orologio è regolato. E senza cookie la pagina ti mostra l'UTC, non l'ora del PLC.
B7 L'ora, non la posizione. Vuoi imparare la diagnostica? Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.

Catena MA/QUINDI: B1 →(come lo sai?) B2 →QUINDI come lo leggo B3 (MA spento) →QUINDI, attivo, ecco le righe B4 →MA no B5 →MA l'ora è la mia B6 →QUINDI sintesi B7.

## 3 · Il taglio
| Battuta | Scena | Clip |
|---|---|---:|
| B1 | S1 | 6 s |
| B2 | S2 | 8 s |
| B3 | S3 | 10 s |
| B4 | S4 | 6 s |
| B5 | S5 | 8 s |
| B6 | S6 | 10 s |
| B7 | S7 | 10 s (CTA) |

Una battuta per clip, nessuna divisa. Ridondanze tolte nella stesura per far stare le battute in 10 s:
- B3: tolto «Il software di programmazione non ti serve» (era la metà che poi il limite smentiva a metà: «serve prima»); l'attivazione dice già che il software serve una volta, prima.
- B5: «l'ultima cosa successa» → «l'ultima» (la parola «fermata» è appena detta in B4).
- B7: «Vuoi imparare a leggere la diagnostica?» → «Vuoi imparare la diagnostica?» (la CTA andava a 10,4 s).

## 4 · Note battuta per battuta
| | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | il gancio: apre «come fa a saperlo?» | F1, F2 | «…e nessuno sa perché»: promette la causa, che il buffer da solo non dà (Non confermato) |
| B2 | risponde «come lo sai?»: nomina il caso (STOP) prima della regola, dà il termine vero | F1, F2 | «Ogni volta che la linea si ferma, lo scrivo»: falso per le fermate gestite dal programma con la CPU in RUN (limite F2) · «con data, ora e il motivo»: che la voce di STOP contenga il motivo non è confermato |
| B3 | risponde «e come ti leggo?» e mette subito il limite intero (quando vale + cosa fare) | F5, F7, F8 | «Ti basta il browser, niente software»: è l'errore 4 · il permesso utente «leggere la diagnostica» detto a voce: si imposta nella stessa configurazione, una volta, da chi attiva il web server (limite F7), quindi non cambia il gesto di chi guarda (far attivare dal software) e costava 4 s · VPN da fuori rete (F8): nel caso mostrato si è nel quadro |
| B4 | il dubbio di chi guarda, detto con le sue parole, dove nasce l'errore 1 | F2, F3 | «Quella in cima è la causa, no?»: porterebbe a chiudere su come si trova la causa, che le fonti non danno |
| B5 | la risposta riprende la parola («prima» → «l'ultima») e dà la regola che regge sempre | F3, F6, F1 | «Nella pagina in cima c'è sempre la più recente»: per la pagina web l'ordine non è scritto in nessuna fonte (F6); per questo «può esserci» e la regola sull'ora |
| B6 | mantiene onesta la promessa del titolo: l'ora è vera a una condizione, detta intera | F9, F10 | «Su UTC sei un'ora indietro d'inverno e due d'estate»: conto di Granite, non nelle fonti · fuso orario del PC che imposta l'orologio (F9): riguarda chi imposta, non chi legge; «regolato» copre il gesto |
| B7 | sintesi in quattro parole, poi una sola CTA e la tagline | — | «Salvale in csv e mandale all'ufficio tecnico» (F12): gesto utile ma fuori dall'indispensabile |

Fatti lasciati nella scheda (descrizione o canale), e perché non cambiano la decisione nel caso mostrato:
- **F4, buffer con numero massimo di voci / a CPU spenta ne resta una parte:** in una notte con tre STOP le voci ci sono; conta con molti eventi o se il quadro è stato spento. Nessun numero, perché in scena c'è «un PLC» senza modello.
- **F11, esempio di causa (tempo di ciclo):** aprirebbe il discorso sulla causa, che è un altro reel.
- **F13, LED RUN/STOP:** usato solo nell'immagine (giallo fisso = STOP).

## 5 · Il piano scena per scena (forma corta)
**Mondo:** REALE. Linea di assemblaggio di oggi, mattina dopo il terzo STOP: linea ferma, nastro fermo, beacon rosso acceso.
Quadro elettrico di bordo macchina sul lato manutenzione, sportello aperto verso il corridoio. Il PLC (con la faccia e il
monogramma MA) sta nella zona bassa, su guida DIN, fra moduli I/O e switch di rete; alimentatore 24 V e sezionatore in alto.
LED RUN/STOP **giallo fisso** (STOP) in tutte le scene; LED dei moduli accesi (c'è tensione). Cavo dalla porta PROFINET sul fondo
del PLC allo switch, e dallo switch al portatile del tecnico (Mister Automation, solo mani). Pagina del browser senza marchi.
**Set A** = dentro il quadro, primo piano del PLC. **Set B** = il portatile appoggiato sul ripiano davanti al quadro aperto.

| Scena | Set | Cosa si vede | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | PLC in primo piano, LED giallo fisso, beacon rosso riflesso sullo sportello | il PLC alza gli occhi in camera su «io so a che ora» |
| S2 | A | PLC, sotto di lui il cavo PROFINET che scende allo switch | il PLC abbassa lo sguardo verso il cavo su «lo scrivo» |
| S3 | B (seguiamo il cavo fino al portatile) | mani sulla tastiera, barra del browser con l'IP; PLC sullo sfondo nel quadro | il dito preme Invio su «indirizzo IP» |
| S4 | B | schermo: pagina «Buffer di diagnostica», tre righe di STOP con le ore (in cima la più tarda) | il dito indica la riga in cima su «in cima» |
| S5 | B | stesso schermo, colonna dell'ora | il dito scende e si ferma sulla riga con l'ora più vecchia su «più vecchia» |
| S6 | B | in alto nella pagina il selettore «UTC / Ora PLC» | il dito clicca «Ora PLC» su «l'ora del PLC» |
| S7 | A | PLC in primo piano, sportello aperto, linea ancora ferma | il PLC fa l'occhiolino su «DIAGNOSI» |

## 6 · Esito dei controlli
- **Lettore fresco e controllo dei limiti:** non lanciati (giro di prova: niente subagenti). Da fare prima di consegnare a Saverio.
- **Tempo** (`timing.py caso-03_parlato.txt --voce lipsync --obiettivo 54-60`):

```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      14    2.5    5.6     6       10
   S2      20    2.5    8.0     8       12
   S3      25    2.5   10.0    10       15
   S4      15    2.5    6.0     6       10
   S5      20    2.5    8.0     8       12
   S6      24    2.5    9.6    10       15
   S7      18    2.5    7.2    10       15  (+2 s CTA)
  TOT     136                  58       89

─── DURATA ───
somma delle clip: 58 s + asset riusabili 0 s = 58 s di montato
controllo veloce (parole ÷ 2.0): 68 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 17 · sotto le 6 parole: 5 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 54-60 s (avviso, non blocca) ───
  ✅ 58 s, dentro l'obiettivo

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 89 crediti su 7 clip
```
S3 è esattamente a 10,0 s: nessun margine; se in Flow la voce va lunga, la prima cosa da togliere è «prima» («va attivato dal software»).

## Deviazioni
- **Durata 58 s, sopra la fascia 48-56 dei reel migliori.** A Saverio: «L'indispensabile sono quattro pezzi: dove sta l'ora (buffer), come lo leggi (browser, ma il web server va attivato), l'ora e non la posizione, e l'ora vale se l'orologio è giusto. Sta in 58 s. Se vuoi 56, si toglie solo la sintesi "L'ora, non la posizione" dalla CTA (che passa da 10 a 8 s); i pezzi restano. Decidi tu.»
- **Quarto pezzo (orologio/UTC)** tenuto anche se il filo regge con tre: è il limite della promessa del titolo («so a che ora»); senza, il gancio promette più di quanto il corpo mantiene.
