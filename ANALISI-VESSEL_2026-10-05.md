# Vessel al 5/10 — i difetti, uno per uno

Fonti lette per intero: il nuovo dossier Vessel del 5/10 (skill, banco di prova, i tre giri del 5/10), il dossier del 4/10,
il dossier di Vincent (1/10) e il METODO di Astra. Le citazioni fra «» sono prese dai file.

---

## 0 · Il verdetto in breve

La struttura regge: una sola mano che scrive, 6 invarianti, master corto, un fotogramma per clip, componente già montato,
archivio in 4 righe. **Ma ci sono tre problemi grossi:**

1. **Il loop sta ricominciando.** In 48 ore ci sono stati 4 giri di banco e almeno 8 regole nuove scritte direttamente nelle
   pagine. Il quaderno è a 0/10 e non è uscito nessun reel. Le immagini e Flow, cioè proprio dove Vincent si è rotto, non sono
   mai stati provati.
2. **La conoscenza più preziosa della vecchia skill non è entrata.** Le 18 correzioni di Saverio sulla voce (`VOCE-SERAFINO.md`)
   non le legge nessuno, e in alcuni punti la skill nuova dice il contrario.
3. **Del metodo di Astra è entrata soprattutto la parte che allunga.** Più carte da compilare, più pezzi, più secondi. Il
   caso 01 è arrivato a 68 s e 10 scene, mentre la v4 approvata diceva le stesse cose in 52 s e 7 scene. In più `timing.py` ha perso il
   margine che Vincent imponeva, quindi i 56 s dichiarati sono in realtà circa 64.

---

## 1 · Le tre critiche di Gemini

| # | Critica | Verdetto | Perché |
|---|---|---|---|
| 1 | Data leakage: casi 01 e 02 in `esempi/parlato/` | **Giusta, ma il problema è più grosso e la cura proposta non basta** | Anche `05_web-server-diagnostica.md` è il bersaglio del caso 03, e Gemini non l'ha visto. Soprattutto, la cartella `banco-di-prova/bersagli/`, con le risposte, sta **dentro** la skill. Una cartella `esempi/nascosti/` dentro la skill resta leggibile da qualsiasi subagente con Read/Glob: è sempre un «non guardare», solo spostato. La cura vera è nel § 3, punto M7. Va detto anche che il COLLAUDO-05 scrive «il caso 01 torna cieco davvero», ma l'esempio 01 è la v4 parola per parola e il dossier non dice se la copia di prova l'avesse tolto. Quell'affermazione non si può verificare. |
| 2 | Passo 4 senza esecutore | **Giusta** | Il dossier stesso lo ammette (cap. 3: «la sua pagina non dice chi lo esegue»). Euclid è la scelta giusta perché lavora già in ChatGPT. Conviene però farne il **giro 0 della pagina 5**, nella stessa chat del reel, invece di tenere una pagina a parte. Va anche scritto che un subagente non può aspettare Saverio: genera, torna, e la scelta la mostra Vessel. |
| 3 | Granite dipende da Vessel per Sider, serve WebSearch/WebFetch | **Già fatto per la maggior parte** | `fasi/2-verita.md` dice già: «Strumenti: WebSearch/WebFetch, oppure Sider Scholar dentro ChatGPT se Vessel te lo chiede». Il problema vero è un altro: Sider richiede Saverio, che il 29/9 ha dovuto cliccare «Reconnect» tre volte. Questo contraddice «dopo la scelta del titolo Vessel va dritto fino al parlato». Inoltre Sider Scholar cerca articoli scientifici («Search 350M+ Paper»), mentre a Granite servono manuali e FAQ dei costruttori. Cura: Granite usa **solo** WebSearch/WebFetch, e Sider si usa solo se lo chiede Saverio. |

**Sull'offerta di Gemini** («procedo io ad applicare le correzioni ai file master… poi lanciamo il giro di prova sui tre casi»):
- **Non fate modificare a Gemini i file della skill mentre ci lavora anche Claude.** Due editor sulla stessa cartella producono
  copie che divergono. È già successo con il COLLAUDO, finito in due copie (nota 2 del dossier del 4/10). Un editor solo, e un backup prima.
- **Il «giro di prova sui tre casi» è proprio il loop** (§ 2, G1). Prima viene il reel vero.

---

## 2 · Difetti gravi

### G1 — La skill sta già violando la sua regola principale

La regola, in `SKILL.md`: «una correzione scritta direttamente in una pagina è una voce del quaderno senza contatore».

Cosa è successo il 5/10:
- la mossa 8 è stata riscritta tre volte;
- in pagina 3 sono entrati «un pezzo è indispensabile se…», «ogni pezzo si dice con il suo appiglio» e «frasi intere quando si spiega»;
- è stato aggiunto un nuovo aiutante (Damocles);
- in `fasi/2` è entrato «l'errore plausibile anche nel gesto pratico»;
- `timing.py` è stato cambiato.

Tutte queste regole sono nelle pagine, e il quaderno è ancora **0/10**. Ogni giro di banco trova un difetto su un caso finto e
aggiunge una regola. È lo stesso meccanismo che ha portato Vincent a 70.000 parole, solo con il nome «banco di prova».

**Cura:** si congela la skill. Niente più giri di banco finché non esce un reel vero, e da quel momento le modifiche
arrivano solo dalle correzioni di Saverio sui reel veri.

### G2 — Il banco misura soprattutto rumore, e la versione finale non è stata controllata

- **Un tentativo per caso**, giudicato da **un solo** lettore LLM, senza sapere quanto due lettori possano dare risposte diverse. Una
  risposta sola («si perde su "permittività"») ha prodotto una regola nuova. Il COLLAUDO-05 stesso scrive «statistica debole», e la skill è stata
  adottata lo stesso.
- **La versione finale (giro 05c) non è mai passata dai suoi due controlli.** Nei tre testi c'è scritto «Lettore fresco e
  controllo dei limiti: non lanciati, il giro di prova vieta i subagenti».
- Nel caso 02 finale c'è di nuovo la frase sulla topologia: «E qui non posso darglielo io: il progetto non dice a quale porta è
  attaccato». È proprio quella che, secondo il COLLAUDO, «in 3 versioni su 5 crea un attimo di confusione», e il lettore non è
  stato lanciato. Il criterio scritto prima («il lettore non dice "aspetterei"») non è stato controllato.
- **Il tono, cioè il motivo per cui avete buttato Vincent, non è stato misurato.** Il test alla cieca è pronto
  (`esiti-2026-10-05c/TONO-alla-cieca.md`) ma nel dossier non c'è nessuna scelta di Saverio.
- Le condizioni del banco non sono quelle della produzione. Nel banco lo scrittore è un subagente fresco che non apre
  `LIBRERIA-CTA.md` né `SET-TIPO.md`. In produzione scrive il thread principale, con tutto il contesto, e può aprire qualsiasi file
  della cartella, bersagli compresi.

**Cura:** Saverio fa il tono alla cieca già pronto (10 minuti). È l'unica misura che manca sul problema che vi blocca
da mesi. Per il resto si dichiara la skill «non collaudata su immagini e Flow» e la giudica il primo reel. Se in futuro
riusate il banco, prima fate leggere **lo stesso testo** a 3 lettori freschi, per vedere quanto sono d'accordo fra loro, e solo dopo
fidatevi di un lettore solo.

### G3 — Le correzioni di Saverio sulla voce sono sparite

Il quaderno parte vuoto con questa motivazione: «Le lezioni di settembre sono già scritte nelle pagine dei passi». Per la
voce non è vero. `VOCE-SERAFINO.md` non è citato da nessuna pagina che serve a scrivere: compare solo come fonte nei file dei
bersagli. Ecco cosa manca, o viene contraddetto:

| Correzione di Saverio (VOCE §) | Cosa fa Vessel | Prova |
|---|---|---|
| **2.1** — le parole d'atteggiamento («e finisce che», «poi scopri che») sono la voce: quando si taglia per il timing si tagliano dati e ripetizioni, **mai loro** | Il nuovo passo «taglio» dice di togliere «ridondanze», senza proteggerle | Nei giri 05c: tolto «e» prima di «il LED resta spento»; tolto «Quindi ti basta un browser» |
| **2.6** — chiusura = payoff che riaggancia l'hook, **mai aforisma** | La mossa 7 dà come modello uno slogan: «Prima il perché, poi il riarmo: ecco l'ordine» | Chiuse finali: «L'ora, non la riga.» · «Stesso modello non basta: serve lo stesso nome.» |
| **2.4** — il nome della cosa entro 8 s | Non c'è in pagina 3 (c'è solo nella descrizione dell'esempio 05) | — |
| **2.11** — lo script di Serafino non si riscrive | Non c'è nessuna regola per quando Serafino porta un suo script | Il caso 01 è proprio questo, e Vessel lo riscrive |
| **2.14** — v1/v2 «robotico»; passa la v3 con *un'altra persona dentro, l'errore vissuto e la reazione*. «Si possono rispettare tutte le regole e suonare comunque da macchina» | Il mestiere dice «una persona sola che parla per clip». L'ingrediente «il momento: chi mette fretta» del manuale di Vincent (14.1) è sparito | Gli output dei giri sono quasi tutti monologhi |
| **2.10 contro 2.17** — «≤20 parole: lo stile non giustifica la lunghezza» contro «priorità alla qualità, non al tempo» | «battute fino a ~22 parole in 10 s», senza dire quale delle due vince | — |

Inoltre il notebook Reddit (le parole vere dei tecnici) e `VOCE-MANUTENTORI.md` si usano solo per i titoli, mai al momento di
scrivere il parlato.

**Cura:** è esattamente il metodo che hai descritto, cioè rispondere alle domande dello scheletro con quello che funzionava. Riempite il quaderno
con 6-8 di queste correzioni in forma ⛔ prima → ✅ dopo, **con le parole vere di Saverio**. Vengono da reel veri, approvati o
bocciati da lui, e valgono più di qualsiasi giro di banco. In pagina 3 basta una riga: «il taglio non tocca le parole
d'atteggiamento; la chiusa riaggancia l'apertura».

### G4 — Il metodo di Astra è stato preso al livello sbagliato

Leggendo il METODO di Astra con attenzione:
- Le note battuta per battuta, dice lei, «sono una valutazione del risultato leggibile, **non una trascrizione del
  ragionamento interno**». Le ha scritte perché le avete chiesto di spiegare il metodo, non sono il suo modo di lavorare. Vessel le ha rese un
  **passo obbligatorio di produzione**.
- Nel suo sistema la durata la decide **un'analisi approvata prima di scrivere** (cita `global.json`: «L'analisi
  determina e motiva la durata… Story e regia adeguano testo, beat, scene e ritmo al budget approvato»). In Vessel la decide
  chi scrive, che poi chiede a Saverio. Il risultato è una fermata in più, a parlato già scritto.
- Sulla voce dice: «Non posso certificare che ogni frase nuova sia una frase che diresti tu… **non lo so**». Astra porta
  correttezza e struttura, non la voce di Serafino. La voce sta in VOCE-SERAFINO, che è stato lasciato fuori (G3).
- I suoi budget sono 70-100 s. Importando il suo metodo è entrata anche la sua lunghezza (G5).

Effetto pratico: per ogni caso lo scrittore produce circa 130 righe (indispensabile, discorso, taglio, note, piano,
controlli, deviazioni). La v4 è nata in un passaggio solo. Quello che l'ha fatta vincere sono **le mosse**: domanda che dice a cosa
serve, meccanismo vero in parole comuni, prova ok → prova ko → obiezione, risposta che riprende la parola, «seguiamo», il gesto,
chiusa in tre parole (VOCE §2.18). Queste mosse sono già nella pagina 3.

**Cura:** «prima della prima battuta» si riduce a 4 righe (cosa distingue · il caso · **massimo 3** pezzi · durata). Le note
battuta per battuta diventano facoltative, solo per le battute dove si è tolto un assoluto o un'eccezione.

### G5 — Durata: crescita strutturale e `timing.py` senza margine

**La crescita.** «L'indispensabile non si taglia» + «la durata parte dai pezzi» + «2-4 pezzi» spingono verso reel sempre più lunghi, e
niente nella skill li comprime.
- Caso 01: v4 approvata 52 s e 7 scene → Vessel 60 → **68 s, 10 scene, 107 crediti**.
- La v4 dice la regolazione in una frase; Vessel ci mette due battute più la sintesi.
- Il COLLAUDO-05 lo scrive al punto 1 di «resta aperto» e lo lascia lì.

**Il margine perso.** In `timing.py` la funzione `taglio()` usa `secondi <= t`: 15 parole a 2,5 parole/s = 6,0 s → clip da 6 s,
**margine zero**. Vincent aveva una regola diversa (prompt di Pneuma, 14.6): «15 parole = 6 s di parlato ⇒ clip da 8 s». A questo si aggiungono
due contraddizioni dentro Vessel:
- `lock-flow.md` chiede in ogni clip un ultimo tratto «NO WORDS — …, mouth closed», che a margine zero non ha spazio;
- `fasi/6` dice «se una battuta sta a margine zero: `delivery` svelto», cioè voce accelerata, quella che Saverio ha bocciato in §2.17.

Nel caso 02 finale ci sono 4 clip su 8 a margine zero, e il «controllo veloce» dello script stesso dà **64 s** invece dei 56
dichiarati. Anche la v4, in produzione, ha dovuto portare S6 da 8 a 10 s.

**Cura:**
- In `timing.py`, margine minimo di circa 1 s: la clip è lo scalino sopra `secondi + 1`.
- Massimo 3 pezzi. Se ne servono 4, il tema si divide **al passo 1**, quando si propongono i titoli, non a parlato già scritto.

---

## 3 · Difetti medi

- **M1 — Saverio ha chiesto di vedere, non di leggere.** Vincent, 15.2: «più che leggere quello che ci mandi, vogliamo
  **vedere**». Al passo 3 Vessel gli manda comunque discorso, taglio, piano e controlli. **Cura:** a Saverio va solo il discorso
  (7-8 righe), più una riga di filo e la durata. Il piano scena per scena va dritto alla griglia.
- **M2 — Manca lo stop se il titolo promette una cosa falsa.** Caso 04: «il "quasi sempre" del titolo non è confermato». La skill
  però dice «va dritto fino al parlato». **Cura:** se la scheda smentisce o non conferma la promessa del titolo, Vessel si ferma con una
  riga e propone un titolo corretto.
- **M3 — L'invariante 1 è più severa di ciò che Saverio ha approvato.** Damocles segnala come «non nella scheda» il «campo
  elettrico» della v4: con le regole di Vessel il testo d'oro sarebbe «DA RIFARE». Il conflitto fra verità e parlato (contraddizione
  n. 11 di Vincent) resta senza proprietario quando la frase viene da Saverio o Serafino. **Cura:** una frase di Saverio o Serafino la
  verifica Granite. Se è falsa, Vessel lo dice in una riga e decide Saverio.
- **M4 — Il quaderno è difficile da usare.** Il contatore «aiutato/sviato» è un'autovalutazione, e la skill stessa scrive «un modello che
  giudica "è scritto bene?" dice sempre sì». Inoltre ogni voce nuova richiede un giro di banco (≥2 casi rigenerati), quindi le correzioni finiscono
  nelle pagine. È già successo (G1). **Cura:** il contatore si muove solo quando Saverio reagisce. Una sua correzione esplicita su un
  reel vero entra subito. Il banco serve solo a decidere cosa togliere o fondere.
- **M5 — Archivio ed esempi si contraddicono.** `fasi/8` dice: «se nella cartella ce n'è già uno della stessa forma, il nuovo prende il suo
  posto». Questo è un cambio di esempio senza prova, mentre `LEGGIMI.md` dice che anche «un esempio cambiato» va provato prima.
- **M6 — Euclid e Hypnosis non sono mai stati provati dal vivo**, ed è lì che Vincent si è rotto. In più nessuna delle due pagine dice
  cosa fare se il subagente resta bloccato a metà (login, Reconnect, upload fallito): non può chiedere a Saverio. **Cura:** in caso di blocco
  il subagente torna con il link della chat, i file già salvati e il punto a cui era. Il primo reel vero fa da collaudo delle pagine 5 e 6.
- **M7 — Il banco vive dentro la skill.** Il dossier pesa 578 KB, quasi tutti di banco. `bersagli/` ed esiti vecchi sono a un Glob di
  distanza sia per gli scrittori del banco sia per Vessel in produzione. **Cura:** il banco va fuori da
  `~/.claude/skills/vessel/` (per esempio in `~/vessel-banco/`), e ogni giro si fa su una copia della skill da cui sono stati tolti gli
  esempi del caso. Questo risolve anche la critica 1 di Gemini.
- **M8 — Il lettore fresco rappresenta un solo livello di pubblico.** Aqua Regia è un manutentore di 35 anni, ma il pubblico dichiarato include
  «chi entra nel settore», e il test di Vincent chiedeva anche «un principiante capisce ogni termine?». **Cura:** a reel alterni,
  un lettore principiante.

---

## 4 · Difetti piccoli

- **Polo o maglietta.** `fasi/4` dice «polo nera MA», `modelli/chatgpt.md` «maglietta nera», `lock-flow.md` «black MA t-shirt». Era già segnalato
  il 4/10 ed è ancora lì. La skill stessa dice che un aggettivo diverso cambia il personaggio.
- **NotebookLM.** Dal 4/10 alle 21:42 la chat dei notebook risponde vuota, e la domanda fissa di Granite («Verifica punto per punto…») dipende
  da quella chat. Prima del prossimo reel va controllato con `notebooklm auth check --test` e una domanda di prova.
- **Due fonti di verità per l'uscita dei reel.** `ARCHIVIO-CONTENUTI.md` e `VOCE-SERAFINO.md` §4 non sono d'accordo (bersaglio 02). Non è un difetto della skill,
  ma l'archivio a 4 righe funziona solo se c'è un posto solo.

---

## 5 · Cosa funziona e va tenuto

- Una mano sola per storia e parlato: il motivo è giusto, e la v4 ne è la prova.
- 6 invarianti bloccanti, tutto il resto è «mestiere» superabile scrivendo il motivo in § Deviazioni.
- Un fotogramma per clip, Fine vuoto, un gesto e un evento: viene dritto dal fallimento del 30/9.
- Componente già montato, stato dell'impianto scritto per ogni scena, griglia approvata guardandola.
- Archivio in 4 righe, master sotto le 150 righe.
- Criteri scritti prima del giro e la sezione «resta aperto» onesta.
- Damocles separato da chi scrive: l'idea è buona, ma va usato in produzione, non per fare altri giri di banco.

---

## 6 · Cosa fare adesso, in ordine

1. **Congelare la skill.** Niente più giri di banco.
2. **Correzioni piccole, in una sessione, con un editor solo e un backup prima:**
   - riempire il quaderno con 6-8 correzioni di VOCE-SERAFINO (G3);
   - aggiungere 1 s di margine in `timing.py` e togliere «delivery svelto» da `fasi/6` (G5);
   - massimo 3 pezzi; se ne servono di più si divide al passo 1 (G5);
   - ridurre «prima della prima battuta» a 4 righe e rendere facoltative le note battuta per battuta (G4);
   - passo 4 → Euclid, giro 0 della pagina 5 (Gemini 2);
   - Granite solo con WebSearch/WebFetch, Sider solo su richiesta di Saverio (Gemini 3);
   - stop se il titolo promette una cosa non confermata (M2), regola per gli script di Saverio e Serafino (M3);
   - al passo 3, a Saverio solo il discorso (M1);
   - polo o maglietta: sceglierne una (§ 4).
3. **Saverio fa il tono alla cieca** già pronto in `esiti-2026-10-05c/TONO-alla-cieca.md` (10 minuti).
4. **Un reel vero, dall'inizio alla fine**, con immagini e Flow. È il collaudo che manca.
5. **Ogni correzione di Saverio va nel quaderno con le sue parole.** Il banco, se lo tenete, serve solo a togliere voci, e va spostato fuori dalla
   cartella della skill (M7).
