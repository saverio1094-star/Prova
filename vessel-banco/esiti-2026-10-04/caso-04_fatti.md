# Scheda dei fatti · «Il cavo si è rotto dentro la catena portacavi. E non è sfortuna.» · 2026-10-04 · Granite

**Filo proposto da Vessel:** un cavo che si rompe dentro una catena portacavi quasi sempre è stato scelto o posato male
(cavo non adatto al movimento continuo, raggio troppo stretto, catena troppo piena, cavi intrecciati o legati fra loro).
· **Notebook usati:** Brain `5b0396dd` · Planimetrie `d1f8acfd` · Brain 2 `ae39f678` (4 fonti caricate oggi)
· **Copertura del tema:** buona dopo la ricerca. Prima mancavano fonti di costruttori su «cavi legati fra loro», «come
è fatto un cavo per catena» e «cosa controllare»: c'erano solo blog di assemblatori di cablaggi. Resta scoperto: la
percentuale massima di riempimento della catena (vedi «Non confermato»).

**Come sono stati verificati i fatti di Brain 2:** la chat di NotebookLM oggi dava risposta vuota su tutti i notebook
(errore «No parseable chunks», 4 tentativi a 2 minuti, anche con `nlm.py`); le frasi di LAPP, HELUKABEL, igus e HELU sono
state lette parola per parola sul testo che il notebook ha importato (`notebooklm source fulltext`), quindi la citazione
c'è. Manca solo il passaggio in chat: se Vessel vuole, si ripete la domanda di verifica quando la chat torna.

> Sul filo: «catena troppo piena» regge solo detto come **cavi senza gioco intorno** (F8), non come percentuale.
> «Quasi sempre» non è nelle fonti: nessuna dà una statistica delle cause. Le fonti dicono che **queste** cause rompono
> il cavo, non quanto spesso.

## Fatti (solo questi entrano nel parlato)
| # | Fatto, per il caso delimitato | Fonte (notebook · documento · pagina o sezione) | Limite che va con il fatto | Stato |
|---|---|---|---|---|
| F1 | Il raggio di curvatura di un cavo ha tre casi: **fisso** (piegato una volta in posa, poi fermo), **flessibile** (movimento occasionale, senza carico ciclico continuo), **catena portacavi** (movimento continuo, tanti cicli): quest'ultimo chiede di più a materiali e struttura | Brain 5b0396dd · igus, *Cable with small bend radii for the tightest installation space* · «Types of bend radii for cables» | È la classificazione di un costruttore di cavi; non dice quanti cicli regge un cavo qualunque | CONFERMATO |
| F2 | Un cavo «da posa fissa» e uno in catena «non sono lo stesso prodotto»: scambiarli dà un guasto che arriva **dopo molto servizio**, come **segnale intermittente o blocco dell'azionamento**, e **mai come un filo rotto che si vede** | Planimetrie d1f8acfd · Motionwell Automation, *Electrical System Integrator Scope: Panels, Wiring, Safety* | Fonte: blog di un integratore, non di un costruttore di cavi. Il meccanismo (rottura interna) è coerente con F3-F5; ma HELU (F4) dice che il cavaturaccioli **si vede** fuori: «mai visibile» non va detto come regola | PARZIALE |
| F3 | Com'è fatto un cavo per movimento continuo: conduttori **cordati a fasci** (non a strati) con **passo di cordatura speciale**, attorno a un **centro resistente a trazione**, guaina estrusa che **riempie gli spazi**. Il cavo standard a strati, fatto senza badare a passo, verso di cordatura e riempimento centrale, sotto sforzo fa l'**effetto cavaturaccioli** → rottura delle anime | Brain 2 ae39f678 · igus, *Continuous-flex Cable Construction* | È la costruzione **igus** («in the majority of… chainflex»); HELU conferma fasci + passo corto + guaina a riempimento «often» per molti conduttori. **Limite chiave igus:** i cavi a strati «may provide sufficient support in certain short-travel applications»; il rischio cresce sopra circa 12 conduttori. Quindi: non «ogni cavo a strati si rompe», ma «nelle corse lunghe e nel movimento continuo» | CONFERMATO |
| F4 | **Cavaturaccioli** = deformazione a elica del cavo lungo il suo asse, che cresce **poco a poco in molti cicli**. Cause: passo di cordatura troppo lungo o non adatto; raggio minimo non rispettato; cavo **attorcigliato quando lo si srotola** o messo in tensione in posa | Brain 2 ae39f678 · HELUKABEL USA, *Corkscrewing in Drag Chain Cables* (FAQ) | FAQ di costruttore con accento commerciale; le cause sono elencate, non pesate; «più critiche quanto più lunga è la corsa». La deformazione esterna è **visibile** | CONFERMATO |
| F5 | Un cavo posato **attorcigliato** si danneggia nella cordatura delle anime; in funzionamento l'effetto **cresce** e diventa cavaturaccioli → **rottura delle anime** → malfunzionamenti | Brain 2 ae39f678 · LAPP, *Assembly guidelines* (T3), punto 4 | Istruzioni per cavi da catena LAPP | CONFERMATO |
| F6 | Raggio troppo stretto: rottura del cavo o dei trefoli, conducibilità ridotta, cavaturaccioli, vita più corta, fermi macchina | Brain 5b0396dd · igus, *Cable with small bend radii…* · «Why is the right bend radius so important?» | — | CONFERMATO |
| F7 | Il raggio della catena dipende dal cavo **più grosso o più rigido** che contiene e deve essere **≥ al raggio minimo dichiarato del cavo** | Brain 5b0396dd · igus, *General rules for cables and hoses in the energy chain* · «Bend radius R»; igus, *Cable with small bend radii…* · «Bend radius for energy chains»; LAPP T3 punto 1 | Il raggio minimo è quello **del costruttore del cavo**, non una regola generale | CONFERMATO |
| F8 | Ogni cavo elettrico tondo vuole **gioco libero tutto intorno di almeno il 10 % del suo diametro** (verso traversini, separatori e cavi vicini); i cavi stanno **sciolti uno accanto all'altro**, separati il più possibile da separatori | Brain 5b0396dd · igus, *General rules…* · «Clearance space»; Brain 2 · LAPP T3 punto 5; HELUKABEL *Installation manual* punto 2 | Vale per cavi elettrici; tubi pneumatici e idraulici hanno altri valori | CONFERMATO |
| F9 | Cavi e tubi non devono **mai** avere modo di aggrovigliarsi; cavi di diametri molto diversi o con guaine di materiali diversi (che si incollano) vanno separati con separatori o ripiani | Brain 5b0396dd · igus, *General rules…* · «Instructions for energy chain interior separation», «Filling rules»; Planimetrie · HIWIN *Assembly Instructions* §4.7 | — | CONFERMATO |
| F10 | **Non legare più cavi insieme**: nella **parte mobile** della catena i cavi non vanno fissati né legati fra loro; con forti accelerazioni le fascette servono poco | Brain 2 ae39f678 · LAPP T3 punto 8 (numerato «18» nel PDF) | Istruzione LAPP per i suoi cavi in catena. Le fascette restano dove il cavo si fissa alle estremità, sui pettini di sgravio (HIWIN §4.7: «strain relief combs… secured with cable ties») | CONFERMATO |
| F11 | In posa i cavi vanno **srotolati dalla bobina di lato (tangenzialmente), senza torsione**, mai tirati da sopra la bobina coricata, e **stesi dritti prima** della posa per farli distendere; la scritta sulla guaina gira a spirale per come è prodotto il cavo, quindi **non serve** a capire se il cavo è dritto | Brain 5b0396dd · igus, *General rules…* · «Filling rules, Electric round cable» punto 1; Brain 2 · LAPP T3 punto 2; HELUKABEL punto 5 | — | CONFERMATO |
| F12 | Nella curva il cavo deve correre nella **zona neutra**: niente guida forzata sul raggio interno o esterno, deve potersi muovere rispetto agli altri cavi e alla catena | Brain 2 · LAPP T3 punto 10; Planimetrie · HIWIN §4.7 («located in the neutral zone… move freely within its radius») | — | CONFERMATO |
| F13 | Dove si fissa il cavo (sgravio di trazione): igus e HIWIN → **a tutte e due le estremità** (fissa sul telaio, mobile sulla staffa del carrello); LAPP → catena **autoportante** a punto fisso e mobile, catena **strisciante** solo al punto mobile; HELUKABEL → saldamente a **un'estremità**, con gioco dall'altra | Brain 5b0396dd · igus *General rules…* («Round electrical cables must have strain relief at both ends»); Planimetrie · HIWIN §4.7; Brain 2 · LAPP T3 punti 8-9, HELUKABEL punto 8, HELU FAQ («tension relievers on both the fixed and moving ends… required») | **Le fonti non concordano**: dipende dal tipo di catena e dalle istruzioni del suo costruttore. Nel parlato: «fissato alle estremità come dice il costruttore della catena», non «sempre a tutte e due» | PARZIALE |
| F14 | Lo sgravio di trazione fa sì che le forze esterne siano prese dalla struttura su cui è montato, e sui contatti del connettore arrivino forze vicine a zero | Planimetrie · igus, *Strain relief cable* · «How does a strain relief work?» | — | CONFERMATO |
| F15 | Se il cavo è fissato **troppo vicino** all'estremità mobile, la piega si sposta dentro il connettore o lo sgravio | Planimetrie · *Robot Cable Carrier Fill Ratio and Separator Guide* · «Bend radius is not separate from fill ratio» | Blog di assemblatore di cablaggi. La distanza giusta da costruttore è in F16 | PARZIALE |
| F16 | Fra la fine della curva e il punto fisso si raccomanda una distanza di **10-30 volte il diametro del cavo** «per la maggior parte dei cavi»; i cavi chainflex igus possono essere fissati direttamente sulla staffa | Brain 5b0396dd · igus, *General rules…* · «Filling rules, Electric round cable» | «For most cables», consiglio igus; non vale per cavi testati per il fissaggio in staffa | CONFERMATO |
| F17 | Peso dei cavi distribuito **simmetricamente** sulla larghezza; cavi **più grossi e pesanti ai lati**, leggeri al centro; niente cavi sovrapposti senza ripiano | Brain 5b0396dd · igus *General rules…* (solo «symmetrically distributed»); Brain 2 · LAPP T3 punto 6, HELUKABEL punto 8 | igus dice solo «simmetrico»; «pesanti ai lati» è LAPP e HELUKABEL | CONFERMATO |
| F18 | Controlli: LAPP raccomanda ispezioni **ogni tre mesi nel primo anno**, poi a ogni intervallo di manutenzione, per verificare che i cavi **si muovano completamente liberi nella curva**; nelle prime ore il cavo si allunga, la catena no, quindi la posizione va ricontrollata e se serve ri-regolata | Brain 2 · LAPP T3 punto 12 | Raccomandazione LAPP per i suoi cavi in catena | CONFERMATO |
| F19 | Se un cavo in funzionamento si attorciglia lungo l'asse, lo si ruota **gradualmente** a uno dei punti di fissaggio finché scorre liscio | Brain 2 · LAPP T3 punto 11 | — | CONFERMATO |
| F20 | «Controllare i cavi di collegamento a intervalli regolari; se sono danneggiati, sostituirli» | Planimetrie · SEW-Eurodrive, *MOVIMOT advanced DAC*, §13.3.5 | Detto per i cavi di quel motoriduttore, non per la catena in generale | CONFERMATO |
| F21 | Se il cliente posa i cavi male, il movimento continuo dentro la catena può causare **sfregamento** fino a scoprire i punti di contatto elettrici | Planimetrie · HIWIN *Assembly Instructions* §8.6 «Visual examination of electrical componentry» | Detto per gli assi lineari HIWIN | CONFERMATO |
| F22 | Le classi dei conduttori: **classe 5** = rame a trefoli flessibile (collegamento a parti in movimento); **classe 6** = più flessibile della 5, per **movimenti frequenti** | Planimetrie · *BSI Standards Publication* (EN/IEC 60204-1), Tabella D.4 | Copia della norma su sito terzo (Nobelcert): il contenuto va ricontrollato sul testo ufficiale prima di citarne il numero in video | PARZIALE |

## Numeri confermati
- **10 % del diametro** — gioco minimo tutto intorno a ogni cavo elettrico tondo nella catena — igus *General rules…* (Brain 5b0396dd, 2026-10-04); stesso valore in LAPP T3 punto 5 e HELUKABEL punto 2 (Brain 2).
- **10 × diametro** — raggio minimo «regola semplice» (cavo da 10 mm → 100 mm) — igus *Cable with small bend radii…*, «Calculating bend radius». Limite della fonte: «can vary depending on application, material and standard»; il valore vero è quello dichiarato dal costruttore del cavo. Per un reel di manutenzione meglio dire «il raggio minimo scritto sulla scheda del cavo» che il 10×.
- **10-30 × diametro** — distanza fra fine della curva e punto fisso «per la maggior parte dei cavi» — igus *General rules…*.
- **almeno 10 % di lunghezza in più** — scorta di cavo per posarlo senza torsione in catena — HELUKABEL *Installation manual* punto 5 (Brain 2).
- **non sotto +5 °C** — temperatura del cavo durante la posa — LAPP T3 punto 3 (Brain 2); vale per quei cavi LAPP.
- **oltre 25 anime** — LAPP e HELUKABEL consigliano, se possibile, di dividere i conduttori su più cavi invece di un cavo a più strati — LAPP T3 punto 1, HELUKABEL punto 8.
- **ogni 3 mesi nel primo anno** — ispezione della posizione dei cavi in catena — LAPP T3 punto 12 (Brain 2).

## Termini veri
- **catena portacavi** (energy chain, drag chain, cable carrier) — la catena a maglie che porta cavi e tubi fra una parte fissa e una mobile della macchina (nel video senza marchio: «catena portacavi»; «e-chain» è un marchio igus).
- **cavo per posa mobile / per catena** (continuous-flex, drag chain cable) — cavo costruito per il movimento continuo con molti cicli (nel video: «cavo per catena» o «cavo per posa mobile»; niente «chainflex», «ÖLFLEX FD», «HELUCHAIN»).
- **raggio minimo di curvatura** — il raggio sotto cui il costruttore dice di non piegare il cavo; per la catena si guarda quello dinamico.
- **effetto cavaturaccioli** (corkscrewing) — deformazione a elica del cavo lungo l'asse, segnale che dentro le anime si stanno rompendo.
- **sgravio di trazione** (strain relief) — il fissaggio del cavo alle estremità della catena (pettine con fascette o morsetto) che scarica le forze sulla struttura.
- **separatore / ripiano** (separator, shelf) — divisori verticali e orizzontali dentro la catena che tengono i cavi in corsie.
- **zona neutra** — la linea a metà della curva dove il cavo non è né tirato né compresso.
- **cordatura a fasci / a strati** (bundle / layer stranding) — come sono avvolti i conduttori dentro il cavo.

## Errore plausibile di chi guarda
0. «Ho messo un cavo **flessibile**, quindi va bene in catena» → igus: molti cavi «flessibili» sono costruiti a strati,
   costano meno, e nelle corse lunghe o nel movimento continuo fanno il cavaturaccioli (F3). Flessibile non vuol dire
   «per catena»: conta che il costruttore lo dichiari per movimento continuo in catena, con il suo raggio minimo (F1, F7).
1. «Il cavo è nuovo e della sezione giusta, quindi va bene» → un cavo da posa fissa in catena si rompe dentro dopo molti
   cicli, senza segni fuori (F1, F2, F3). Il dubbio del parlato: **non basta che sia della sezione giusta, deve essere fatto
   per il movimento continuo**.
2. «Metto una fascetta per tenere in ordine i cavi nella catena» → nella parte mobile i cavi non si legano fra loro (F10);
   le fascette stanno solo sul pettine di fissaggio alle estremità.
3. «Srotolo il cavo nuovo tirandolo dalla bobina e lo infilo» → se entra attorcigliato, la torsione cresce col movimento
   fino al cavaturaccioli (F5, F11). La scritta sulla guaina non dice se è dritto (F11).
4. «Lo fisso tutte e due le estremità, sempre» → dipende dal tipo di catena e dal suo costruttore (F13).

## Dove sta davvero il componente
Sulla **macchina**, sull'asse che si muove: la catena va da un **punto fisso** sul telaio (lato da cui arrivano i cavi dal
quadro) a una **staffa sul carrello** mobile (asse lineare, portale, settimo asse del robot). Il ramo superiore è
autoportante, il ramo inferiore **corre appoggiato su una superficie/canalina di appoggio** mentre si srotola (HIWIN §4.7).
Altezza e lato: **non dati dalle fonti**, dipendono dall'asse. Cosa ha intorno: il carrello e il servomotore sull'asse;
dentro la catena cavi di potenza del servo, cavo encoder, eventuali tubi pneumatici, divisi da separatori.
Cavo: **dal quadro (drive del servo) → canalina → punto fisso della catena → catena → staffa del carrello → servomotore**
(SET-TIPO §0-bis, riga «Servomotore»; Planimetrie · *Field-Level Physical Integration…* «Dynamic Cable Routing and Energy
Chain Engineering»: cavi lungo il telaio dentro la catena).
Com'è fatto (per il disegno): maglie con traversini; separatori dentro (HIWIN: un divisorio ogni seconda maglia); ai due
capi una staffa di attacco con **pettine di sgravio** su cui i cavi sono stretti con fascette o morsetti; nella curva i
cavi stanno sciolti, uno accanto all'altro, con gioco. Nessuna pagina di disegno d'ingombro cercata (non c'è un prodotto
specifico in scena).

## Non confermato — il parlato non lo usa
- **«Quasi sempre» è colpa di scelta/posa** — nessuna fonte dà una statistica delle cause di rottura. Dire «queste sono le
  cause tipiche», non «quasi sempre».
- **Riempimento massimo della catena al 60 % della sezione** — c'è solo in un blog di assemblatore di cablaggi (*Robot
  Cable Carrier Fill Ratio…*, «unless the carrier maker approves more») e in una sintesi senza costruttore (*Field-Level
  Physical Integration…*). Il Brain igus dice esplicitamente che una percentuale massima complessiva **non** c'è; c'è solo
  il gioco del 10 % per cavo (F8). Il manuale Tsubaki Kabelschlepp non è stato letto (PDF troppo grande).
- **Classe dei trefoli 1-2 per i cavi fissi** — detto dal notebook Planimetrie senza frase testuale di costruttore.
- **Punti di rottura più frequenti (uscita, sgravio, curva)** — solo da blog di assemblatore (FPIC, *Robot Drag Chain Cable
  Assembly: Common Failure Points…*); la parte «piega che finisce nel connettore» resta PARZIALE (F15).
- **Checklist di sostituzione completa** (pinout, continuità in movimento, ecc.) — solo da blog di assemblatore (*Robot Dress
  Pack Cable Routing…*). Le fonti di costruttori coprono: cavo adatto (F1, F3), raggio (F7), srotolare senza torsione
  (F11), gioco e separatori (F8-F9), non legare (F10), zona neutra (F12), fissaggio secondo il costruttore della catena
  (F13), ricontrollo nelle prime ore e ispezioni (F18).
- **Un filo rotto può bucare l'isolamento di altri conduttori e causare cortocircuiti o incendi** — è nella HELU FAQ (Brain 2,
  «Consequences of a Corkscrew»), quindi è confermato, ma il parlato non lo usa: tono da panico, fuori dallo slot.

## Aggiunto ai notebook oggi
- LAPP, *Assembly guidelines* T3 → Brain 2 `ae39f678` (https://imager.lapp.com/e/lapp/r8KwQSJD1erl7Jknjqb6_w~~/T3_Assembly_guidelines_int.pdf) · id c1b0ac8d
- HELUKABEL, *Installation manual — Cable installation in drag chains* → Brain 2 `ae39f678` (https://assets-cdn.helukabel.com/suppliers/Helukabel/documents/ma/Installation-Guide-Drag-Chains.pdf) · id cea5bbac
- igus, *Continuous-flex Cable Construction* → Brain 2 `ae39f678` (https://www.igus.com/company/unharnessed-cables-chainflex-construction-ca) · id 953c066a
- HELUKABEL USA, *Corkscrewing in Drag Chain Cables* → Brain 2 `ae39f678` (https://www.helu.com/us-en/newsroom/item/faq-corkscrewing-drag-chain-cables.html) · id af5a973e
- Tabella delle fonti: `banco-di-prova/esiti-2026-10-04/caso-04_ricerca.md`
