# Caso 02 · «Ho perso un nodo. Tutta la rete lo sta cercando» · passo 3 · Vessel · 2026-10-05 (prova 05b)
Slot lunedì 18:30 → componente con la faccia, in panico. Protagonista: **la CPU del PLC con la faccia**, prima persona, al tu
verso il tecnico. Mister Automation c'è ma non parla (una voce sola per clip). Keyword NOME. Fonti: `esiti-2026-10-04/caso-02_fatti.md` (F1-F16).

## 1 · Prima della prima battuta
**Cosa deve saper distinguere chi guarda alla fine:** un nodo PROFINET appena sostituito che il PLC non trova **non è per
forza guasto**: il PLC lo cerca per **nome**, non per IP, e un ricambio nuovo di fabbrica il nome non ce l'ha. Si distingue
dal PC («pronto per l'assegnazione») e si rimedia dandogli il nome del progetto.

**Il caso preciso (detto a voce):** nodo di I/O PROFINET nel quadro, guasto e sostituito con uno **nuovo di fabbrica** (F2),
in un progetto **senza topologia configurata** (F11): quindi il PLC non può ridargli il nome da solo. Niente scheda di memoria (F15).

**L'indispensabile** (senza questi pezzi, domani sbaglia):
| # | Pezzo | Errore che evita | Fatti |
|---|---|---|---|
| P1 | Il PLC riconosce ogni nodo del progetto **dal nome**, non dall'IP; l'IP glielo assegna lui dopo | «È identico e gli ho messo lo stesso IP: deve andare» | F1, F3, F4 |
| P2 | Il ricambio nuovo di fabbrica **non ha nome** → il PLC non lo trova | «Stesso modello = stesso nodo» | F1, F2 |
| P3 | Non trovato ≠ guasto: il LED verde della porta dice solo che c'è il cavo; il PC dice «pronto per l'assegnazione» = il nodo c'è, manca il nome | Cambiare di nuovo il ricambio (o ordinarne un altro) credendolo guasto | F8, F9 |
| P4 | Il nome si dà dal PC: scegli il nodo **dal MAC**, lo fai lampeggiare, gli assegni **il nome del progetto** (non uno nuovo) | Nominare il nodo sbagliato, o inventare un nome che il PLC non cerca | F6, F7, F16 |
| caso | «Nel mio progetto non c'è la topologia» | Credere che un nodo senza nome non si ritrovi **mai** (errore 3 della scheda) | F11 |

**Durata obiettivo: 60-66 s.** Motivo: quattro pezzi più il caso nominato a voce, ognuno ~1 battuta da 8-10 s, più gancio e
CTA. Sta sopra il riferimento 48-56 s: P3 e P4 sono quello che il tecnico fa domani in quadro, e il caso «senza topologia»
è il limite del filo (senza, la regola detta a voce è falsa negli impianti con topologia).

**Chiusura che il contenuto autorizza:** «Nodo nuovo? Prima il nome.» — dopo aver mostrato il PLC che lo ritrova dal nome e gli
dà l'IP. Non autorizza «senza nome non lo trovi mai» (F11) né «la CPU va in STOP» (non confermato).

## 2 · Il discorso (prima stesura, di fila, senza secondi)
B1 Ho perso un nodo! Lo cerco in tutta la rete… e lui è lì: nuovo, montato al posto di quello guasto.
B2 Mi dici: «È identico, gli ho messo lo stesso IP.» Ma io i nodi non li cerco per IP: li cerco per nome.
B3 All'avvio chiamo ogni nodo del progetto col suo nome. Lo riconosco dal nome, e poi l'IP glielo assegno io.
B4 Ma questo è nuovo di fabbrica: un nome non ce l'ha. Quindi io non lo trovo.
B5 Nel mio progetto la topologia, chi è collegato a quale porta, non è configurata: quindi il nome non posso darglielo da solo.
B6 «Ma il LED della porta è verde: è guasto anche lui?» No. Quel verde ti dice solo che il cavo c'è.
B7 Collega il portatile alla rete. Il mio software lo segna «pronto per l'assegnazione»: il nodo c'è, gli manca il nome.
B8 Lo scegli dal suo indirizzo MAC, lo fai lampeggiare per essere sicuro che è lui, e gli dai il nome del progetto.
B9 Eccolo: lo riconosco e gli do l'IP. Nodo nuovo? Prima il nome, poi lo ritrovo.
B10 Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

## 3 · Il taglio
Prima misura della stesura: **88 s** (10 clip). Ridondanze tolte, nessun pezzo dell'indispensabile tolto:
- B2 + B3 dicevano due volte «per nome» («li cerco per nome» / «chiamo… col suo nome» / «lo riconosco dal nome»): resta una
  volta in B2; «l'IP glielo assegno io» si sposta nella chiusa (B8), dove si vede succedere.
- B1 «nuovo, montato al posto di quello guasto» e B4 «nuovo di fabbrica» ripetevano «nuovo»: B1 dice solo «l'hai appena cambiato».
- B4 «Quindi io non lo trovo»: lo dice già il gancio. Tolta.
- B9 «poi lo ritrovo»: lo mostra la scena. Tolto.
- B6 «anche lui» / «ti dice»: ridondanti; il dubbio diventa «allora il ricambio è guasto?» (più chiaro chi è guasto).

**Discorso dopo il taglio** (= `caso-02_parlato.txt`):
| Battuta | Clip | Testo |
|---|---:|---|
| B1 | 8 s | Ho perso un nodo! Lo cerco in tutta la rete… e lui è lì: l'hai appena cambiato. |
| B2 | 8 s | «È identico, ha lo stesso IP!» Ma io i nodi non li riconosco dall'IP: li riconosco dal nome. |
| B3 | 4 s | E uno nuovo di fabbrica un nome non ce l'ha. |
| B4 | 10 s | Nel mio progetto non c'è la topologia, la mappa di chi sta su quale porta: quindi il nome, da solo, non posso darglielo. |
| B5 | 8 s | «Il LED della porta è verde: allora il ricambio è guasto?» No. Quel verde dice solo che il cavo c'è. |
| B6 | 8 s | Collega il portatile alla rete: il mio software lo segna «pronto per l'assegnazione». Il nodo c'è, gli manca il nome. |
| B7 | 10 s | Lo scegli dal suo indirizzo MAC, lo fai lampeggiare per essere sicuro che è lui, e gli dai il nome del progetto. |
| B8 | 6 s | Eccolo: lo riconosco dal nome e gli do l'IP. Nodo nuovo? Prima il nome. |
| B9 | 8 s | Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza. |

Una battuta per clip; nessuna oltre 10 s, nessuna divisa.

## 4 · Note battuta per battuta
| B | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | Gancio del titolo, in panico: «perché non lo trova se è lì?» | F4 | «Tutta la rete lo sta cercando» alla lettera: chi cerca è il PLC, non la rete; il titolo resta come scritta di copertina |
| B2 | Dà voce all'errore 1 con le parole del tecnico e risponde riprendendo la parola «IP» | F1, F3 | «Il PLC non guarda l'IP»: troppo assoluto; il punto è *da cosa lo riconosce* |
| B3 | Quindi: perché questo non lo trova | F2 | «Nessun ricambio ha il nome»: falso, un ricambio usato può avere un nome vecchio (F2, F14); per questo «nuovo di fabbrica» |
| B4 | Nomina il caso: perché il PLC non risolve da solo | F11 | Elencare le quattro condizioni della sostituzione automatica (topologia, supporto, funzione attiva, stato di consegna): un'idea in più a voce; nel caso mostrato basta la prima per sapere che il nome va dato a mano. Le altre restano in scheda/descrizione |
| B5 | Errore 2 detto con le sue parole; il «dettaglio che ti frega» sul LED | F9 | «Il LED dice che il nodo è ok»: falso, dice solo il cavo. Scartato anche parlare dei LED di errore/bus: non confermato |
| B6 | Quindi come distingui guasto da senza nome | F8 | «Il nodo te lo dice dalle spie»: non confermato. «Il software» generico: gli stati sono della tabella di un software preciso, per questo «il **mio** software» |
| B7 | Il gesto di domani: come gli dai il nome giusto | F6, F7, F16 | «Gli dai un nome»: il PLC cerca il nome del progetto, uno nuovo non lo ritrova (F16). Scartato «cambia la scheda di memoria» (F15): non tutti i nodi l'hanno |
| B8 | Chiude la promessa sull'effetto: riconosciuto dal nome, poi l'IP | F3 | «Ora funziona tutto»: troppo; «e la linea riparte»: lo stato della linea non è nella scheda |
| B9 | CTA unica + tagline | — | Keyword riciclabile «diagnosi»: il caso dà NOME |

Scartati a voce del tutto: la porta giusta dopo la sostituzione (F13, vale solo con la sostituzione automatica, non nel nostro
caso) · l'opzione «sovrascrivi i nomi» (F14, non su tutti i controller) · «la CPU va in STOP» (non confermato) · l'IP preso
via DHCP da alcuni dispositivi (F3, limite): non cambia la decisione, il nome serve lo stesso.

MA/QUINDI: B1→B2 MA · B2→B3 QUINDI · B3→B4 MA (non può darglielo il PLC?) · B4→B5 MA · B5→B6 QUINDI · B6→B7 QUINDI · B7→B8 QUINDI.

## 5 · Piano scena per scena (forma corta)
**Mondo IBRIDO**: quadro elettrico di una linea di assemblaggio di oggi, sul lato manutenzione; ologrammi sovrapposti (impulsi
di ricerca lungo i cavi, cartellini col nome sopra i nodi), mai toccati. Linea ferma per la sostituzione, niente in moto.
**Set A** — interno del quadro, zona logica in basso su guida DIN: PLC (CPU con la faccia e logo MA), switch, tre nodi di I/O
uguali, cavi di rete RJ45 connessi ai due capi. **Set B** — davanti al quadro aperto: carrello col portatile di Mister
Automation, cavo dal portatile allo switch; il quadro resta sullo sfondo.

| S | Set | Cosa si vede · stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | PLC in panico; impulsi olografici partono lungo i cavi; sopra due nodi si accende il cartellino col nome, sopra il terzo (nuovo) resta vuoto. LED di link del nuovo verde | occhi che seguono l'impulso su «cerco» |
| S2 | A | sopra il nodo nuovo un ologramma con lo stesso IP degli altri; i cartellini-nome degli altri brillano | il PLC scuote la testa su «dall'IP» |
| S3 | A | primo piano del nodo nuovo, cartellino vuoto che lampeggia | sguardo del PLC sul nodo su «nuovo» |
| S4 | A | ologramma della mappa delle porte, grigio e vuoto, accanto al PLC | il PLC indica la mappa con lo sguardo su «non c'è» |
| S5 | A | zoom sulla porta RJ45 del nodo: LED verde acceso, cartellino ancora vuoto | sopracciglio alzato su «solo» |
| S6 | B | schermo con l'elenco dei dispositivi (senza marchi): una riga «pronto per l'assegnazione» | Mister Automation indica la riga su «pronto» |
| S7 | B | in primo piano il portatile, sullo sfondo il nodo nel quadro col LED che lampeggia; alla fine il cartellino si riempie | click su «lampeggiare», il LED risponde |
| S8 | A | l'impulso del PLC arriva al nodo, cartellino pieno, compare l'IP; tutti e tre i nodi coi nomi accesi | sorriso di sollievo su «eccolo» |
| S9 | B | PLC e Mister Automation (merch con logo completo) davanti al quadro; keyword NOME olografica | Mister Automation punta la keyword |

## 6 · Uscita del timing (sul copione dopo il taglio)
```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      17    2.5    6.8     8       12
   S2      18    2.5    7.2     8       12
   S3      10    2.5    4.0     4        7
   S4      23    2.5    9.2    10       15
   S5      20    2.5    8.0     8       12
   S6      20    2.5    8.0     8       12
   S7      22    2.5    8.8    10       15
   S8      14    2.5    5.6     6       10
   S9      12    2.5    4.8     8       12  (+2 s CTA)
  TOT     156                  70      107

─── DURATA ───
somma delle clip: 70 s + asset riusabili 0 s = 70 s di montato
controllo veloce (parole ÷ 2.0): 78 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 18 · sotto le 6 parole: 6 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 60-66 s (avviso, non blocca) ───
  ⚠️ 70 s, fuori obiettivo — o si stringe il caso (un'idea in meno, non frasi compresse) o si scrive il motivo in § Deviazioni

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 107 crediti su 9 clip
```
(La prima stesura misurava 88 s su 10 clip; la misura qui sopra è dopo il taglio.)

## Controlli non fatti in questo giro
Lettore fresco (Aqua Regia) e controllo dei limiti: non lanciati, perché la prova chiede di non aprire subagenti.

## Deviazioni
- **Durata 70 s** contro l'obiettivo 60-66 s e il riferimento 48-56 s. A Saverio direi: «Ci stanno quattro pezzi che servono
  domani (riconosce dal nome, il nuovo non ha nome, verde ≠ nome e "pronto per l'assegnazione", nome del progetto scelto dal
  MAC) più il caso "senza topologia", che è il limite del filo: sono 70 s. Per scendere sui 55 dovremmo togliere un pezzo
  intero — il più sacrificabile è il LED verde (B5, −8 s), ma è proprio l'errore di chi cambia il ricambio due volte.
  Teniamo 70 o togliamo B5?»
- **9 scene** invece di 6-7: una battuta per pezzo; B3 è una clip da 4 s perché è un solo passaggio logico (il nuovo non ha nome).
- Il titolo «Tutta la rete lo sta cercando» resta per la copertina; a voce «Lo cerco in tutta la rete», perché chi cerca è il PLC (F4).
