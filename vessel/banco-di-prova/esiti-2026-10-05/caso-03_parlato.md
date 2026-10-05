# Caso 03 · «Stanotte questa linea si è fermata tre volte. E io so a che ora.» · passo 3 · 2026-10-05
Slot lunedì 18:30 → componente con la faccia: parla **la CPU**, in prima persona, al tu. Keyword DIAGNOSI. Primo passaggio,
versione unica. Scritto dalla copia PROVA (SKILL.md, fasi/3-storia-parlato.md, quaderno vuoto, esempi 01-02-03-07).

## 1 · Filo
**Filo:** la riga che leggi per prima nel buffer di diagnostica non è la prima cosa successa: per sapere quando è
cominciato si guarda la colonna dell'ora, non la posizione. Caso: la CPU stanotte è andata in STOP tre volte e il buffer
si legge dal browser.
**Errore plausibile** (scheda, errore 1): «la prima riga è la causa / è dove è cominciato tutto».
**Durata obiettivo: 48-56 s**, la fascia standard: un caso (tre fermate), un passo pratico (aprire il buffer dal browser),
un errore, la correzione, il gesto che ne segue. Nessun motivo per uscirne.

## 3 · Il discorso (prima consegna, di fila)
B1. Stanotte questa linea si è fermata tre volte. E io so a che ora.
B2. Sono la CPU. Ogni volta che vado in STOP scrivo una riga nel mio buffer di diagnostica, con l'ora.
B3. Non ti serve il software di programmazione: il web server l'hanno attivato. Apri il browser e scrivi il mio IP.
B4. Ecco il buffer. La prima riga dice: passaggio a STOP, 4:51. E pensi: «È cominciato tutto lì.»
B5. È la prima che leggi, non la prima che è successa. Guarda l'ora: la prima fermata è alle 23:40.
B6. Vai alla riga delle 23:40 e cliccala: sotto compaiono i dettagli. È da lì che cominci a cercare il perché.
B7. Guarda l'ora, non la posizione. Vuoi impararlo? Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.

Controllo MA / QUINDI: B1 →(quindi: come lo sai?) B2 →(ma come lo leggi?) B3 →(quindi) B4 →(ma) B5 →(quindi) B6 →(quindi) B7.
Il dubbio di chi guarda (B4, «è cominciato tutto lì») sta dove nasce l'errore; B5 riprende la parola «prima» e chiude
sull'effetto (l'ora delle 23:40).

## Il taglio
| Battuta | Clip | Note |
|---|---:|---|
| B1 → S1 | 6 s | gancio, 14 parole |
| B2 → S2 | 8 s | tolto «data, ora e cosa è successo» → «con l'ora»: la data e la descrizione non servono al filo |
| B3 → S3 | 8 s | tolto «indirizzo» (resta «il mio IP», come lo dice un tecnico) e «mio» davanti a web server |
| B4 → S4 | 8 s | il dubbio scritto prima come «È la prima riga: è cominciato tutto lì, no?» → tolto «è la prima riga»: lo dice già la frase prima |
| B5 → S5 | 8 s | — |
| B6 → S6 | 8 s | — |
| B7 → S7 | 10 s | tolto «Tre fermate, tre righe» prima della sintesi: portava la CTA a 10,4 s |
Nessuna battuta divisa. Una battuta per clip.

## 4 · Piano scena per scena (forma corta)
**Mondo:** IBRIDO (fabbrica vera + un solo ologramma in S2, mai toccato). Linea di confezionamento all'alba, ferma:
nastri fermi, niente in moto. **Componente:** la CPU con la faccia (monogramma MA sul frontale), su guida DIN nella **zona
bassa** del quadro di bordo macchina, lato manutenzione, sportello aperto verso il corridoio; accanto moduli I/O e switch di
rete; drive e contattori in mezzo; alimentatore 24 V e sezionatore in alto. Cavo dalla porta PROFINET **sul fondo** della CPU
allo switch. **LED RUN/STOP giallo fisso (STOP) in tutte le scene**: la terza fermata è ancora in corso. Mister Automation
c'è, muto, volto 3/4: è il «tu» con il portatile.
**Set A** = davanti al quadro aperto. **Set B** = il portatile appoggiato sul ripiano del quadro, cavo di rete allo switch
(«seguiamo il cavo» dalla CPU allo switch dà la causa del passaggio).

| Scena | Set | Cosa si vede | Stato | Gesto ↔ parola |
|---|---|---|---|---|
| S1 | A | linea ferma all'alba, quadro aperto, la CPU guarda in camera | LED giallo fisso, tutto fermo | su «so a che ora» la CPU alza un sopracciglio, mezzo sorriso |
| S2 | A | primo piano della CPU; accanto le compare un ologramma: una riga «Passaggio a STOP · 23:40» | LED giallo | su «scrivo una riga» la riga olografica si accende |
| S3 | B | la camera segue il cavo dal fondo della CPU allo switch, al portatile; barra degli indirizzi con un IP generico; CPU a bordo inquadratura | LED giallo; schermo acceso | su «scrivi il mio IP» le mani di M.A. battono l'indirizzo |
| S4 | B | sopra la spalla di M.A.: pagina «Buffer di diagnostica» senza marchi; in cima «Passaggio a STOP · 04:51», sotto 02:15 e 23:40 con passaggi a RUN in mezzo; CPU visibile a destra | LED giallo | su «È cominciato tutto lì» il dito di M.A. tocca la prima riga; la CPU stringe gli occhi |
| S5 | B | CPU in primo piano, schermo di lato con la colonna dell'ora | LED giallo | su «Guarda l'ora» la CPU sposta lo sguardo giù, verso la riga delle 23:40 |
| S6 | B | M.A. clicca la riga delle 23:40; sotto si apre il riquadro dei dettagli | LED giallo | su «cliccala» il clic; la CPU annuisce |
| S7 | A | stesso asse di S1: la CPU in camera, M.A. col portatile accanto al quadro; scritta DIAGNOSI | LED giallo, linea ancora ferma | su «Guarda l'ora» la CPU fa l'occhiolino |

## Verità battuta per battuta
| Battuta | Affermazione | Fatto della scheda | Limite |
|---|---|---|---|
| B1 | la linea si è fermata tre volte; la CPU sa a che ora | F1 (voce con data e ora), F2 (ogni passaggio a STOP) | caso delimitato: le tre fermate sono passaggi a STOP della CPU (B2 lo nomina: «ogni volta che vado in STOP») |
| B2 | ogni passaggio a STOP → una riga nel buffer di diagnostica, con l'ora | F1, F2 | F2: vale per gli STOP della CPU, detto a voce. F9 (orologio) non detto: vedi Deviazioni |
| B3 | senza software di programmazione, dal browser, con l'IP; il web server «l'hanno attivato» | F5, F8, F7 | F7 a voce: «l'hanno attivato» dice che qualcuno l'ha acceso prima. Permesso «Query diagnostics» e VPN non detti |
| B4 | pagina del buffer; la prima riga è un passaggio a STOP alle 4:51 | F6 (pagina, righe con data e ora), F2 | dato di scena del caso, non regola generale |
| B5 | la prima riga letta non è la prima successa; si guarda l'ora | F6 (limite: «guarda l'ora, non la posizione» regge sempre), F3 | non si dice a voce che nella pagina web la più recente sta in cima (non confermato) |
| B6 | cliccando una riga compaiono i dettagli sotto; si parte dalla prima fermata | F6; «per la causa si scende verso le voci più vecchie e si confrontano le ore» (scheda, errore 1) | non si dice che i dettagli contengano il motivo dello STOP (non confermato) |
| B7 | sintesi + CTA | F6 (regola che regge sempre) | — |
Numeri: nessuno (la CPU in scena non ha modello). Marchi: nessuno a voce né in scena.

## Deviazioni
- **Piano, S4:** la schermata mostra la riga più recente in cima. È coerente con F3 (buffer in generale), ma per la pagina
  web l'ordine non è confermato (F6). La voce non dipende dall'ordine («guarda l'ora»); chi fa le immagini lo sappia: se si
  vuole zero rischio, la schermata può mostrare le tre righe con l'ora evidenziata invece della posizione.
- **F9 (orologio) e F10 (UTC) non detti a voce.** Motivo: la regola del reel è l'ordine per ora, e quello regge anche con
  l'orologio sbagliato (tutte le righe sono spostate allo stesso modo); quindi non cambiano la decisione di chi guarda davanti
  a questo buffer. «So a che ora» è detto dalla CPU per il suo caso. Vanno nella descrizione: «l'ora è quella dell'orologio
  della CPU: va impostato; senza cookie la pagina mostra l'UTC».
- **F4 (buffer che si sovrascrive) non detto:** errore plausibile 2 della scheda, un'idea in più; in questo caso le righe ci sono.
  Candidato per la descrizione o per un altro reel.
- **Mister Automation in scena muto** accanto al componente che parla: serve un «tu» che digita e clicca. Una sola voce per clip.

## Uscita del timing
```
python3 .../prova-2026-10-05/vessel/scripts/timing.py caso-03_parlato.txt --voce lipsync --obiettivo 48-56

scena  parole  p/sec    sec  clip  crediti
   S1      14    2.5    5.6     6       10
   S2      19    2.5    7.6     8       12
   S3      20    2.5    8.0     8       12
   S4      17    2.5    6.8     8       12
   S5      19    2.5    7.6     8       12
   S6      20    2.5    8.0     8       12
   S7      17    2.5    6.8    10       15  (+2 s CTA)
  TOT     126                  56       85
somma delle clip: 56 s di montato · controllo veloce (parole ÷ 2.0): 63 s
spia di mestiere: frasi 17 · sotto le 6 parole: 6 · sopra le 25: 0
OBIETTIVO 48-56 s: ✅ 56 s, dentro l'obiettivo
ESITO: ✅ nessuna scena oltre i 10 s · 🟢 VERDE · 85 crediti su 7 clip
```
Nota: S3 e S6 sono a 8,0 s esatti, al limite della clip da 8: se la voce rallenta, salgono a 10 e il montato esce a 58-60 s.

## Controlli non fatti qui
Lettore fresco e controllo dei limiti: li fa chi ha lanciato il giro (come da consegna).
