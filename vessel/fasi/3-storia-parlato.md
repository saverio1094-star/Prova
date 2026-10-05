# Passo 3 · Storia e parlato (lo scrive Vessel)

## Intento
Un discorso che un tecnico ascolta fino in fondo e alla fine **sa distinguere una cosa che prima confondeva**, detto da un
personaggio che fa cose vere in una fabbrica vera. Parlato, storia e piano scena per scena nascono insieme, dalla stessa
mano, perché ogni battuta deve stare sopra quello che si vede.

## Cosa ricevi
La scheda dei fatti di Granite (`copioni/<slug>_fatti.md`): fatti per il caso delimitato con le fonti, numeri confermati,
errore plausibile e limite che lo corregge, dove sta davvero il componente, cosa è non confermato. Più il titolo, lo slot
(che forma vuole il giorno) e `quaderno.md`.

## Cosa consegni
Nel master, sezioni 1, 3 e 4 di `modelli/master.md`:
- **prima della prima battuta** (è il lavoro che decide il reel, come lo fa Astra): cosa deve saper distinguere chi guarda ·
  il caso preciso · **l'indispensabile**: i 2-4 pezzi senza cui chi guarda domani sbaglia, ognuno con l'errore che evita e il
  fatto della scheda (F…) · la **durata obiettivo** che ne viene, col motivo · la chiusura che il contenuto autorizza.
  **Un pezzo è indispensabile** se senza di lui chi guarda domani fa una cosa sbagliata davanti al componente del reel; i
  dettagli di contorno (fuso orario, permessi, software o modelli diversi) restano nella scheda e vanno in descrizione.
  **Ogni pezzo si dice con il suo appiglio**: cosa fa chi guarda (il gesto, il controllo) e, se c'è un termine che in reparto
  non si usa, cosa succede invece del numero («due metalli che scaldandosi si allungano in modo diverso, e la lamella si
  piega», non «coefficienti di dilatazione diversi»). Un pezzo che non sai dire così, a voce non regge: resta nella scheda.
  La durata parte dai pezzi, non il contrario. Riferimento: i 10 reel migliori stanno fra 48 e 56 s (è un dato, non una
  legge). Se l'indispensabile non ci sta, **non lo tagli**: lo dici a Saverio in una riga e la durata si decide con lui;
- **il discorso**: le battute numerate B1, B2…, scritte di fila, **senza secondi né clip**. È la prima consegna e si scrive
  prima di pensare al taglio;
- **il taglio**, come passo separato: tabella battuta · clip (4, 6, 8 o 10 s), una battuta per clip. Se una battuta non sta
  in 10 s, prima cerchi una ridondanza da togliere; se non c'è, la dividi in **due battute dove cambia il ragionamento**,
  mai a metà frase (Flow rigenera la voce a ogni clip). Scrivi quale ridondanza hai tolto;
- **il piano scena per scena**: mondo, set, e per ogni scena cosa si vede, dove sta il componente, cosa è acceso o spento,
  e **il gesto** del personaggio legato a una parola;
- **le note battuta per battuta**: tabella battuta · cosa fa (a quale domanda risponde) · fatto F · alternativa scartata e
  perché (es. «scarto "il termico sente la temperatura del motore": è un'altra misura»). È qui che si vedono gli assoluti e
  le eccezioni: se scarti un'eccezione, scrivi perché non cambia la decisione di chi guarda;
- il copione in `copioni/<slug>_parlato.txt` (una riga per scena, `S1: …`) e l'esito dei controlli.
A Saverio in chat: discorso + taglio + piano in forma corta e l'esito dei controlli. ⏸ Il tono lo giudica lui.

## Come si scrive (le mosse)
1. **Prima il filo e l'indispensabile, poi la prima battuta** (vedi «Cosa consegni»). Esempio di filo: «lo scatto del
   termico non ti dice il guasto: ti dice che il motore ha assorbito troppo; prima di riarmare cerchi perché». Il gancio
   promette solo quello che il corpo poi mantiene: se apre una domanda che il reel non chiude, chi guarda si sente preso in giro.
2. **Scrivi un discorso continuo, poi taglialo in scene.** Un discorso scritto tutto di fila tiene il filo; battute scritte
   una per volta diventano frasi staccate. Se poi non entra nell'obiettivo, togli ridondanze e fatti fuori
   dall'indispensabile; i pezzi restano e la voce non si accelera.
3. **Ogni battuta risponde alla domanda lasciata dalla precedente o da ciò che si vede.** Controllo pratico: fra due battute
   deve poterci stare **MA** oppure **QUINDI**; dove ci sta solo «e poi», la battuta è piatta. Controllo di taglio: togli una
   battuta; se non manca niente, era di troppo.
4. **Il termine vero insieme a cosa succede davvero**, in parole comuni: «la corrente **scalda la lamina bimetallica**, la
   lamina si piega e apre il contatto». Un paragone si usa solo se sai dire dove smette di
   valere; altrimenti si spiega il meccanismo vero, che a un pubblico di tecnici interessa di più.
5. **Il dubbio di chi guarda entra dove nascerebbe l'errore**, detto con le sue parole («Ma se lo riarmo, riparte, no?»),
   e la risposta riprende quella parola e chiude sull'effetto («Riparte, sì. E scatta di nuovo: il motivo è ancora lì»). Il dubbio
   è vero e viene dalla scheda: i finti ribaltamenti («tutto quello che sai è sbagliato») i tecnici li riconoscono e li bocciano.
6. **Porta con te chi guarda**: al tu, in prima persona di chi lavora («Apriamo il quadro», «Misuro la corrente»). Le
   proprietà del componente diventano **gesti del tecnico** che si possono vedere.
7. **Chiudi la promessa, poi una sola CTA.** Una sintesi corta e utile («Prima il perché, poi il riarmo: ecco l'ordine»),
   poi la keyword che porta a corsi o webinar, poi la tagline. La conclusione sta in piedi anche senza la CTA.
   Formule pronte in `01_Piano_Editoriale/LIBRERIA-CTA.md`; keyword riciclabili (automazione, metodo, diagnosi, plc) o una
   dedicata se sul tema si costruisce qualcosa.
8. **Il limite di un fatto si rispetta scegliendo il caso e nominandolo a voce, non elencando le eccezioni.** Se il fatto
   vale per un caso, la storia mostra quel caso e il parlato lo nomina prima della regola («Nel termico a bimetallo…»,
   «Prendiamo un sensore a tre fili…»): un limite che si vede soltanto, mentre la voce dice una regola generale, non basta.
   Le eccezioni restano nella scheda e, se servono, nella descrizione o nel canale: ogni idea in più detta a voce prende il
   posto del gesto pratico che serve domani (es. «Me lo segno: martedì la tolgo»). Un'eccezione entra a voce solo se, **nel
   caso che hai mostrato**, chi guarda senza di lei farebbe una cosa sbagliata; allora entra **intera**, con quando vale e cosa
   fare («Se il relè è sul riarmo automatico, si richiude da solo: mettilo su manuale prima di cercare la causa»). Mai a metà:
   «a volte lo fa da solo», senza dire quando, lascia chi guarda ad aspettare.
9. **Dichiara cosa è verificato e cosa no.** Se ti serve un fatto che la scheda non ha, non lo scrivi: torni a Granite, che lo
   cerca e lo aggiunge al notebook.

**Frasi intere quando si spiega.** La spiegazione si dice in frasi con soggetto e verbo, come la direbbe un collega accanto
a te: «Il PLC ha perso la memoria. La batteria tampone è morta.», non «PLC: memoria persa. Batteria: morta.». Le frasi
spezzate servono alle reazioni («Appunto. … Era accesa.», «Accesa. Va bene.»), non a spiegare: una spiegazione fatta di
etichette suona da robot e lascia a chi guarda il lavoro di riempire i buchi. Se il tempo non basta, si toglie una ridondanza o un fatto fuori dall'indispensabile, non i verbi.

**Tono.** Italiano parlato, tecnicamente esatto, divertente quando l'azione se lo guadagna (constatazione asciutta, non
battute appiccicate), semplice senza essere infantile. La semplicità sta nel concetto: un apprendimento centrale per reel, con i
suoi pezzi indispensabili, e nessun salto logico non detto.

## La storia che si vede (stessa mano, subito dopo il discorso)
1. **Un mondo per reel, e la storia ci si sposta dentro** da un set all'altro con una causa che si vede («Seguiamo il cavo
   fino al motore»). Fra due set c'è un taglio; in ogni scena c'è un set solo. Il mondo si dichiara: REALE · IBRIDO (fabbrica
   vera + ologrammi sovrapposti, mai toccati) · CONCETTUALE (dentro il componente). La fantasia sceglie il mondo; quello che
   si vede è vero: schemi, simboli, schermate, scritte di scena senza marchi.
2. **Ogni componente sta dove lo trova un manutentore**, con altezza e lato dalla scheda e da `SET-TIPO.md`. Il componente
   in scena è **già montato e al suo posto**: il personaggio al massimo fa un piccolo gesto di manutenzione (sfiora, stringe).
   Montarlo in scena chiede a Flow tre azioni in una clip e il video del 2/10 si è rotto proprio lì.
3. **Di ogni oggetto in scena si sa che lavoro fa**: cosa rileva e a che distanza, cosa comanda.
4. **Ogni scena è una situazione che si può fotografare**: si anima da un solo fotogramma, quindi ci sta **un gesto**
   legato a una parola, e il personaggio reagisce a quello che succede (un LED che si accende, un pezzo che passa).
5. **Stato dell'impianto scritto per ogni scena**: cosa è acceso e di che colore, cosa si muove. Lo stato fa la storia
   (LED spento = la domanda, LED acceso = la risposta) e deve restare coerente.
6. **Saverio approva vedendo**: la storia gli arriva come griglia storyboard al passo 5, non come tabella da leggere.

## I controlli prima di consegnare (al posto di «è scritto bene?»)
1. **Lettore fresco**: lancia Aqua Regia (`controlli/lettore-fresco.md`) con **solo il discorso**. Passa se le sue risposte
   coincidono con il filo e con l'errore plausibile della scheda. Se si perde in una battuta, riscrivi quella battuta.
2. **Verità e limiti**: lancia Damocles (`controlli/limiti.md`), un subagente nuovo che riceve **solo la scheda
   dei fatti e il discorso**. Il controllo non lo fai tu: chi ha scritto il testo ci legge quello che voleva dire. Passa se
   ogni affermazione sta nella scheda e ogni limite che serve è arrivato a voce. Una battuta col limite mancante si riscrive;
   un fatto che non è nella scheda basta a rifare.
3. **Tempo**: `python3 ~/.claude/skills/vessel/scripts/timing.py copioni/<slug>_parlato.txt --voce lipsync --obiettivo 50-55`
   (l'obiettivo del filo). Dà la clip per scena, la durata del montato (somma delle clip, CTA compresa) e i crediti. Blocca
   solo una clip oltre i 10 s. Fuori obiettivo è un avviso: togli ridondanze; se restano solo pezzi indispensabili, lo
   dici a Saverio in una riga (§ Deviazioni) e propongi la scelta (tenere la durata o dividere in due reel).
   La durata del reel uscito prima la guardi tu dopo e la dici a Saverio in una riga: non è un motivo per togliere contenuto.
Un modello che giudica «è scritto bene?» dice sempre sì: per questo i controlli fanno domande precise e il gusto resta a Saverio.

## Esempi
Leggi gli esempi in `esempi/parlato/` prima di scrivere. Servono a vedere **come** si fanno le mosse, non a copiarne le
frasi: sono su temi diversi apposta. Nessuno è sullo stesso tema del reel che stai scrivendo; se lo fosse, saltalo.
| File | Tema e forma | Cosa guardare |
|---|---|---|
| `01_induttivo-capacitivo.md` | sensori · Mister Automation fa e spiega | prova ok → prova ko → dubbio di chi guarda → risposta che riprende la parola |
| `02_profinet-nodo-perso.md` | reti · componente in prima persona | il componente ferma l'errore del tecnico; il termine vero arriva come risposta |
| `03_riparato-o-acceso.md` | mestiere · mini-storia con voci fuori campo | parola del mestiere in una scelta sotto pressione; chiusa che è una domanda |
| `05_web-server-diagnostica.md` | diagnostica · componente che rivela un trucco | il «dettaglio che ti frega» messo dove si sbaglia |
| `07_rientro-dalle-ferie.md` | stagionale · monologo comico | frasi corte, una persona in ogni frase, comicità per constatazione |
| `08_astra-pnp-e-termico.md` | il metodo di Astra su due temi nuovi (non usciti) | cosa si decide prima della prima battuta; il caso nominato a voce; le note «cosa fa · scartata» |
Gli esempi più vecchi hanno CTA e uso del voi di allora: la CTA e il tu si prendono da questa pagina.

## Mestiere che puoi superare scrivendo il motivo
6-7 scene · durata obiettivo dal filo, riferimento 48-56 s (i 10 reel migliori; il loop del mercoledì ha la sua misura) ·
una persona sola che parla per clip · battute fino a ~22 parole in 10 s. Se la storia chiede altro, una riga nel master § Deviazioni.
