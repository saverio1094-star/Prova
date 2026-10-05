# Ricerca Sider Scholar — interblocco fra due linee scollegate (reel 30/9, relè d'appoggio)

> 29/9 · metodo di Saverio: **Scholar cerca → il notebook verifica → chi scrive usa solo il confermato.**
> Chat del video: https://chatgpt.com/g/g-p-6aa1cfdf0cc08191a926ff19ca967087-mr-automation-academy-creative-lab/c/6aba7f2b-7ce0-83ed-bc15-2c2f2da0f123
> Risposta di Sider arrivata il 29/9, dopo il 3º Reconnect di Saverio («Worked for 33s», più chiamate Scholar). Qui sotto la sua risposta
> **riassunta fedelmente, senza aggiunte mie**. Le URL sono quelle linkate da Sider (tolti solo i parametri `?utm_source=chatgpt.com`):
> **nessuna è stata aperta né verificata da chi scriveva** → la verifica è del notebook. Nessuna fonte è una prova finché non è caricata nel notebook.
> ⚠️ Nelle fonti compaiono marchi (ABB, Schneider, Phoenix Contact, Siemens, Rockwell, Nordson): servono alla verifica, **nel video restano vietati**.

> 🔬 **Verifica nel notebook 29/9 — fonti caricate nel Brain 2 `ae39f678`:** F3 · F4 · F5 · F8 · F10 · F11 · F12 (7). **Saltate:** F1 e F9 (schede di norme senza testo) · F6 e F14 (relè di sicurezza, non d'interfaccia) · F7 (copia su sito terzo). **Non caricabili:** F2 e F13 (forum, «pratica»): il sito blocca la lettura, 2 tentativi. Brain 1 non toccato.

## Elenco fonti (14 URL uniche)
| # | Fonte | URL | Tipo |
|---|---|---|---|
| F1 | IPC/SMEMA 9851 — Mechanical Equipment Interface Standard (scheda ANSI Webstore) | https://webstore.ansi.org/standards/ipc/ipcsmema98512007 | norma (solo scheda di vendita, testo non aperto) |
| F2 | PLCtalk — Multiple conveyor sequence start and interlock | https://www.plctalk.net/forums/threads/multiple-conveyor-sequence-start-and-interlock.109451/ | forum tecnico |
| F3 | Nordson Asymtek M-2000, manuale (ManualsLib) — sezione SMEMA | https://www.manualslib.com/manual/1781717/Nordson-Asymtek-M-2000.html | manuale produttore (copia su ManualsLib) |
| F4 | ABB — Relè di interfaccia e optoaccoppiatori | https://new.abb.com/low-voltage/it/prodotti/rele-elettronici-di-comando-e-controllo/rele-di-interfaccia-e-optoaccoppiatori | pagina prodotto produttore |
| F5 | Schneider Electric — TeSys T LTMR, Installation Guide, «Wiring: Logic Inputs» (interposing relay) | https://productinfo.se.com/tesys_t_user_guides/doca0128-tesys-t-ltmr-motor-management-controller-installation-guide/English/Tesys_T%20LTMR%20Installation%20Guide.xml/$/TPC_Wiring_LogicInputs_53457272_T001005731 | guida ufficiale produttore |
| F6 | Phoenix Contact — pagina «rele-di-accoppiamento-psr-ps20-1no-1nc-24dc» | https://www.phoenixcontact.com/it-it/prodotti/rele-di-accoppiamento-psr-ps20-1no-1nc-24dc-sc-2700356 | pagina prodotto · ⚠️ da controllare: la sigla PSR potrebbe essere un modulo di sicurezza, non un relè d'interfaccia |
| F7 | Copia PDF della specifica SMEMA (pdf.51smt.cn) | https://pdf.51smt.cn/a50dbbaa79fbd801636e478ce43b2d11 | ⚠️ copia su sito terzo, non la fonte ufficiale |
| F8 | Siemens — Safety Integrated, Function Manual (Safety-FHS-LD) | https://cache.industry.siemens.com/dl/files/017/61889017/att_101370/v1/Safety-FHS-LD-ENG_en-US.pdf | manuale ufficiale |
| F9 | ISO 13849-1:2023 (pagina ISO) | https://committee.iso.org/standard/73481.html | norma (solo scheda, testo non aperto) |
| F10 | Phoenix Contact — PLC-INTERFACE, moduli relè ultracompatti | https://www.phoenixcontact.com/it-it/prodotti/rele-e-optoaccoppiatori/rele-statici-e-rele-elettromeccanici/moduli-rele-ultracompatti | pagina prodotto produttore |
| F11 | Schneider Electric — FAQ FA23633, cablaggio PNP/NPN | https://www.se.com/uk/en/faqs/FA23633/ | FAQ ufficiale produttore |
| F12 | Rockwell Automation — Input and Output Troubleshooting Procedures | https://support.rockwellautomation.com/ci/okcsFattach/get/48906_5 | documento supporto ufficiale |
| F13 | PLCtalk — Troubleshooting PLC Inputs (articolo tecnico) | https://www.plctalk.net/technical-articles/troubleshooting-plc-inputs/ | guida tecnica / forum |
| F14 | Rockwell Guardmaster 440R — User Manual, Troubleshooting | https://literature.rockwellautomation.com/idc/groups/literature/documents/um/440r-um013_-en-p.pdf | manuale ufficiale (relè di sicurezza) |

## 1. Esempi reali e quotidiani di interblocco fra due linee/macchine con PLC diversi e nessuna rete fra loro
- **Risposta (Sider):** (a) **nastro/linea a monte → macchina a valle**: la macchina a valle dice «pronta a ricevere», quella a monte «materiale disponibile»; si avanza quando le due condizioni sono vere; lo standard IPC-SMEMA 9851 formalizza proprio questa interfaccia fra macchine. (b) **due nastri consecutivi**: ogni nastro riceve segnali tipo *upstream running / downstream running / upstream enable / downstream enable*, una catena di permessi fra macchine; documentato come pratica su una linea di movimentazione malto. (c) **macchine SMT con controllori distinti**: SMEMA usa segnali discreti fra macchine adiacenti, *Machine Ready* e *Board Available*; un manuale di manutenzione Nordson descrive il caso monte → valle e il relativo scambio.
- **Fonti:** F1 · F3 · F2
- **Solidità (Sider):** standard/manuale + forum. SMEMA molto solida; per i nastri generici il forum documenta una pratica reale, non una prescrizione.
- **🔬 Verifica nel notebook (Brain 2 `ae39f678`, 29/9): ⚠️ PARZIALE.** ✅ Il manuale SMT (F3, Lesson 15 «SMEMA Transfer», p. 171-172) conferma lo scambio fra due macchine: quella a valle, pronta ad accettare, manda un segnale che chiede il pezzo; quella a monte, se è pronta, risponde con un suo segnale. ❌ I nomi «Machine Ready / Board Available» e il contatto NA che si chiude NON sono nel testo. ❌ L'esempio dei nastri (F2 forum) non è verificato: la pagina non si carica nel Brain.

## 2. Come si chiama in campo quel relè
- **Risposta (Sider):** nei manuali il termine più solido è **«relè di interfaccia»** (in inglese **«interposing relay»**). ABB usa «relè di interfaccia» per i dispositivi che isolano e adattano segnali fra PLC e altri livelli; Schneider usa «interposing relay»; Phoenix Contact usa sia «relè di interfaccia» sia «relè di accoppiamento». **«Relè d'appoggio»** si capisce come gergo, ma **SENZA FONTE** primaria che lo stabilisca come termine tecnico. «Relè di consenso» descrive la **funzione** del segnale, non il tipo di componente.
- **Fonti:** F4 · F5 · F6 (⚠️ vedi elenco) · F10
- **Solidità (Sider):** manuali/guide ufficiali dei produttori. «Relè d'appoggio» → SENZA FONTE come denominazione standard.
- **🔬 Verifica nel notebook: ✅ APPROVATA.** «Relè di interfaccia» (F4: «isolamento elettrico, amplificazione e bilanciamento dei segnali fra… PLC… e il livello sensore/attuatore») · «interposing relay» (F5) · «interfaccia fra il controllore e le periferiche» (F10). ⚠️ «Relè di accoppiamento» dei produttori non verificato: F6 saltata perché è un relè di sicurezza. «Relè d'appoggio» = gergo di Serafino, fonte Serafino.

## 3. Il consenso passa su un contatto NA o NC, e perché
- **Risposta (Sider):** per un **semplice consenso di processo** non c'è una regola universale «deve essere NC»: si può usare un **NA che si chiude quando il consenso è presente** (esempio: in SMEMA *Machine Ready* e *Board Available* sono circuiti a contatto che si chiudono nella condizione attiva). Se invece il segnale svolge una **funzione di sicurezza**, si usa di solito un'architettura **de-energize-to-trip** con circuiti normalmente chiusi, così la perdita dell'energia di comando porta allo stato sicuro; Siemens documenta la **protezione contro la rottura del filo** con questa architettura; ISO 13849 riguarda la progettazione delle parti di comando legate alla sicurezza. Sintesi: **NA per un normale permesso**, **NC/diseccitazione quando è una funzione di sicurezza**; la scelta vera dipende da analisi dei rischi e architettura.
- **Fonti:** F7 (SMEMA, copia) · F1 · F8 · F9
- **Solidità (Sider):** standard + manuale di sicurezza + norma. Sider **sconsiglia** di usare EN 60204-1 o ISO 13849 per dire «un consenso deve essere NC»: troppo categorico.
- **🔬 Verifica nel notebook: ⚠️ PARZIALE.** ✅ Per la sicurezza (F8, manuale di sicurezza di un azionamento, §7.2): «protected against wire break, i.e. if the relay's control voltage fails then the safety function is active». ✅ Nelle schede, quando il segnale c'è la bobina si eccita e il contatto NA chiude. ❌ Nessuna fonte dà una regola «NA per il consenso di processo»: nel video non si afferma una regola NA/NC.

## 4. In quale quadro si mette il relè, A (chi dà il consenso) o B (chi lo riceve), e perché
- **Risposta (Sider):** **nessuna regola universale A o B**: dipende da cosa si vuole isolare e da quale circuito eccita la bobina. Pratica documentata: relè **nel quadro di chi riceve**, vicino al suo ingresso, quando si isola un segnale che arriva da un'altra apparecchiatura (Schneider raccomanda l'interposing relay per segnali provenienti dall'esterno del quadro, installato il più vicino possibile al controllore). Ma il relè può stare anche **nel quadro A**: il PLC A eccita la bobina e i contatti isolati viaggiano nel cavo verso B; la separazione galvanica è una delle funzioni per cui i produttori propongono questi relè. Per il nostro caso A → B, metterlo in A «è una soluzione perfettamente plausibile», va deciso dallo schema.
- **Fonti:** F5 · F4 · F10
- **Solidità (Sider):** guida tecnica dei produttori. «Sempre nel quadro A» o «sempre nel quadro B» → **SENZA FONTE** (non è una regola generale).
- **🔬 Verifica nel notebook: ⚠️ PARZIALE.** ✅ F5: relè d'interposizione «for all information on logic inputs coming from outside of the switchboard and mainly connected with long lines», per ridurre i disturbi, «installed in the switchboard as close as possible to the LTMR controller», cioè vicino a chi riceve, per quel dispositivo. ❌ «Anche nel quadro A va bene» non è nelle fonti. Il video non dice A né B: dipende dallo schema.

## 5. Chi alimenta i 24 V che corrono fra i due quadri
- **Risposta (Sider):** un **contatto pulito** non porta con sé la tensione del PLC A: è elettricamente separato. Il circuito lato B **può** quindi essere alimentato dall'alimentazione del quadro B, attraverso il contatto del relè; Schneider indica contatti *dry / free of potential* e, per mantenere l'isolamento galvanico, un'alimentazione separata. Ma **non è detto che sia sempre B**: dipende dallo schema; se A e B condividono di proposito una sorgente, il circuito può essere diverso. Con alimentazioni separate il relè evita di legare direttamente i due circuiti.
- **Fonti:** F5 · F11 · F4
- **Solidità (Sider):** guida ufficiale + documentazione produttore. Per il reel Sider suggerisce: «il contatto è pulito e il circuito del ricevitore **può** usare la propria alimentazione»; da evitare la frase assoluta «i 24 V li mette sempre il quadro B».
- **🔬 Verifica nel notebook: ✅ APPROVATA nella forma «può».** ✅ F5: «only dry contacts free of potential can be used»; gli ingressi sono «internally powered» dal controllore che riceve; la bobina va «supplied by separate power supply… to respect the galvanic isolation». ✅ Guida tecnica del relè: bobina e contatto possono stare su due sorgenti diverse. ❌ «Sempre B» non c'è: dipende dallo schema, il video non lo afferma.

## 6. I guasti più comuni che il tecnico trova su questi interblocchi
- **Risposta (Sider):** le fonti reggono una prima fascia: **cablaggio e morsetti**, **alimentazione assente**, **circuito aperto**, **chiusura del contatto non riconosciuta dall'ingresso**, **modulo relè non inserito correttamente**. Rockwell, nei troubleshooting, dice di verificare alimentazione, continuità e cablaggio quando una chiusura di contatto non viene riconosciuta; PLCtalk indica **morsetti allentati e connessioni difettose** fra i punti di guasto più frequenti. Aggiunta di Sider per due quadri: **riferimento elettrico / alimentazione del circuito ricevente sbagliati** — ma se il circuito è davvero isolato con contatto pulito e usa l'alimentazione di B, **lo 0 V non in comune non è un guasto**; lo diventa solo se lo schema richiede un riferimento comune. **Ponticelli**: dipendono dallo schema, **non** li chiamerebbe «guasto tipico» senza vedere il circuito.
- **Fonti:** F12 · F13 · F14
- **Solidità (Sider):** manuali ufficiali + guida tecnica PLCtalk. ⚠️ Nel testo di Sider non è chiaro quale fonte copra «modulo relè non inserito correttamente»: da controllare.
- **🔬 Verifica nel notebook: ⚠️ PARZIALE.** ✅ F12, tabella 10.4, «Input… does not appear to recognize a contact closure»: controllare l'alimentazione → «the continuity and wiring to the connected contact» → il LED dell'ingresso («illuminate when the user-connected device contact is closed»), e se è spento misurare tensione e corrente sull'ingresso. È il manuale di un relè di protezione motore, ma la procedura vale per un ingresso. ✅ Usura del contatto = «modalità di guasto predominante» (guida tecnica del relè). ❌ «Relè non inserito nello zoccolo» NON è nelle fonti. ❌ «Morsetti allentati» (F13 forum) non è verificato: la pagina non si carica.

## Sintesi di Sider per il reel (sua, non verificata)
La catena più solida da raccontare: **PLC A → relè d'interfaccia → contatto pulito → cavo → ingresso PLC B**. Il punto interessante non è «il relè manda i 24 V da A a B», ma che **il relè separa i due circuiti** e il contatto fa leggere il consenso al ricevitore con la sua alimentazione. L'esempio quotidiano più documentato: **macchina a monte pronta/disponibile → macchina a valle autorizzata a ricevere** (SMEMA).

## Cosa manca / da verificare (per la verifica)
- Nessuna URL aperta da chi scriveva: tutte da verificare. F1 e F9 sono solo schede di norme (il testo non c'è); F7 è una copia su sito terzo.
- F6 (Phoenix «PSR») potrebbe essere un modulo di **sicurezza**, non un relè d'interfaccia: controllare prima di usarla per la domanda 2.
- Domanda 2: **nessuna fonte per «relè d'appoggio»**, il termine che usiamo noi (se Serafino lo vuole, è gergo di reparto, non termine da manuale).
- Domanda 6: manca una fonte specifica per «relè tolto/non inserito nello zoccolo» e per «contatto sporco»; niente fonti italiane né da forum di manutentori sugli interblocchi fra due quadri.
