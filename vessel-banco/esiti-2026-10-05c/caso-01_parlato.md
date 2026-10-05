# Caso 01 · «Induttivo o capacitivo?» · passo 3 · giro di prova 5/10 (c)
Scritto da Vessel dalla copia PROVA. Input: brief di Serafino (caso-01 INPUT) + scheda `esiti-2026-10-05/caso-01_fatti.md` (F1-F5).
Quaderno: 0 voci, nessun contatore da aggiornare.

## 1 · Prima della prima battuta

**Cosa deve saper distinguere chi guarda alla fine.** Induttivo e capacitivo non si scelgono a occhio: l'induttivo vede solo il
metallo, e la distanza scritta vale per l'acciaio; il capacitivo sente ogni materiale, anche dietro un vetro, e proprio per
questo sente un po' anche il vetro. Quindi prima guardi di cosa è fatto quello che devi vedere, poi provi il sensore su quel materiale.

**Il caso preciso.** Un pezzo di alluminio su un nastro, letto da un induttivo standard su staffa alla sponda. Poi lo stesso
pezzo entra in lavatrice, dove il PLC vuole il livello dell'acqua: capacitivo montato fuori dalla finestra di vetro della vasca.

**Errore plausibile di chi guarda** (la scheda lo lasciava a chi scrive):
- «È metallo, quindi l'induttivo lo vede alla distanza scritta. Se il LED non si accende, il sensore è guasto: lo cambio.»
- «Il capacitivo sul vetro è acceso, quindi c'è acqua.» Invece, troppo sensibile, vede il vetro e resta acceso anche a vasca vuota.

**L'indispensabile** (senza questi pezzi domani chi guarda sbaglia davanti a questi due sensori):

| # | Pezzo, con il suo appiglio | Errore che evita | Fatto |
|---|---|---|---|
| I1 | L'induttivo fa un campo magnetico alternato; il metallo che ci entra ne assorbe energia e l'uscita commuta → vede **solo il metallo**. Appiglio: la chiave d'acciaio davanti alla faccia, LED acceso. | mettere un induttivo su un materiale che non è metallo (l'acqua) | F2 |
| I2 | Nell'induttivo **standard** la distanza di intervento vale per l'acciaio; sull'alluminio è meno della metà. Appiglio: il gesto, lo avvicino e il LED si accende. | cambiare un sensore buono perché «non vede il pezzo» | F1 |
| I3 | Il capacitivo fa un campo elettrico e sente ogni materiale, ma non allo stesso modo: il vetro poco, l'acqua tantissimo → vede l'acqua attraverso il vetro. Appiglio: il sensore fuori dal vetro, niente fori nella vasca. | pensare che serva un sensore a contatto con l'acqua, o provare con un induttivo | F3, F4 |
| I4 | Anche il vetro lo sente: se la sensibilità è troppo alta resta acceso a vasca vuota. Appiglio: il gesto, abbasso la sensibilità finché, senz'acqua, si spegne. | fidarsi di un LED acceso che sta guardando il vetro | F3 |

Restano nella scheda e vanno in descrizione: induttivi a fattore 1 (stessa distanza su tutti i metalli) · fattore preciso 0,35-0,45 ·
parete fino a circa 10-20 mm, secondo materiale e modello · teach-in al posto del potenziometro · valori di permittività (vetro ~5, acqua ~80).
Non usati perché non confermati: condensa/schiuma (F5), colore del LED.

**Durata obiettivo: 62-68 s.** Viene dai pezzi: quattro pezzi con il loro gesto stanno in circa 8 s l'uno, più gancio, cambio di
set, sintesi e CTA. Il brief di 52 s ne aveva tre (mancava I4). Fuori dai 48-56 s dei reel migliori: vedi § Deviazioni.

**La chiusura che il contenuto autorizza.** «Prima guardi di cosa è fatto, poi lo provi su quel materiale.» Non autorizza
«metallo = induttivo, il resto = capacitivo»: il capacitivo vede anche i metalli (F4) e la scheda non dice quando preferire l'uno sul metallo.

## 2 · Il discorso
B1 Quando passa questo pezzo, il PLC deve saperlo. Senza toccarlo. Induttivo o capacitivo?
B2 È metallo, quindi induttivo. Fa un campo magnetico alternato: il metallo che ci entra ne assorbe energia, e l'uscita commuta.
B3 La chiave d'acciaio la vede. Ma passa il pezzo… il LED resta spento. Lo cambio?
B4 Cambiarlo non serve: è alluminio. Nell'induttivo standard la distanza di intervento vale per l'acciaio. Sull'alluminio è meno della metà.
B5 Quindi lo avvicino. Ripassa il pezzo… acceso.
B6 In lavatrice il PLC vuole il livello. Ma l'acqua non è metallo: serve il capacitivo.
B7 Fa un campo elettrico e sente ogni materiale: il vetro poco, l'acqua tantissimo. Così la vede attraverso il vetro.
B8 Ma anche il vetro lo sente: se è troppo sensibile, resta acceso senz'acqua. Abbasso la sensibilità finché si spegne.
B9 Quindi: prima guardi di cosa è fatto, poi lo provi su quel materiale.
B10 Vuoi impararlo? Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

Filo MA/QUINDI: B1→B2 quindi · B2→B3 ma · B3→B4 ma (no, non serve) · B4→B5 quindi · B5→B6 ma (altro pezzo d'impianto, altro materiale) ·
B6→B7 quindi (perché il capacitivo ci riesce) · B7→B8 ma · B8→B9 quindi.

## 3 · Il taglio
| Battuta | Scena | Clip | Ridondanza tolta per starci |
|---|---|---:|---|
| B1 | S1 | 6 s | — |
| B2 | S2 | 8 s | «davanti alla faccia sensibile»: lo mostra l'immagine |
| B3 | S3 | 6 s | «e» prima di «il LED resta spento» |
| B4 | S4 | 8 s | — |
| B5 | S5 | 4 s | — (tenuta separata: è la scena del gesto) |
| B6 | S6 | 6 s | «Il pezzo va in lavatrice» e «dell'acqua» dopo «livello»: li dicono l'immagine e la frase dopo |
| B7 | S7 | 8 s | «Il capacitivo» come soggetto: è appena stato nominato |
| B8 | S8 | 8 s | il secondo «senz'acqua» e «a vasca vuota» (era detto due volte) |
| B9 | S9 | 6 s | — |
| B10 | S10 | 8 s | — (CTA + tagline, +2 s di coda) |

Nessuna battuta divisa. Bozza prima del taglio: 11 scene, 78 s; tolte le ridondanze sopra e fuse «L'acqua sale… acceso» (si vede in S7).

## 4 · Note battuta per battuta
| B | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | apre la scelta che il reel chiude in B9 | — | «Sembrano uguali. Ma rilevano gli stessi oggetti?» (gancio di Astra): promette un confronto su più oggetti che il reel non fa |
| B2 | perché l'induttivo vede il metallo: termine vero + cosa succede | F2 | «il metallo lo smorza» (brief): giusto ma non dice cosa succede · «solo l'induttivo vede il metallo»: falso, F4 |
| B3 | prova ok → prova ko; il dubbio di chi guarda col suo gesto sbagliato | F2 | «È guasto?»: più astratto; «lo cambio» è quello che si fa davvero |
| B4 | risponde riprendendo la parola («cambiarlo»), nomina il caso (standard) prima della regola | F1 | «0,35-0,45 volte»: il numero preciso non cambia il gesto · l'eccezione fattore 1: nel caso mostrato non c'è, e chi ha un fattore 1 il pezzo lo vede già e non avvicina niente → descrizione |
| B5 | il gesto di domani, con l'esito che si vede | F1 | «lo metto a 3 mm»: nessun modello in scheda, il millimetro sarebbe inventato |
| B6 | cambio di set con causa (il pezzo entra in lavatrice) e il criterio applicato a un non metallo | F2 | «galleggiante» o altre tecnologie di livello: non in scheda, altro reel |
| B7 | perché il capacitivo vede l'acqua attraverso il vetro, senza la parola permittività | F3, F4 | «permittività 5 contro 80»: numeri che in reparto non si usano · «attraverso qualsiasi parete»: F3 dipende da spessore e materiale; il caso detto è il vetro |
| B8 | la trappola del capacitivo, simmetrica a B3-B4, col gesto che la risolve | F3 | «condensa e schiuma lo ingannano»: F5 non confermato · «rifai il teach-in»: dipende dal modello; «abbasso la sensibilità» vale per potenziometro e teach-in |
| B9 | chiude la promessa di B1 e tiene insieme le due trappole | F1-F4 | «Metallo induttivo, il resto capacitivo»: F4 lo smentisce · «Prima guardi di cosa è fatto, poi scegli» (brief): lascia fuori le due prove, metà della lezione |
| B10 | una sola CTA → corsi e webinar, poi tagline | — | «Salva il confronto» (Astra): non porta a corsi né webinar |

## 5 · Il piano scena per scena (forma corta)
**Mondo REALE.** Un reparto: set A = nastro trasportatore con pezzi di alluminio, induttivo (monogramma MA) su staffa con asola,
fissata alla sponda, faccia verso il passaggio del pezzo, cavo dal sensore alla canalina; set B = lavatrice industriale per pezzi,
finestra di vetro sulla vasca, capacitivo (monogramma MA) fuori dal vetro all'altezza del livello da rilevare, cavo al pressacavo.
Il nastro entra nella lavatrice: è la causa che porta da A a B. Mister Automation sempre fuori dalle parti in moto.
Altezze e lato esatti non verificati su SET-TIPO; colore del LED non fissato.

| S | Set | Cosa si vede · stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | mezza figura, nastro in marcia, pezzo d'alluminio in arrivo; LED induttivo spento | indica il pezzo senza toccarlo ↔ «questo pezzo» |
| S2 | A | mani da vicino, nastro fermo, nessun pezzo davanti; chiave d'acciaio davanti alla faccia → LED acceso | avvicina la chiave ↔ «il metallo che ci entra» |
| S3 | A | primo piano radente sul LED, nastro in marcia, mani fuori; il pezzo passa → LED spento | aggrotta la fronte, sfondo ↔ «Lo cambio?» |
| S4 | A | nastro fermo; un pezzo preso dalla cassetta a lato; staffa con il sensore ancora indietro nell'asola | batte l'unghia sul pezzo ↔ «è alluminio» |
| S5 | A | stesso asse di S3: sensore più avanti nell'asola (segno del dado vecchio), nastro in marcia, pezzo passa → LED acceso | annuisce verso il LED ↔ «acceso» |
| S6 | B | il pezzo entra in lavatrice; finestra di vetro, capacitivo già sul vetro, acqua che sale | indica il sensore sul vetro ↔ «capacitivo» |
| S7 | B | primo piano di lato: acqua sopra il sensore, LED acceso | sfiora il vetro accanto al sensore ↔ «attraverso il vetro» |
| S8 | B | vasca scaricata, acqua sotto il sensore, LED ancora acceso → dopo il gesto spento | piccolo cacciavite sul potenziometro ↔ «abbasso» |
| S9 | A | come S1: pezzo dopo in arrivo, LED acceso al passaggio | gira un pezzo in mano guardandolo ↔ «di cosa è fatto» |
| S10 | A | mezza figura in camera, scritta di scena SENSORE, logo MA sul merch | guarda in camera ↔ «Commenta SENSORE» |

## 6 · Controlli
- **Lettore fresco (Aqua Regia)** e **controllo dei limiti**: non lanciati, il giro di prova vieta i subagenti. Da fare prima di Saverio.
- **Tempo** (`timing.py caso-01_parlato.txt --voce lipsync --obiettivo 62-68`):

```
scena  parole  p/sec    sec  clip  crediti
   S1      13    2.5    5.2     6       10
   S2      20    2.5    8.0     8       12
   S3      15    2.5    6.0     6       10
   S4      19    2.5    7.6     8       12
   S5       7    2.5    2.8     4        7
   S6      15    2.5    6.0     6       10
   S7      19    2.5    7.6     8       12
   S8      19    2.5    7.6     8       12
   S9      13    2.5    5.2     6       10
  S10      12    2.5    4.8     8       12  (+2 s CTA)
  TOT     152                  68      107
somma delle clip: 68 s di montato · controllo veloce (parole ÷ 2.0): 76 s
spia: frasi 26 · sotto le 6 parole 15 · sopra le 25: 0
OBIETTIVO 62-68 s: ✅ 68 s · nessuna scena oltre i 10 s · 🟢 VERDE · 107 crediti su 10 clip
```
S3, S6 e S8 stanno a filo della loro clip (6,0 s su 6 · 7,6 su 8): se la voce di Flow va più lenta, sono le prime a stringere.

## § Deviazioni
- **Durata 68 s e 10 scene** (mestiere: 48-56 s, 6-7 scene). A Saverio direi: «Viene 68 secondi, 12 sopra i reel migliori. Il motivo
  è che ogni sensore ha la sua trappola: l'induttivo vede l'alluminio a meno di metà distanza, il capacitivo sul vetro resta acceso
  se è troppo sensibile. Il tuo brief da 52 secondi aveva solo la prima. Togliere la seconda lascia chi guarda a fidarsi di un LED
  che guarda il vetro. Se vuoi stare sotto i 56, la strada che non lascia errori è fare due reel: induttivo e alluminio, capacitivo
  dietro il vetro. Decidi tu.» Se la voce va al ritmo del controllo veloce, il montato sale verso 76 s.
- **Dal brief:** l'induttivo è già montato sulla staffa (il brief lo faceva montare in S2: tre azioni in una clip); in S5 il
  sensore è già avanzato e lui reagisce al LED, invece di allentare-avvicinare-stringere davanti al nastro in marcia.
- **Gancio:** tenuto quello del brief («Induttivo o capacitivo?»), scartato quello di Astra.
- **Limiti non detti a voce, per descrizione:** fattore 1, spessore della parete (10-20 mm secondo materiale e modello), teach-in.
