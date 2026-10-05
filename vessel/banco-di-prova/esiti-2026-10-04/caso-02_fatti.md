# Scheda dei fatti · «Ho perso un nodo. Tutta la rete lo sta cercando» · 2026-10-04 · Granite

**Filo proposto da Vessel:** in PROFINET il PLC riconosce un dispositivo dal suo nome, non solo dall'IP; un nodo di I/O nuovo, montato al posto di uno guasto, senza nome non viene trovato · **Notebook usati:** Brain `5b0396dd` (copertura), Brain 2 `ae39f678` (verifica), Planimetrie `d1f8acfd` (nessuna risposta: errore della CLI, 2 tentativi) · **Copertura del tema:** buona dopo la ricerca. Prima era parziale: nel Brain 1 c'erano solo sintesi in Markdown, nessun documento del costruttore (vedi `caso-02_ricerca.md`)

Sigle delle fonti: **SIE** = Siemens, *PROFINET with STEP 7*, Function Manual 11/2022 (Brain 2 `ae39f678`) · **PI** = PI, *PROFINET System Description*, 2018 (Brain 2 `ae39f678`). Le pagine sono quelle dell'indice stampato.

## Fatti (solo questi entrano nel parlato)
| # | Fatto, per il caso delimitato | Fonte (notebook · documento · pagina o sezione) | Limite che va con il fatto | Stato |
|---|---|---|---|---|
| F1 | Prima che il controller (il PLC) possa indirizzare un dispositivo di I/O, il dispositivo deve avere un nome. Senza nome non scambia dati: né la configurazione all'avvio, né i dati ciclici. | `ae39f678` · SIE · §4.2.1 «Device name», p. 46 | Vale per i dispositivi di I/O PROFINET (IO device) | CONFERMATO |
| F2 | Nello stato di consegna un dispositivo di I/O non ha nome. | `ae39f678` · SIE · §4.2.1, p. 46 | «in delivery state»: un ricambio già usato può avere ancora un nome vecchio | CONFERMATO |
| F3 | Ogni dispositivo riceve un nome simbolico che lo identifica dentro il sistema di I/O; all'avvio MAC e IP vengono ricavati da quel nome. Il controller riconosce il dispositivo dal nome e gli assegna lui l'IP configurato. | `ae39f678` · PI · §2.5 «Addressing PROFINET Devices», p. 9 · SIE · §4.2.3, p. 50 | L'IP lo assegna il controller nel caso normale; alcuni dispositivi prendono l'IP in un altro modo (DHCP, metodi del costruttore) | CONFERMATO |
| F4 | All'avvio il controller stabilisce una relazione di comunicazione con **ciascun dispositivo configurato**: cerca quelli che ha nel progetto, col loro nome. | `ae39f678` · PI · §2.6 «Engineering of an IO System», p. 9 | — | CONFERMATO |
| F5 | Se il dispositivo non riceve dati entro il tempo di sorveglianza (watchdog), mette le uscite ai valori sostitutivi e il controller segnala «guasto stazione» (station failure). | `ae39f678` · SIE · §3.1.1 «PROFINET terms», p. 21 | — | CONFERMATO |
| F6 | Il nome si dà a mano con il software di programmazione: PC nella stessa rete, elenco dei «dispositivi accessibili», si sceglie il dispositivo **dal suo indirizzo MAC** e si preme «assegna nome». Poi il controller lo riconosce dal nome e gli dà l'IP. | `ae39f678` · SIE · §4.2.3, p. 50 | Procedura del software di un costruttore; il principio (nome dato via rete, dispositivo scelto per MAC) è anche in PI §2.5 | CONFERMATO |
| F7 | Fra più dispositivi identici in un quadro, quello giusto si riconosce facendo lampeggiare dal PC il LED di link del dispositivo. | `ae39f678` · SIE · §4.2.3, p. 50 | — | CONFERMATO |
| F8 | **Guasto e senza nome si distinguono dal PC.** Nella verifica dei dispositivi online lo stato è diverso: «dispositivo non raggiungibile» oppure «pronto per l'assegnazione», che compare quando il MAC c'è e il tipo corrisponde **ma online non si trova nessun nome**. | `ae39f678` · SIE · §4.2.4 «Assign device name via communication table», p. 55 | Sono gli stati della tabella di un software preciso; per altri costruttori non verificato. Il notebook conferma la tabella, non una spia del dispositivo | CONFERMATO |
| F9 | Il LED di link della porta: spento = nessuna connessione Ethernet col partner; verde = connessione presente. | `ae39f678` · SIE · §5.2 «Diagnostics via LEDs», p. 76 | Tabella per quattro famiglie di un costruttore. **Il LED dice se c'è il cavo, non se c'è il nome** | CONFERMATO |
| F10 | Lo stato del dispositivo si legge dal PC direttamente dal dispositivo, senza passare dal controller, anche se il controller non è operativo. | `ae39f678` · SIE · §5.1, p. 73 | Solo col PC collegato alla rete | CONFERMATO |
| F11 | **Il controller può dare il nome da solo** («sostituzione senza supporto rimovibile / senza PC»): confronta la topologia configurata con i vicini reali che ogni dispositivo annuncia sulle porte (LLDP), trova il dispositivo senza nome e gli assegna nome e IP. | `ae39f678` · SIE · §6.9-6.9.2, p. 225-228 · PI · §4.2 e §4.4, p. 12-13 | **Solo se:** la topologia (porta per porta) è configurata nel progetto; il dispositivo supporta la funzione; la funzione è attiva nel controller (lo è di default); il ricambio è nuovo o riportato allo stato di consegna | CONFERMATO |
| F12 | Se il dispositivo non supporta questa sostituzione automatica, il controller emette un allarme per quel dispositivo. | `ae39f678` · SIE · §6.9.2, p. 228 | — | CONFERMATO |
| F13 | Dopo la sostituzione il cavo di rete va rimesso **nella stessa porta** prevista nel progetto: se no i nomi possono essere assegnati in modo sbagliato. Un dispositivo inserito in un'altra posizione riceve il nome di un altro; va riportato allo stato di consegna prima di riusarlo. | `ae39f678` · SIE · §6.9 p. 225 e §6.9.1 p. 227 | Vale con la sostituzione automatica attiva | CONFERMATO |
| F14 | Un ricambio che ha già un nome non viene rinominato dal controller, a meno che nel controller sia attiva l'opzione «permetti di sovrascrivere i nomi dei dispositivi»; senza l'opzione il nome va dato a mano o cancellato prima. Prima di sovrascrivere il controller controlla che il tipo corrisponda. | `ae39f678` · SIE · §6.9.3, p. 229 | Opzione non presente su tutti i controller | CONFERMATO |
| F15 | Un dispositivo con scheda di memoria rimovibile: il nome sta sulla scheda; spostando la scheda dal vecchio al nuovo (prima di accenderlo) il nome passa al ricambio. | `ae39f678` · SIE · §4.2.3, p. 50-51 | Solo per dispositivi che hanno la scheda | CONFERMATO |


**Aggiunto da Vessel dopo il lettore fresco (4/10, verificato su `source fulltext` del manuale SIE):**
| F16 | Il nome che si assegna al nodo è **il nome configurato nel progetto**: dal PC si scarica nel dispositivo «the configured device name» (scelto il dispositivo dal MAC, «Assign name»); poi il controller lo riconosce dal nome e gli assegna l'IP configurato. Un nome diverso da quello del progetto non fa ritrovare il nodo. | `ae39f678` · SIE · «Downloading configured device name to IO device» (§4.2) | la seconda frase («un nome diverso…») è la conseguenza della prima, non una citazione | CONFERMATO |

## Numeri confermati
- Nessun numero serve al filo. (L'opzione di F14 esiste per esempio su una CPU compatta dal firmware 4.0: SIE §6.9.3, 11/2022. Riguarda un modello solo, quindi meglio non usarlo.)

## Termini veri
- **Nome dispositivo** (device name, «NameOfStation») — secondo la fonte è il nome simbolico che identifica il dispositivo dentro il sistema di I/O; da quel nome si ricavano MAC e IP all'avvio (PI §2.5). Nel video: «il nome del dispositivo».
- **Controller di I/O** (IO controller) / **dispositivo di I/O** (IO device) — chi comanda e il nodo periferico (SIE §3.1.1). Nel video: «il PLC» / «il nodo di I/O».
- **Stato di consegna** (delivery state) — dispositivo come esce dalla fabbrica, senza nome (SIE §4.2.1). Nel video: «nuovo di fabbrica».
- **Rilevamento dei vicini** (neighborhood detection, protocollo LLDP) — ogni dispositivo dice sulle sue porte chi è, così si sa chi è collegato a quale porta (PI §4.2). Nel video: «sa chi ha accanto».
- **Sostituzione senza supporto rimovibile / senza PC** (device replacement without exchangeable medium/PG) — il controller dà il nome al ricambio dalla topologia (SIE §6.9). Nel video: «il PLC gli ridà il nome da solo».
- **Guasto stazione** (station failure) — il controller non riceve più i dati dal dispositivo (SIE §3.1.1). Nel video: «nodo perso».
- **Dispositivi accessibili / Lampeggio LED / Assegna nome** — comandi del software di programmazione (SIE §4.2.3). Nel video senza marchio: «il software di programmazione».

## Errore plausibile di chi guarda
1. «Il nodo nuovo è identico e l'IP lo imposto io: deve funzionare» → no: il PLC lo cerca per nome e il nuovo di fabbrica non ce l'ha (F1, F2, F3).
2. «Non lo trova, quindi anche il ricambio è guasto» → il PC lo distingue: «non raggiungibile» contro «pronto per l'assegnazione» (MAC presente, nome no) (F8). Il LED di link verde dice solo che il cavo c'è (F9).
3. ⚠ **L'errore opposto, quello del filo se lo si allarga:** «un nodo nuovo senza nome non viene MAI trovato». Falso se la topologia è configurata e il dispositivo supporta la funzione: allora il PLC gli dà il nome da solo (F11). Il filo vale per il caso **senza topologia configurata, o con un dispositivo che non supporta la funzione, o con un ricambio che ha già un nome** (F11, F12, F14).
4. «Lo monto dove capita, tanto è uguale» → con la sostituzione automatica, porta sbagliata = nome sbagliato (F13).

**Cosa controllare dopo una sostituzione** (tutto dai fatti sopra): il cavo di rete è nella stessa porta di prima (F13) · il LED di link è verde (F9) · il ricambio è nuovo o riportato allo stato di consegna (F2, F11, F14) · dal PC: «non raggiungibile» o «pronto per l'assegnazione»? (F8) · se il PLC non l'ha nominato da solo, si dà il nome a mano scegliendo il dispositivo dal MAC e facendo lampeggiare il LED per essere sicuri (F6, F7).

## Dove sta davvero il componente
Due casi veri. Scegline uno solo per la scena.
- **Nel quadro** · moduli I/O e switch su guida DIN, **in basso** nella zona logica, vicino al PLC · cavo di rete con connettore RJ45 dal PLC o dallo switch al nodo · fonte SET-TIPO §0-bis (riga «PLC, moduli I/O, switch di rete»); PI §10.3 p. 24 (connettori «inside» per il quadro = RJ45); SIE §4.2.3 («più dispositivi identici in un quadro»).
- **Sul campo, fuori dal quadro** · connettori per esterno, push-pull o M12 · fonte PI §10.3 p. 24 (connettori «outside», per i dispositivi direttamente sul campo). Per analogia con SET-TIPO §0-bis (IO-Link master: blocco IP67 imbullonato al telaio, vicino ai sensori, cavi M12): **non confermato per un nodo PROFINET**, perché Planimetrie non ha risposto.
- Lato: il quadro di solito sta sul lato manutenzione della linea (SET-TIPO §0-bis).
Com'è fatto (per il disegno): porte di rete con LED di link per ogni porta (SIE §5.2); il disegno d'ingombro non è stato cercato perché il reel non nomina un modello.

## Non confermato — il parlato non lo usa
- Come appare **sulle spie del nodo** (LED di errore o di bus) un dispositivo acceso ma senza nome, rispetto a uno guasto o spento — non c'è in SIE né in PI. Il Brain 1 lo dice solo nelle sintesi in Markdown, che non sono fonti del costruttore.
- «Se nel programma c'è il blocco per il guasto stazione la CPU non va in STOP» — c'è solo nella sintesi Markdown «Il "Mega Cervello"…» (Brain 1). Il comportamento cambia da una famiglia di CPU all'altra: non usarlo.
- Testi o codici esatti del registro diagnostico per «nodo non trovato» e per «nome mancante» — non coperti (Brain 1 e Brain 2).
- Posizione fisica tipica di un nodo PROFINET sul campo (altezza, staffa, telaio) — Planimetrie `d1f8acfd` ha dato errore di risposta vuota per 2 volte; manca anche nei manuali.

## Aggiunto ai notebook oggi
- Siemens *PROFINET with STEP 7*, Function Manual 11/2022 → `ae39f678` (https://cache.industry.siemens.com/dl/files/856/49948856/att_897210/v1/profinet_step7_v18_function_manual_en-US_en-US.pdf) · ricerca in `caso-02_ricerca.md`
- PI *PROFINET System Description*, 2018 → `ae39f678` (https://www.profibus.com/fileadmin/media/downloadsection/technical_description_&_books/PROFINET_System_Description_engl_2018_Update.pdf)
- Nessuna sintesi caricata come testo: i due PDF ufficiali bastano, e una sintesi nel notebook verrebbe poi citata come se fosse una fonte (è quello che è successo nel Brain 1).
