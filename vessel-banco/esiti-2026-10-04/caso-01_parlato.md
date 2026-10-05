# Caso 01 · collaudo alla cieca · induttivo o capacitivo — parlato nuovo
Scritto da Vessel il 4/10/2026. Input: tabella di Serafino (7 scene, stesse durate 6+8+6+8+6+8+10) + obiettivo del tema di
Astra («Sembrano uguali. Ma rilevano gli stessi oggetti?», visualizzazioni qualificate e salvataggi). Niente scheda di Granite:
fatti solo dall'input e da quello che so con certezza, gli altri in fondo «da verificare».
Mondo REALE · Mister Automation in campo, una sola voce, lip-sync.

## Il filo e l'errore plausibile
**Filo:** induttivo e capacitivo sembrano uguali, ma la scelta la fa il materiale: l'induttivo vede solo il metallo (e la sua
distanza cambia con *quale* metallo), il capacitivo sente quasi tutto, ognuno con la sua forza.
**Errore plausibile:** «è metallo, quindi l'induttivo lo vede alla distanza scritta sul sensore» → invece quella distanza vale
per l'acciaio: sull'alluminio è meno di metà, e il pezzo passa senza essere visto.

## Il parlato
| Scena | Clip | Battuta |
|---|---:|---|
| S1 | 6 s | Sembrano uguali. Ma quando passa questo pezzo, quale dei due lo vede? |
| S2 | 8 s | È metallo: induttivo. Ci passo la chiave: l'acciaio assorbe energia dal suo campo magnetico. LED acceso. |
| S3 | 6 s | Passa il pezzo… e il LED resta spento. Ma non era metallo? |
| S4 | 8 s | Metallo sì, ma alluminio. La distanza di intervento vale per l'acciaio: qui è meno di metà. Lo avvicino. |
| S5 | 6 s | Adesso lo vede. Ma in lavatrice il PLC vuole sapere se l'acqua arriva qui. |
| S6 | 8 s | L'acqua non è metallo: capacitivo. Col campo elettrico sente quasi tutto: il vetro appena, l'acqua tantissimo. |
| S7 | 10 s | Prima guardi di cosa è fatto: se è metallo, quale. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza. |

Catena MA/QUINDI: S1 domanda → S2 QUINDI induttivo → S3 MA spento (il dubbio con le parole di chi guarda: «non era metallo?»)
→ S4 MA alluminio (riprende la parola «metallo» e chiude sull'effetto) → S5 QUINDI lo vede, MA problema nuovo → S6 QUINDI
capacitivo → S7 QUINDI la regola da salvare.

## Il piano scena per scena (corto)
**Mondo:** REALE. Linea di lavorazione: nastro con sponda laterale, poi a 2-3 m la lavatrice industriale con finestra di vetro
sul fianco della vasca. Pezzi di alluminio sul nastro. Nessun marchio; logo MA sui sensori e sul merch.

| Scena | Cosa si vede | Dove sta il componente | Stato | Gesto → parola |
|---|---|---|---|---|
| S1 | Mezza figura al nastro, pezzo di alluminio che arriva | Due sensori cilindrici identici (M18), uno per mano | Nastro in marcia | alza i due sensori → «uguali» |
| S2 | Mani da vicino sulla staffa | Induttivo **già montato** su staffa sulla sponda del nastro, faccia verso il pezzo, all'altezza del pezzo; cavo M12 che va in canalina | Nastro **fermo**; LED dell'uscita spento → acceso | passa la chiave d'acciaio davanti alla faccia → «chiave»; LED acceso su «acceso» |
| S3 | Primo piano radente sul LED, il pezzo passa | Stesso sensore, stessa posizione | Nastro in marcia; LED **resta spento** | alza lo sguardo dal LED alla camera → «metallo?» |
| S4 | Stesso asse, camera che si avvicina al LED | Sensore spostato più vicino sulla stessa staffa | Nastro **fermo**, pezzo di alluminio fermo davanti al sensore; LED spento → acceso | stringe il dado della staffa → «avvicino»; il LED si accende a fine battuta |
| S5 | La camera segue il pezzo dal sensore alla lavatrice | — (taglio di set: dal nastro alla vasca) | Nastro in marcia, LED induttivo acceso al passaggio; acqua **sotto** il sensore di livello | indica il punto sul vetro → «qui» |
| S6 | Finestra della vasca, primo piano di lato | Capacitivo **già montato** su staffa contro il vetro, all'altezza del livello da controllare | Acqua che sale; LED spento → acceso quando l'acqua arriva al sensore | sfiora il vetro accanto al sensore → «vetro»; reagisce al LED su «tantissimo» |
| S7 | Di nuovo al nastro, stesso asse di S1 | Induttivo al suo posto, LED che si accende al passaggio | Nastro in marcia; scritta SENSORE in sovrimpressione | guarda il pezzo successivo → «di cosa è fatto»; scritta su «SENSORE» |

## Deviazioni dal mestiere (e dall'input)
- **S7 senza «Vuoi impararlo?»**: con +2 s di CTA il tetto è 20 parole in 10 s; la sintesi «se è metallo, quale» porta la
  lezione dell'alluminio ed è quella che fa salvare, quindi ho tenuto lei e tolto la domanda. La keyword porta ai corsi in DM.
- **S1 senza «il PLC deve saperlo, senza toccarlo»**: il gancio va dritto alla promessa del tema («sembrano uguali… quale lo
  vede?»); il bisogno del PLC entra in S5, dove serve per cambiare set.
- **S2 e S6: sensori già montati** (l'input diceva «monta l'induttivo» / «tira fuori il capacitivo»): è il mestiere della
  pagina 3 (montare in scena chiede tre azioni in una clip). Stessa storia, un gesto per scena.
- **Nastro fermo in S2 e S4** (l'input non lo diceva): mani e chiave a pochi millimetri dalla faccia del sensore, vicino al
  nastro; con il nastro in marcia sarebbero dentro le parti in moto (invariante 3).
- **Molte frasi corte** (12 su 19 sotto le 6 parole, spia di timing): voluto, è il ritmo «prova → esito» degli esempi.

## Da verificare con Granite
1. **Distanza di intervento definita sull'acciaio.** La distanza nominale (Sn) dell'induttivo è misurata su un bersaglio
   standard di acciaio dolce (norma EN 60947-5-2). *Limite:* è la definizione di norma; da confermare con un datasheet.
2. **Alluminio «meno di metà».** Fattore di riduzione tipico dell'alluminio ~0,3-0,5 della Sn. *Limite:* dipende dal modello
   e dallo spessore del pezzo; **non vale per i sensori «fattore 1»** (tutti i metalli alla stessa distanza). Se Granite trova
   un fattore sopra 0,5 per i modelli comuni, la battuta S4 cambia.
3. **Meccanismo induttivo**: campo magnetico alternato, il metallo ne assorbe energia (correnti parassite) e l'oscillazione si
   smorza. *Limite:* «campo magnetico» è la semplificazione corrente di «campo elettromagnetico alternato».
4. **Capacitivo «sente quasi tutto», vetro poco, acqua tantissimo**: sente i materiali in base alla costante dielettrica (aria 1,
   vetro ~4-10, acqua ~80). *Limite:* materiali vicini all'aria (es. polistirolo espanso) quasi non li sente; sente anche i
   metalli, il parlato non dice il contrario.
5. **Capacitivo che sente l'acqua attraverso il vetro**: si fa su pareti non metalliche sottili, regolando la sensibilità
   (trimmer) per ignorare la parete. *Limite:* spessore e materiale della parete; condensa, schiuma o depositi sul vetro possono
   dare falsi segnali. È un controllo di **livello a punto** («arriva qui»), non una misura continua.
6. **Lavatrice industriale con finestra di vetro sulla vasca**: plausibile ma non confermato; se non è credibile, il capacitivo
   va su un tubo-spia o una vasca in plastica (Planimetrie / SET-TIPO).
7. **Posizione e cablaggio**: induttivo su staffa alla sponda, all'altezza del pezzo, cavo M12 in canalina; colore del LED di
   uscita (di solito giallo/arancio) — dipende dal costruttore. *Limite:* SET-TIPO.md non letto in questo collaudo.

## Esito del timing
`python3 ~/.claude/skills/vessel/scripts/timing.py caso-01_parlato.txt --voce lipsync --precedente 56`

| Scena | Parole | Sec | Clip |
|---|---:|---:|---:|
| S1 | 12 | 4.8 | 6 |
| S2 | 16 | 6.4 | 8 |
| S3 | 12 | 4.8 | 6 |
| S4 | 18 | 7.2 | 8 |
| S5 | 14 | 5.6 | 6 |
| S6 | 16 | 6.4 | 8 |
| S7 | 20 | 8.0 (+2 s CTA) | 10 |

**🟢 VERDE** · 52 s di montato (fascia 48-56 ✅) · nessuna scena oltre 10 s ✅ · 4 s di differenza dal reel precedente (56 s) ✅ ·
81 crediti su 7 clip. Le clip coincidono con le durate dell'input.
Iterazioni: S7 era 23 parole, poi 22 (⛔ oltre 10 s con i 2 s di CTA) → 20 parole togliendo «Vuoi impararlo?».
Controlli non fatti qui: lettore fresco (lo fa chi ha lanciato il collaudo) e verità contro la scheda (scheda assente).

---

# v2 dopo i controlli
Input: lettore fresco (si perde in S5; sul campo monterebbe il capacitivo ovunque senza regolarlo = errore plausibile non
corretto) + verifica di Granite (F1-F4 confermati, F5 condensa/schiuma NON confermato → tolto).

**Filo (aggiornato):** la scelta la fa il materiale: l'induttivo vede solo il metallo e la sua distanza dipende da *quale*
metallo; il capacitivo sente quasi tutto, **anche la parete**, quindi va regolato.
**Errori plausibili corretti:** (1) «è metallo, quindi lo vede alla distanza scritta» → S3-S4; (2) «sente quasi tutto, quindi lo
monto ovunque» → S6.

## Il parlato v2
| Scena | Clip | Battuta |
|---|---:|---|
| S1 | 6 s | Sembrano uguali. Ma quando passa questo pezzo, quale dei due lo vede? |
| S2 | 8 s | È metallo: induttivo. Ci passo la chiave: l'acciaio assorbe energia dal suo campo magnetico. LED acceso. |
| S3 | 4 s | Passa il pezzo… LED spento. Ma non era metallo? |
| S4 | 8 s | Metallo sì, ma alluminio. La distanza di intervento vale per l'acciaio: qui è meno di metà. Lo avvicino. |
| S5 | 6 s | Lo vede. Seguiamo il pezzo al lavaggio: l'acqua deve arrivare a questo segno. |
| S6 | 10 s | L'acqua non è metallo: capacitivo. Ma sente quasi tutto: l'acqua è sotto, e lui è acceso. Vede il vetro. Abbasso la sensibilità: spento. |
| S7 | 10 s | Prima guardi di cosa è fatto: se è metallo, quale. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza. |

## Cosa cambia e perché
- **S6 (8 → 10 s):** il dubbio entra dove nasce il secondo errore: lui stesso dice «sente quasi tutto», poi il LED è
  acceso anche se l'acqua è sotto, perché vede il vetro. La sensibilità diventa un gesto: «abbasso» col cacciavitino sul
  trimmer, poi il LED si spegne. È la mossa 5, la 6 e la F3 di Granite (sensibilità troppo alta = resta acceso, va ridotta).
- **S5:** il cambio di set ora ha una causa che si vede («Seguiamo il pezzo al lavaggio») e «qui» diventa «questo segno»:
  una tacca di livello sul vetro, indicata dal dito.
- **S3 (6 → 4 s):** tolgo «e il LED resta» per pagare i 2 s di S6 e tenere il montato a 52 s (4 s di distanza dal
  reel precedente da 56 s). S1, S2, S4 e S7 restano come nella v1.

## Piano: cosa cambia rispetto alla v1
| Scena | Cosa si vede | Componente | Stato | Gesto → parola |
|---|---|---|---|---|
| S3 | Primo piano radente sul LED, il pezzo passa | induttivo sulla staffa, invariato | nastro in marcia; LED resta spento | alza lo sguardo → «metallo?» |
| S5 | La camera segue il pezzo dal nastro dentro la lavatrice a tunnel; stacco sulla finestra di vetro della vasca con la tacca di livello | — (taglio di set) | nastro in marcia; acqua **sotto** la tacca | indica la tacca → «segno» |
| S6 | Finestra della vasca, primo piano di lato | capacitivo **già montato** su staffa, faccia appoggiata al vetro all'altezza della tacca | acqua sotto la tacca; LED **acceso** (vede il vetro) → **spento** dopo la regolazione | gira il trimmer col cacciavitino → «abbasso»; il LED si spegne su «spento» |

## Deviazioni v2
- **S4 tiene «meno di metà»:** Granite lo conferma per gli induttivi standard (fattore alluminio 0,35-0,45, Eaton p. 1-28);
  quello in scena è standard, non a fattore 1, e il numero è quello che un tecnico si ricorda. Se Saverio preferisce
  stare più largo: «l'alluminio lo vede solo più da vicino» (stesse parole, stesso tempo).
- **S2 «Ci passo la chiave»:** invariata. La chiave si vede in scena, quindi per il coordinatore non è un difetto del parlato.
- **S6 con 23 parole in 10 s:** sopra la soglia di ~22 della pagina 3, ma il timing è verde (9,2 s).
- **La regolazione non mostra l'acqua che sale:** in una clip da un fotogramma c'è un solo cambio di stato (acceso → spento).
  Che dopo «si accende con l'acqua» lo si capisce dal contrasto con «l'acqua è sotto».

## Fatti v2 (da Granite)
F1 distanza riferita all'acciaio Fe 235, alluminio 0,35-0,45 (Eaton p. 1-28; limite: non vale per i modelli a fattore 1) ·
F2 meccanismo induttivo (p. 1-27) · F3 capacitivo attraverso pareti non metalliche se il materiale dietro ha permittività più
alta, pareti fino a 10-20 mm, sensibilità con potenziometro/teach-in, troppo alta = resta acceso (SICK; ifm) · F4 vetro ~5,
acqua ~80, il capacitivo vede anche i metalli (Eaton p. 1-34) · F5 condensa/schiuma: NON confermato, non usato.
Ancora da verificare: colore del LED di uscita e posizione rispetto a SET-TIPO.md (non letto).

## Esito del timing v2
`timing.py caso-01_parlato_v2.txt --voce lipsync --precedente 56`
S1 12 parole/6 s · S2 16/8 · S3 9/4 · S4 18/8 · S5 13/6 · S6 23 parole, 9,2 s/clip 10 · S7 20 parole, 8,0 s + 2 s CTA/10.
**🟢 VERDE** · 52 s di montato · nessuna scena oltre 10 s ✅ · fascia 48-56 ✅ · 4 s dal precedente ✅ · 81 crediti su 7 clip.
Avviso, non blocca: 14 frasi su 21 sotto le 6 parole.
