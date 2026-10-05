# Caso 03 · «Stanotte questa linea si è fermata tre volte. E io so a che ora.» · passo 3 · Vessel (prova 2026-10-05c)

Slot lunedì 18:30 → componente con la faccia: **il PLC (la CPU) parla in prima persona**, al tu. Keyword DIAGNOSI.
Fonte unica dei fatti: `esiti-2026-10-04/caso-03_fatti.md` (F1…F13). Quaderno: vuoto, nessuna voce da applicare.

## 1 · Prima della prima battuta

**Il filo, in una riga.** La riga in alto della pagina del buffer non è per forza la prima fermata: quale è venuta prima te
lo dice l'ora; e il buffer va letto prima di spegnere il PLC, perché le righe vecchie si perdono.

**Cosa deve saper distinguere chi guarda.** La *posizione* di una riga nel buffer dalla *sua ora*: la prima fermata della
notte è quella con l'ora più vecchia, non quella che leggi per prima.

**Il caso preciso.** Il PLC di una linea è andato **in STOP** tre volte stanotte (01:12, 03:40, 04:55). Il suo web server è
stato attivato e l'orologio regolato quando l'hanno configurato. La mattina il manutentore lo legge da un browser, col suo
indirizzo IP, collegato alla rete del quadro, **prima** di spegnere e riaccendere. Nessun modello di CPU in scena → nessun
numero di righe a voce.

**L'indispensabile** (senza questi, domani davanti al PLC si sbaglia):

| # | Pezzo, con l'appiglio | Errore che evita | Fatti |
|---|---|---|---|
| I1 | Ogni volta che il PLC **va in STOP** scrive una riga, con data e ora, nel buffer di diagnostica. Appiglio: «scrivo una riga». | ripartire a intuito, chiedere al turno di notte «quando si è fermata?» senza un dato | F1, F2 (caso nominato: «vado in STOP») |
| I2 | Lo leggi da un browser scrivendo l'indirizzo IP del PLC — **perché qui** il web server l'hanno attivato e l'orologio l'hanno regolato. Appiglio: il gesto di scrivere l'IP. | cercare il portatile col software per una lettura; oppure credere che basti il browser su qualunque PLC e che l'ora sia sempre giusta | F5, F8; limiti F7 e F9 nominati come caso |
| I3 | **L'ora, non la posizione**: la riga in alto non è per forza la prima cosa successa. | prendere la riga in alto per la prima fermata (errore plausibile 1 della scheda) | F3, F6 (l'ordine nella pagina web non è confermato: per questo «non è detto») |
| I4 | **Leggimi prima di spegnermi**: a buffer pieno le righe nuove cancellano le vecchie, e da spento ne resta solo una parte, le più recenti. Appiglio: la mano che si ferma sul sezionatore. | spegnere e riaccendere il quadro per far ripartire la linea e perdere la riga dell'01:12 (errore plausibile 2) | F4 |

**Fuori dalla voce** (scheda e descrizione): numero di righe per CPU (50/10 · 500/100), UTC quando il browser non accetta
i cookie e fuso orario, permesso «leggere la diagnostica», VPN da fuori rete, salvataggio in csv, l'esempio del tempo di
ciclo (F11), la fermata con CPU in RUN (F2: non è il caso mostrato).

**Durata obiettivo: 50-56 s.** Quattro pezzi più gancio e CTA = 7 scene; due pezzi (I2, I4) portano con sé il loro caso o
il loro perché, quindi si sta verso l'alto della fascia dei reel migliori, non sotto.

**La chiusura che il contenuto autorizza.** «L'ora, non la riga» (sintesi del filo) e il gesto «leggimi prima di spegnermi».
**Non** autorizzata: «e da lì trovi la causa» — nessuna fonte dà un metodo per riconoscere la causa (non confermato).

## 2 · Il discorso

B1 Stanotte questa linea si è fermata tre volte. E io so a che ora.
B2 Sono il PLC. Ogni volta che vado in STOP, scrivo una riga nel buffer di diagnostica, con data e ora.
B3 Il mio web server l'hanno attivato, l'orologio l'hanno regolato: apri un browser e scrivi il mio indirizzo IP.
B4 Ecco le tre righe di STOP. Guardi quella in alto: «È la prima fermata, no?»
B5 La prima? Non è detto. La prima te la dice l'ora, non la posizione: è quella dell'una e dodici.
B6 Ma leggimi prima di spegnermi: quando il buffer è pieno, le righe nuove cancellano le vecchie, e da spento tengo solo le ultime.
B7 L'ora, non la riga. Vuoi imparare a leggere la diagnostica? Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.

Controllo MA/QUINDI: B1→B2 quindi (come lo sai?) · B2→B3 quindi (come la leggo?) · B3→B4 quindi · B4→B5 **ma** ·
B5→B6 **ma** · B6→B7 quindi. Nessun «e poi».

## 3 · Il taglio

| Battuta | Scena | Clip |
|---|---|---:|
| B1 | S1 | 6 s |
| B2 | S2 | 8 s |
| B3 | S3 | 8 s |
| B4 | S4 | 6 s |
| B5 | S5 | 8 s |
| B6 | S6 | 10 s |
| B7 | S7 | 10 s (CTA) |

Una battuta per clip, nessuna oltre i 10 s. La prima stesura misurava **64 s** (stessi pezzi). Ridondanze tolte per entrare
nell'obiettivo, senza toccare l'indispensabile:
- «Quindi ti basta un browser.» → tolta: il gesto «apri un browser e scrivi il mio indirizzo IP» lo dice già.
- «Le mie righe sono contate» → tolta: lo dice già «quando il buffer è pieno, le nuove cancellano le vecchie».
- «L'ordine te lo dice l'ora» → «la prima te la dice l'ora»: riprende la parola del dubbio e accorcia.
- «Prima mi leggi, poi mi spegni» in chiusa → tolta: ripeteva B6; al suo posto «L'ora, non la riga», che chiude il filo.
- «nel *mio* buffer» → «nel buffer»; «Il mio web server è acceso e il mio orologio è regolato» → «l'hanno attivato… l'hanno
  regolato» (stessa lunghezza, ma dice che qualcuno l'ha fatto prima: è il limite di F7).

## 4 · Note battuta per battuta

| | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | apre la promessa: chi sa quando? | — (gancio = titolo) | «Il PLC si è fermato tre volte»: toglie il mistero e anticipa chi parla |
| B2 | «come fa a saperlo?» → la riga con data e ora; nomina il caso «vado in STOP» | F1, F2 | «Ogni volta che la linea si ferma, scrivo una riga»: falso per le fermate col PLC in RUN (limite F2) · «data, ora, categoria e descrizione»: vero, ma la categoria non serve alla decisione |
| B3 | «come la leggo?» → browser e IP; il caso nomina web server attivato e orologio regolato | F5, F7, F8, F9 | «Senza software, ti basta il browser»: il software serve ad attivare il web server (F7) · spiegare UTC, cookie e fuso: nel caso mostrato l'orologio è giusto e chi guarda non sbaglia; va in descrizione |
| B4 | mostra le righe e dà voce al dubbio di chi guarda, con le sue parole | F2, F6 | «La prima riga è la causa»: la scheda non dà un metodo per la causa, il reel non può chiudere quella domanda · «tre righe e basta»: nel buffer ci sono anche i passaggi a RUN (F2), le righe di STOP sono tre fra le altre |
| B5 | risponde riprendendo «la prima» e chiude sull'effetto: l'ora dell'01:12 | F3, F6 | «In cima c'è sempre la più recente»: vero per il buffer letto col software (F3), **non confermato** per la pagina web (F6); «non è detto» + «l'ora, non la posizione» regge in entrambi i casi |
| B6 | «e adesso riavvio?» → prima leggi, e il perché in due meccanismi | F4 | dire il numero di righe (50, 500…): dipende dalla CPU e in scena non c'è un modello · «se mi spegni perdo tutto»: falso, ne resta una parte |
| B7 | sintesi in tre parole del filo, poi una CTA e la tagline | — | «Prima mi leggi, poi mi spegni»: doppione di B6 · «e da lì trovi la causa»: non confermato |

Assoluti ed eccezioni: la regola «ogni STOP = una riga» è detta col caso («vado in STOP»), non come «ogni fermata della
linea». L'eccezione «linea ferma con CPU in RUN» resta fuori: nel caso mostrato le tre fermate sono tre STOP, e la decisione
di chi guarda (leggere l'ora, leggere prima di spegnere) non cambia.

## 5 · Il piano scena per scena (forma corta)

**Mondo IBRIDO**: linea di assemblaggio di oggi all'alba, ferma; le righe del buffer compaiono anche come ologrammi accanto
al PLC (mai toccati). **Set A**: corridoio di manutenzione a bordo linea. **Set B**: dentro il quadro di bordo macchina aperto
(si entra seguendo il cavo dal PLC allo switch al portatile). Parla solo il PLC; Mister Automation c'è con le mani e il
portatile, muto.
**Componente**: il PLC con la faccia, logo MA, su guida DIN nella **zona bassa** del quadro, moduli I/O a sinistra, switch a
destra; cavo dalla porta di rete **sul fondo** del PLC allo switch, e dallo switch al portatile appoggiato sul ripiano dello
sportello (connesso ai due capi). Alimentatore 24 V e sezionatore in alto. Stato fisso: **linea ferma, nastro fermo, beacon
rosso, LED RUN/STOP giallo fisso (STOP, F13)**, nessuna parte in moto.

| Scena | Set | Cosa si vede · stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | linea ferma all'alba, beacon rosso; sportello del quadro aperto, il PLC in basso con LED giallo | il PLC alza gli occhi in camera su «**so** a che ora» |
| S2 | B | primo piano del PLC fra I/O e switch; accanto, ologramma di una riga «STOP · 01:12» | l'ologramma della riga appare su «**scrivo**» |
| S3 | B | si segue il cavo dal fondo del PLC allo switch al portatile; sullo schermo un browser vuoto, senza marchi | il dito di Mister Automation batte l'IP su «**scrivi**» |
| S4 | B | sullo schermo la pagina «Buffer di diagnostica»: righe con colonna Data e ora, tre STOP evidenziati fra i RUN (04:55 in alto, 01:12 in basso) | il dito del tecnico punta la riga in alto su «**in alto**» |
| S5 | B | stessa pagina; la riga 01:12 si illumina (ologramma) | il PLC sposta lo sguardo in basso su «**l'una e dodici**» |
| S6 | B | la mano del tecnico sul sezionatore, ancora acceso; PLC con LED giallo | la mano si ferma su «**spegnermi**» |
| S7 | B | portatile con la riga 01:12 aperta nei dettagli; blocco note con «01:12» | la matita scrive «01:12» su «**l'ora**»; il PLC guarda in camera per la CTA |

## 6 · Controlli

**Tempo** — `timing.py caso-03_parlato.txt --voce lipsync --obiettivo 50-56`:

```
scena  parole  p/sec    sec  clip  crediti
   S1      14    2.5    5.6     6       10
   S2      20    2.5    8.0     8       12
   S3      18    2.5    7.2     8       12
   S4      15    2.5    6.0     6       10
   S5      19    2.5    7.6     8       12
   S6      23    2.5    9.2    10       15
   S7      20    2.5    8.0    10       15  (+2 s CTA)
  TOT     129                  56       86
somma delle clip: 56 s di montato · controllo veloce (parole ÷ 2.0): 64 s
OBIETTIVO 50-56 s: ✅ 56 s, dentro l'obiettivo · nessuna scena oltre i 10 s · 🟢 VERDE · 86 crediti su 7 clip
```
Avvisi: 56 s è il bordo alto della fascia; il controllo veloce (÷2,0) dà 64 s, quindi se la voce di Flow parla lenta S6 è la
clip più a rischio (23 parole, una sopra le ~22 del mestiere).

**Lettore fresco e controllo dei limiti** — **non eseguiti** in questa prova: l'istruzione del giro vieta i subagenti, e il
controllo dei limiti non va fatto da chi ha scritto il testo. Da lanciare prima di dare il parlato a Saverio.

## Deviazioni
- **Ordine delle righe nella pagina web (F6, PARZIALE).** Il parlato non lo afferma («non è detto»), ma l'immagine di S4
  deve mostrare un ordine: la disegno con la più recente in cima, come dice F3 per il buffer in generale. A Saverio: «la
  pagina in S4 mostra la più recente in alto come il buffer del software; se Granite non trova conferma per il web, la
  scena tiene la colonna dell'ora in primo piano e l'ordine fuori fuoco».
- **Orari 01:12 · 03:40 · 04:55** inventati per il caso (non sono fatti tecnici).
- Nessuna deviazione di durata: l'indispensabile entra in 56 s.
