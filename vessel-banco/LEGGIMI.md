# Banco di prova di Vessel

> **Stato dal 5/10: congelato.** Il banco non si usa finché non esce un reel vero fatto con Vessel dall'inizio alla fine,
> immagini e Flow compresi. In due giorni ha prodotto quattro giri e otto regole nuove su casi finti, ed è lo stesso
> meccanismo che ha gonfiato Vincent. Le correzioni arrivano da Saverio, sui reel veri, e vanno nel quaderno.

## A cosa serve (quando si riapre)
A decidere **cosa togliere o fondere** nel quaderno e nelle pagine, e a provare uno script prima di usarlo. Non serve a
inventare regole nuove: una regola nata da un errore su un caso finto può rovinare i lavori che riuscivano.

## Dove sta, e perché
Il banco sta **fuori** dalla cartella della skill (`~/vessel-banco/`), perché dentro ci sono i bersagli. Ogni giro si fa su
**una copia della skill** da cui si tolgono, prima di lanciare, gli esempi che sono il bersaglio del caso (01, 02, 05 in
`esempi/parlato/`) e le voci del quaderno che li citano. Dire a chi scrive «non guardarli» non basta: un subagente può
aprire qualsiasi file che vede.

## I casi (`casi/`)
| Caso | Cosa prova | Cosa si nasconde a chi scrive |
|---|---|---|
| 01 · cieco induttivo | riscrivere il parlato avendo solo la tabella v2 e l'obiettivo, come Astra il 30/9 | l'esempio 01 (è il bersaglio) |
| 02 · PROFINET | storia + parlato su un titolo già uscito, dalla scheda dei fatti | l'esempio 02 |
| 03 · web server | storia + parlato su un titolo già uscito, dalla scheda dei fatti | l'esempio 05 |
| 04 · catena portacavi | tema mai fatto, scheda dei fatti nuova | niente (non c'è un esempio sul tema) |
| 05 · controllo negativo | il lettore fresco sulla v2 bocciata: deve trovare più problemi che sulla v4 approvata | — |
I bersagli (`bersagli/`) si aprono **solo dopo**, per il confronto.

## Come si fa un giro
1. **Scheda dei fatti** (casi 02-04): un subagente Granite con `fasi/2-verita.md`, uscita in `esiti-<data>/caso-0N_fatti.md`.
   Se le schede di un giro precedente sono ancora buone, si riusano: il banco prova la scrittura, non i notebook.
2. **Scrittura**: un subagente fresco per caso, che legge solo `SKILL.md`, `fasi/3-storia-parlato.md`, `quaderno.md`, gli esempi
   permessi e l'input del caso, e scrive filo, parlato, piano scena per scena e copione in `esiti-<data>/caso-0N_parlato.md`.
   Si usa un subagente e non la chat principale perché chi prova non deve aver visto i bersagli.
3. **Controlli**: `scripts/timing.py` su ogni copione; un lettore fresco **nuovo** (Aqua Regia) per ogni parlato, compreso il
   controllo negativo e la v4 approvata come controllo positivo.
4. **Confronto** coi bersagli, battuta per battuta per il caso 01; per mosse (filo, dubbio, termine vero, chiusa) per 02-03.
   Verità: ogni affermazione dei parlati si cerca nella scheda; una inventata = caso bocciato.
5. **Esito** in `COLLAUDO-<data>.md`: cosa è passato, cosa no, cosa si cambia. Una modifica entra solo se il giro con la
   modifica non è peggiore del giro senza sui casi riusciti.

## Cosa conta come prova
- **Regola di scrittura** (pagina 3, quaderno, esempi): si rigenerano **almeno 2 casi** con la regola attiva e scrittori
  nuovi, e uno dei due è un caso già riuscito. Controllare che i testi approvati rispettino la regola è una conferma, non una
  prova.
- **Controllo** (lettore fresco, controllo dei limiti): si fa girare su un testo bocciato, su uno approvato e su un caso di
  confine: deve distinguerli.
- **Script**: si fa girare sui copioni che esistono già.
- **I criteri di successo si scrivono prima del giro** (`esiti-<data>/CRITERI.md`), non dopo.
- **Gli esempi delle pagine non vengono dai casi del banco**: lo scrittore ci leggerebbe la risposta.
- Un tentativo per caso è poco: se un caso cambia esito, si rigenera una seconda volta prima di concludere.
- **Un lettore solo non basta per decidere una regola.** Prima di fidarsi del lettore fresco su un testo, lo stesso testo si
  dà a 3 lettori nuovi: se si perdono in punti diversi, quello che dice uno solo è rumore.
- **Un giro conta solo se il testo finale è passato dai suoi controlli** (lettore fresco e limiti). Il 5/10 il giro 05c è
  stato adottato senza: il caso 02 finale ha ancora la frase sulla topologia, mai riletta da un lettore.
- **Il tono** non lo misura nessun controllo: Saverio legge la versione vecchia e la nuova come A e B senza sapere quale è
  quale, e sceglie.
