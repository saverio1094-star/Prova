# Caso 01 · «Sensore induttivo o capacitivo: quale scegliere per rilevare il pezzo?» · passo 3 · giro 05b

Fonti lette: PROVA/SKILL.md · PROVA/fasi/3-storia-parlato.md · PROVA/quaderno.md (0 voci, niente contatori da aggiornare) ·
esempi 02, 03, 05, 07, 08 (01 non aperto) · `casi/caso-01_cieco-induttivo_INPUT.md` · `esiti-2026-10-05/caso-01_fatti.md`.

---

## 1 · Prima della prima battuta

**Cosa deve saper distinguere chi guarda alla fine.** L'induttivo vede solo il metallo, e la sua distanza di intervento
dichiarata vale per l'acciaio: sull'alluminio, in un induttivo standard, è meno della metà. Il capacitivo vede anche quello
che non è metallo, perfino l'acqua attraverso il vetro della vasca, ma solo se la sensibilità è regolata in modo che il vetro
da solo non lo accenda. Quindi: prima il materiale, poi il sensore, poi la regolazione.

**Il caso preciso.** Una linea sola, in due punti. (a) Nastro con pezzi di alluminio, induttivo **standard** su staffa alla
sponda. (b) Lavatrice a valle, vasca con finestra di **vetro**, capacitivo fuori dal vetro all'altezza del livello d'acqua.

**Errore plausibile di chi guarda** (la scheda lo lascia a me).
- Principale: «metallo è metallo»: se l'induttivo accende con l'acciaio, a quella distanza vede anche l'alluminio; se
  resta spento è guasto e lo cambio (o lo monto alla distanza di catalogo e non funziona mai).
- Secondo, sul capacitivo: «LED acceso = acqua al livello», mentre con la sensibilità troppo alta il sensore sta vedendo il
  vetro.

**L'indispensabile** (4 pezzi: senza uno di questi, domani si sbaglia)
| # | Pezzo | Errore che evita | Fatto |
|---|---|---|---|
| P1 | L'induttivo fa un campo magnetico e solo il metallo ne assorbe energia → vede solo il metallo | metterlo su un bersaglio che non è metallo (l'acqua) | F2 |
| P2 | La distanza di intervento dichiarata vale per l'acciaio; in un induttivo **standard**, sull'alluminio è meno della metà → si avvicina | credere guasto un sensore buono, o montarlo alla distanza di catalogo | F1 |
| P3 | Il capacitivo sente l'acqua **attraverso il vetro** perché la permittività dell'acqua (circa 80) è molto più alta di quella del vetro (circa 5) | scegliere l'induttivo per il livello, o pensare che serva forare la vasca | F3, F4 |
| P4 | Con la sensibilità troppo alta il capacitivo vede la parete e resta acceso senza acqua → si abbassa finché il vetro da solo non lo accende | leggere «livello raggiunto» quando il sensore vede solo il vetro | F3 |

**Durata obiettivo: 54-60 s.** Motivo: sono due sensori, ognuno con il suo meccanismo e la sua trappola (4 pezzi, il limite
alto della pagina). Il riferimento 48-56 s regge un componente e una trappola; qui servono qualche secondo in più. Non taglio
un pezzo per rientrare: P4 è il gemello di P2 sul capacitivo, e senza P4 chi guarda monta il capacitivo sul vetro e si fida
di un LED sempre acceso. → Riga per Saverio in § Deviazioni.

**Chiusura che il contenuto autorizza.** «Prima il materiale, poi il sensore, poi la regolazione.» Regge su F1-F4.
**Non** autorizzata: «per il metallo sempre l'induttivo» o «il capacitivo non vede il metallo» (F4 dice il contrario; la
scheda non confronta i due sensori sullo stesso metallo).

---

## 2 · Il discorso (di fila, senza secondi né clip)

B1 Questo pezzo di alluminio passa, e il PLC deve saperlo senza toccarlo. Induttivo o capacitivo?
B2 È metallo, quindi prendo l'induttivo. Fa un campo magnetico, e solo il metallo ne assorbe energia. Con l'acciaio: acceso.
B3 Passa il pezzo… spento. Ma è metallo: è guasto?
B4 Guasto no. La distanza di intervento dichiarata vale per l'acciaio: in un induttivo standard, sull'alluminio è meno della metà. Lo avvicino: acceso.
B5 In lavatrice, però, il PLC vuole il livello dell'acqua. Non è metallo: serve il capacitivo.
B6 Sente l'acqua attraverso il vetro: l'acqua ha permittività circa ottanta, il vetro circa cinque.
B7 E il vetro? Lo vede, se la sensibilità è troppo alta: resta acceso senza acqua. La abbasso finché il vetro da solo non lo accende.
B8 Prima il materiale, poi il sensore, poi la regolazione. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

Controllo MA / QUINDI: B1→B2 quindi (è metallo) · B2→B3 ma (acceso con l'acciaio, spento col pezzo) · B3→B4 ma (guasto no)
· B4→B5 ma («però»: il bersaglio nuovo non è metallo) · B5→B6 quindi · B6→B7 ma (e il vetro?) · B7→B8 quindi. Nessun «e poi».

---

## 3 · Il taglio in clip

| Battuta | Scena | Clip | Note di taglio |
|---|---|---:|---|
| B1 | S1 | 6 s | |
| B2 | S2 | 8 s | |
| B3 | S3 | 4 s | |
| B4 | S4 | 10 s | |
| B5 | S5 | 6 s | |
| B6 | S6 | 6 s | |
| B7 | S7 | 10 s | al limite (25 parole, 10,0 s): se la pilota parla più lenta, si divide **dove cambia il ragionamento**, prima di «La abbasso…» (S7a dubbio+risposta 6 s · S7b gesto 4 s): stesso totale, 60 s |
| B8 | S8 | 10 s | CTA (+2 s) |

**Ridondanze tolte prima di misurare** (la prima stesura misurava 80 s su 11 clip):
- «sul nastro» in B1 e «sul vetro della vasca / lo metto fuori» in B6: si vedono.
- «È alluminio» in B3: detto una volta in B1, che così prepara la trappola.
- «Quindi lo avvicino… stringo. Acceso.» come battuta a sé: fusa nella coda di B4 (stessa risposta, stesso gesto).
- «Il pezzo finisce in lavatrice, e qui…»: diventa «In lavatrice, però,…» (il passaggio lo fa il taglio di set).
- «Adesso si accende solo con l'acqua» dopo il gesto in B7: lo dice il LED che si spegne.
- «Vuoi impararlo?» e una sintesi lunga nella CTA: la sintesi diventa tre parole in fila e la CTA sta in una clip.
Nessun pezzo dell'indispensabile è uscito.

---

## 4 · Le note battuta per battuta

| | Cosa fa (a quale domanda risponde) | F | Alternativa scartata, e perché |
|---|---|---|---|
| B1 | apre la scelta su un pezzo vero e dice subito che è alluminio (prepara la trappola senza svelarla) | F2, F3 (rilevare senza contatto) | «Sembrano uguali. Ma rilevano gli stessi oggetti?» (proposta di Astra): confronto astratto, la domanda non nasce da niente che si vede |
| B2 | perché l'induttivo per il metallo, e **solo** per il metallo (meccanismo vero) | F2 | «il metallo lo smorza» (brief): parola vaga, il fatto è «ne assorbe energia» · «e l'uscita commuta» a voce: lo dice il LED |
| B3 | il fatto che smentisce la scelta + il dubbio di chi guarda nel punto esatto dove nasce l'errore | F1 | affermare «è rotto»: il dubbio si dice come domanda, così la risposta lo può riprendere |
| B4 | risponde riprendendo «guasto», dà il termine vero, nomina il caso (induttivo standard) prima della regola, chiude sul gesto e sull'effetto | F1 | «0,35-0,45 volte la distanza»: il numero preciso non cambia il gesto (avvicinare); «meno della metà» è nella scheda · regola senza «standard»: falsa per i modelli a fattore 1 · **eccezione fattore 1 scartata a voce**: nel caso mostrato (induttivo standard già montato) chi guarda fa la cosa giusta anche senza saperla, cioè lo avvicina; va in descrizione/canale come alternativa al ricambio |
| B5 | svolta: il secondo bersaglio non è metallo, quindi l'induttivo non basta | F2 | «Fa un campo elettrico» (brief, S6): non è nella scheda |
| B6 | come fa il capacitivo a vedere l'acqua attraverso il vetro, col termine vero e i due numeri | F3, F4 | «sente ogni materiale» (brief): la scheda dice «anche i metalli» e «se dietro c'è permittività più alta della parete», non «ogni» · spessore massimo 10-20 mm e «dipende dal modello» a voce: nel caso mostrato (finestra di vetro di una vasca) non cambia la decisione; va in descrizione |
| B7 | dubbio di chi guarda dove nasce il secondo errore («e il vetro?»), risposta che riprende «vetro», gesto di regolazione | F3 | «condensa e schiuma lo disturbano» (F5, non confermato) · «teach-in» a voce: un secondo metodo in più, il gesto mostra il potenziometro · «a volte resta acceso» senza dire quando: eccezione a metà |
| B8 | chiude la promessa del gancio («induttivo o capacitivo?») in tre passi, poi una CTA e la tagline | F1-F4 | «Prima guardi di cosa è fatto, poi scegli» (brief): dimentica la regolazione, che è metà del reel · «per il metallo sempre induttivo»: la scheda non lo dice (F4: il capacitivo vede anche i metalli) |

---

## 5 · Il piano scena per scena (forma corta)

**Mondo: REALE.** Un capannone, una linea: nastro trasportatore con pezzi di alluminio che va dentro una lavatrice
industriale. Mister Automation (anchor, render 3D stilizzato, volto 3/4, merch con logo MA) sempre fuori dalle parti in moto.
Due set: **A · sponda del nastro** (induttivo su staffa, faccia verso il passaggio del pezzo) · **B · finestra della vasca**
(capacitivo fuori dal vetro, all'altezza del livello). Altezze e lato esatti: non verificati su SET-TIPO. Colore del LED: non
confermato, si scrive solo acceso/spento. Monogramma MA sui due sensori, niente marchi.

| Scena | Set | Cosa si vede · stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | A | mezza figura accanto alla sponda; nastro in marcia; un pezzo di alluminio arriva verso l'induttivo; LED spento | indica il pezzo senza toccarlo ↔ «questo pezzo» |
| S2 | A | mani e staffa da vicino; passa un **pezzo campione d'acciaio** davanti alla faccia → LED acceso | sfiora la staffa ↔ «campo magnetico»; annuisce al LED ↔ «acceso» |
| S3 | A | primo piano radente sul LED; il pezzo di alluminio passa nello stesso punto → LED resta spento | si china verso il LED, sopracciglio alzato ↔ «è guasto?» |
| S4 | A | stesso asse; mano solo sulla staffa, dal lato esterno della sponda: spinge il sensore più vicino al passaggio, toglie la mano, il pezzo successivo passa → LED acceso | spinge il sensore ↔ «lo avvicino» |
| S5 | B (taglio) | il pezzo entra nella lavatrice; davanti alla finestra della vasca, acqua dietro il vetro; capacitivo già montato fuori dal vetro | indica il livello dell'acqua ↔ «livello» |
| S6 | B | primo piano di lato sul capacitivo sul vetro; acqua all'altezza del sensore → LED acceso | tocca il vetro accanto al sensore ↔ «attraverso il vetro» |
| S7 | B | dopo uno scarico (luce uguale, livello sotto il sensore): LED ancora acceso; piccolo cacciavite sul potenziometro → LED si spegne | gira il potenziometro ↔ «la abbasso» |
| S8 | B | livello che risale fino al sensore → LED acceso; Mister Automation verso camera, scritta SENSORE | conta tre dita ↔ «materiale, sensore, regolazione» |

---

## 6 · Controlli

- **Tempo** (`timing.py`, voce lipsync, obiettivo 54-60): uscita sotto. 60 s, dentro l'obiettivo; nessuna clip oltre 10 s;
  S7 esattamente a 10,0 s (vedi taglio).
- **Lettore fresco** e **verità e limiti**: non lanciati in questo giro (istruzione: niente subagenti). Da fare prima di
  mandare il parlato a Saverio.
- Autocontrollo dei limiti (non vale come controllo, l'ho scritto io): F1 «standard» detto a voce prima della regola · F2
  «solo il metallo» a voce · F3 caso nominato («attraverso il vetro»), spessore/modello lasciati alla descrizione · F4
  «circa» su entrambi i numeri · F5 non usato · nessun «campo elettrico», nessun «ogni materiale».

```
─── TIMING · voce: lipsync ───
scena  parole  p/sec    sec  clip  crediti
   S1      15    2.5    6.0     6       10
   S2      19    2.5    7.6     8       12
   S3       9    2.5    3.6     4        7
   S4      22    2.5    8.8    10       15
   S5      15    2.5    6.0     6       10
   S6      14    2.5    5.6     6       10
   S7      25    2.5   10.0    10       15
   S8      19    2.5    7.6    10       15  (+2 s CTA)
  TOT     138                  60       94

─── DURATA ───
somma delle clip: 60 s + asset riusabili 0 s = 60 s di montato
controllo veloce (parole ÷ 2.0): 69 s — se si scosta di molto, ricontare

─── SPIA DI MESTIERE (non blocca) ───
frasi: 21 · sotto le 6 parole: 11 · sopra le 25 parole: 0 — nei parlati approvati ci sono frasi corte e nessuna sopra le 25

─── OBIETTIVO 54-60 s (avviso, non blocca) ───
  ✅ 60 s, dentro l'obiettivo

─── ESITO ───
  ✅ nessuna scena oltre i 10 s

🟢 VERDE
Costo animazione: 94 crediti su 8 clip
```

---

## Deviazioni

- **Durata 60 s, sopra il riferimento 48-56.** Riga per Saverio: «Per far capire i due sensori servono 4 pezzi (induttivo solo
  metallo · distanza sull'alluminio meno di metà · capacitivo attraverso il vetro · sensibilità che non deve vedere il vetro):
  stanno in 60 s. Va bene 60, o ne facciamo due reel (induttivo cieco sull'alluminio / capacitivo attraverso il vetro)?»
- **8 scene invece di 6-7**: una per pezzo di ragionamento; fondendo B3 in B4 la clip supera i 10 s.
- **Prova con l'acciaio**: nel brief una chiave tenuta in mano davanti al sensore; qui un pezzo campione d'acciaio sul nastro,
  così nessuna mano davanti al nastro in marcia (invariante 3).
- **Capacitivo già montato** sul vetro (nel brief lo tira fuori in scena): pagina 3, la storia che si vede, punto 2.
- **Altezze/lato** dei due sensori e **colore del LED**: non verificati; da chiudere con SET-TIPO prima delle immagini.
