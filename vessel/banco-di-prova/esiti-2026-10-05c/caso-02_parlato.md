# Caso 02 · «Ho perso un nodo. Tutta la rete lo sta cercando» · passo 3 · Vessel · 5/10/2026
Slot lunedì 18:30 → componente con la faccia, in panico · keyword NOME · scheda: `esiti-2026-10-04/caso-02_fatti.md`
Parla il PLC con la faccia (prima persona, al tu verso chi guarda). Mister Automation è in scena, muto: fa i gesti.

## 1 · Prima della prima battuta

**Cosa deve saper distinguere chi guarda:** un nodo identico, col cavo attaccato e il LED verde, che il PLC non trova
**non è guasto: è senza nome**. Il PLC i nodi li cerca per nome, non per IP.

**Filo in una riga:** «Il PLC riconosce il nodo dal nome e l'IP glielo dà lui; un ricambio nuovo di fabbrica il nome non ce
l'ha, quindi non lo trova. Dal PC vedi che c'è, scegli quello giusto e gli scarichi il nome del progetto.»

**Il caso preciso:** nodo di I/O PROFINET nel quadro, su guida DIN in basso vicino al PLC, cavo RJ45 (scheda, «Dove sta»,
caso confermato) · sostituito con uno **identico e nuovo di fabbrica** (F2) · in un progetto dove **non è scritto a quale porta
è collegato ogni nodo** (topologia non configurata), quindi il PLC non può dargli il nome da solo (F11). Il caso si nomina a
voce in B4, prima del gesto: così la regola non suona come «un nodo nuovo non viene mai trovato» (errore 3 della scheda).

**L'indispensabile (3 pezzi + il caso nominato):**
| # | Pezzo, con il suo appiglio | Errore che evita domani davanti al quadro | Fatti |
|---|---|---|---|
| 1 | Il PLC cerca i nodi **per nome, non per IP**; uno nuovo di fabbrica il nome non ce l'ha. Appiglio: il LED verde della porta dice solo che il cavo c'è. | Rimettere a mano lo stesso IP e aspettarsi che riparta; fidarsi del LED verde | F1, F2, F3, F4, F9 |
| 2 | **Senza nome non vuol dire guasto**: col PC lo vedi, c'è col suo indirizzo MAC ma senza nome. Appiglio: il gesto di aprire il PC e guardare. | Pensare che anche il ricambio sia guasto e cambiarlo di nuovo | F8, F10, F6 |
| 3 | Il nome si dà dal PC: **fai lampeggiare il LED** per essere sicuro che sia lui, poi gli scarichi **il nome del progetto, quello del vecchio**. | Dare il nome al nodo sbagliato fra due identici; inventare un nome nuovo che il PLC non cerca | F6, F7, F16 |
| caso | «Qui il progetto non dice a quale porta è attaccato»: per questo il nome non glielo dà il PLC. | Generalizzare a «mai trovato» (errore 3); nel caso mostrato non cambia il gesto | F11 |

**Restano nella scheda (descrizione o canale):** sostituzione automatica con tutte le sue condizioni (F11, F12, F13: stessa
porta, dispositivo che la supporta, funzione attiva) · ricambio già usato col nome vecchio e opzione «sovrascrivi» (F14) ·
scheda di memoria che porta il nome (F15) · watchdog e valori sostitutivi (F5) · le scritte esatte del software
(«pronto per l'assegnazione» / «non raggiungibile», F8: sono di un software solo).

**Durata obiettivo: 52-58 s.** Motivo: tre pezzi, ognuno col suo gesto che si vede (LED verde, PC, lampeggio), più il dubbio di
chi guarda e il caso in una frase. Sta sul bordo alto dei 48-56 s di riferimento; non serve di più perché tutto il resto
sta in descrizione.

**Chiusura che il contenuto autorizza:** «L'ho trovato dal nome. L'IP glielo do io.» Chiude la promessa del gancio («non lo
trovo» → trovato) e ripete la distinzione (nome prima, IP dopo) senza dire «sempre».

## 2 · Il discorso (di fila, senza secondi)
B1 Ho perso un nodo! Me l'hanno cambiato con uno identico, e non lo trovo.
B2 Lo so cosa pensi: il LED è verde, gli rimetti lo stesso IP e riparte.
B3 Verde vuol dire solo che il cavo c'è. Io i nodi non li cerco per IP: li cerco per nome.
B4 Uno nuovo di fabbrica il nome non ce l'ha. E qui non posso darglielo io: il progetto non dice a quale porta è attaccato.
B5 Col PC lo vedi: c'è, col suo indirizzo MAC, ma senza nome. Non è guasto.
B6 Fai lampeggiare il LED per essere sicuro che sia lui, poi gli scarichi il nome del progetto: quello del vecchio.
B7 Eccolo! L'ho trovato dal nome. L'IP glielo do io.
B8 Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

Catena: B1 → **MA** B2 (il dubbio) → **MA** B3 (verde = solo cavo; nome, non IP) → **QUINDI** B4 (nuovo = senza nome; qui il PLC
non può darlo) → **QUINDI** B5 (col PC: c'è, non è guasto) → **QUINDI** B6 (scegli e dai il nome giusto) → **QUINDI** B7 (trovato).

## 3 · Il taglio in clip
| Battuta | Scena | Clip |
|---|---|---:|
| B1 | S1 | 6 s |
| B2 | S2 | 6 s |
| B3 | S3 | 8 s |
| B4 | S4 | 10 s |
| B5 | S5 | 6 s |
| B6 | S6 | 8 s |
| B7 | S7 | 4 s |
| B8 | S8 | 8 s (CTA, +2 s) |

Una battuta per clip, nessuna divisa. **Ridondanze tolte** dalla prima stesura continua (che misurava 74 s su 9 scene):
- «Senza nome non posso parlargli» dopo «il nome non ce l'ha»: lo dicono già B1 («non lo trovo») e B3 («li cerco per nome»); così B4 e la frase del caso stanno in una clip sola.
- «Glielo dai tu, col PC. Nell'elenco della rete c'è…» → «Col PC lo vedi: c'è…»: «glielo dai tu» lo dice già il gesto di B6.
- «…e non il gemello accanto» in B6: «per essere sicuro che sia lui» dice la stessa cosa.
- La sintesi «Prima il nome, poi l'IP» davanti alla CTA: è la stessa cosa di B7 («L'ho trovato dal nome. L'IP glielo do io»).
- «e io continuo a non trovarlo» → «e non lo trovo»; «il LED della porta» → «il LED» (la porta si vede in S2).
Nessun pezzo dell'indispensabile è stato tolto.

## 4 · Note battuta per battuta
| | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | apre la domanda: perché un nodo identico non viene trovato? Il panico è quello dello slot | F4, F5 | «Tutta la rete lo sta cercando» detto a voce: a cercare è il PLC, non la rete (F4) · «Sono andato in STOP»: non confermato, cambia da CPU a CPU |
| B2 | il dubbio di chi guarda, con le sue parole, dove nasce l'errore 1 | F9, errore 1 | «Tutto quello che sai sull'IP è sbagliato»: finto ribaltamento, l'IP conta, lo assegna il PLC |
| B3 | risponde riprendendo «verde» e chiude sull'effetto; porta il criterio vero: nome, non IP | F9, F3, F4 | «Il PLC usa il NameOfStation»: termine che in reparto non si usa · «l'IP non serve»: falso (F3) |
| B4 | perché non lo trova, e nomina il caso prima del gesto | F2, F1, F11 | «Un nodo nuovo non viene mai trovato»: falso con la topologia configurata (errore 3) · spiegare intera la sostituzione automatica (vicini, stessa porta, supporto, F11-F13): nel caso mostrato non cambia cosa fa chi guarda, va in descrizione · «un ricambio» senza dire «nuovo di fabbrica»: uno usato può avere il nome vecchio (F2, F14) |
| B5 | separa «senza nome» da «guasto», con un controllo che si fa | F8, F10, F6 | «Guarda le spie del nodo: se lampeggiano manca il nome»: non confermato · la scritta «pronto per l'assegnazione»: è di un software solo, detta col suo significato · «se non è nell'elenco è guasto»: non raggiungibile può essere anche rete o cavo, e non è il caso mostrato |
| B6 | il gesto: quello giusto fra identici, e il nome giusto | F6, F7, F16 | «Dagli un nome, per esempio nodo nuovo»: un nome diverso da quello del progetto non lo fa ritrovare (F16) · «lo riconosci dal posto nel quadro»: sono identici, si sceglie dal MAC e dal lampeggio (F7) |
| B7 | chiude la promessa del gancio e ribadisce l'ordine nome → IP | F3, F6 | sintesi a parte «Prima il nome, poi l'IP»: ripete questa battuta, tolta al taglio |
| B8 | una CTA, keyword NOME, tagline | invariante 6 | «Commenta NOME e ti mando la procedura»: niente materiali gratis nel video |

## 5 · Il piano scena per scena (forma corta)
**Mondo IBRIDO**: quadro vero + ologrammi (le etichette dei nomi, la mappa delle porte), mai toccati. Linea in stop, niente in
moto. Logo MA sul PLC e sui nodi; Mister Automation col merch MA.
**Set A**: quadro aperto a bordo linea, lato manutenzione; PLC con la faccia sulla guida DIN; sotto, nella zona logica, una
fila di nodi di I/O identici e lo switch, cavi RJ45 inseriti ai due capi. Il ricambio è già montato e cablato.
**Set B**: carrello col portatile davanti al quadro (taglio motivato da «Col PC lo vedi»). Schermata senza marchi.
Spie: sul ricambio si vede solo il LED di link, verde (F9); le altre spie del nodo restano fuori fuoco (non confermato cosa mostrano).

| Scena | Set | Cosa si vede · componente · stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | PLC in panico; sotto, la fila di nodi; il ricambio nuovo, LED di link verde; ologramma di un'etichetta col punto di domanda che scorre sulla fila | gli occhi del PLC scorrono la fila su «non lo trovo» |
| S2 | A | Mister Automation davanti al quadro, il ricambio in primo piano, LED verde | M.A. indica il LED su «verde» |
| S3 | A | primo piano della porta: cavo inserito, LED verde; poi ologrammi: un'etichetta col nome sopra ogni nodo | su «per nome» si accendono le etichette dei nodi |
| S4 | A | sopra il ricambio un'etichetta vuota; accanto l'ologramma della mappa del progetto con la colonna delle porte vuota | il PLC allarga lo sguardo verso la mappa vuota su «non dice a quale porta» |
| S5 | B | schermo: elenco dei dispositivi in rete, una riga col MAC e il campo nome vuoto | M.A. tocca il trackpad su «vedi»; il PLC tira un sospiro su «non è guasto» |
| S6 | A/B | il LED di link del ricambio lampeggia verde; M.A. guarda dal portatile al quadro | il LED lampeggia su «lampeggiare» |
| S7 | A | l'etichetta col nome del vecchio si posa sul ricambio; ologramma dell'IP che arriva dal PLC | il PLC sorride su «Eccolo!» |
| S8 | A | PLC frontale, sereno; M.A. accanto, portatile chiuso; logo MA | il PLC guarda in camera su «Commenta NOME» |

## 6 · Controlli
- **Tempo** (`timing.py --voce lipsync --obiettivo 52-58`): 56 s di montato, 8 clip, 88 crediti, nessuna clip oltre 10 s, ✅ dentro l'obiettivo.
  Il controllo veloce (parole ÷ 2,0) dà 64 s: S2, S3, S5 e S6 stanno **esattamente** al bordo della clip (6,0 / 8,0 / 6,0 / 8,0 s).
- **Lettore fresco** e **verità e limiti**: non lanciati in questo giro (consegna: niente subagenti). Da fare prima di dare il parlato a Saverio.

```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      14    2.5    5.6     6       10
   S2      15    2.5    6.0     6       10
   S3      20    2.5    8.0     8       12
   S4      24    2.5    9.6    10       15
   S5      15    2.5    6.0     6       10
   S6      20    2.5    8.0     8       12
   S7       9    2.5    3.6     4        7
   S8      12    2.5    4.8     8       12  (+2 s CTA)
  TOT     129                  56       88
somma delle clip: 56 s · controllo veloce: 64 s · ✅ 56 s, dentro l'obiettivo · 🟢 VERDE
```

## Deviazioni
- **8 scene** invece di 6-7: tre pezzi, il dubbio e il caso nominato; S7 è una reazione da 4 s che chiude la promessa.
- **Durata tirata.** A Saverio direi: «L'indispensabile entra in 56 s, ma quattro clip sono al limite: se la pilota mostra che
  la voce sfora, preferisco salire a 58-60 s piuttosto che togliere il lampeggio del LED o la frase sul progetto senza mappa
  delle porte. Decidi tu.»
- **Parla il componente, Mister Automation è muto** in scena: lo slot del lunedì vuole il componente con la faccia; una voce sola per clip.
- **CTA** presa dalla forma dell'esempio 01 («Vuoi impararlo? Commenta …»): la `LIBRERIA-CTA.md` in questo giro non si apre.
- **Etichette del software** («pronto per l'assegnazione») dette col loro significato, non con la scritta: F8 vale per un software solo.
