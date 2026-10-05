# Caso 01 · giro 2 · parlato (collaudo alla cieca)
Tema: «Sensore induttivo o capacitivo: quale scegliere per rilevare il pezzo?» · obiettivo: visualizzazioni qualificate e
salvataggi · stesse 7 scene e stessa storia del brief di Serafino · fatti: solo F1-F4 del caso.

## Filo ed errore plausibile
**Filo:** non sceglie il sensore il fatto che «è metallo»: guardi di cosa è fatto il pezzo, poi scegli e regoli.
L'induttivo vede l'alluminio solo più da vicino (meno della metà della distanza dichiarata); il capacitivo vede l'acqua
attraverso il vetro, ma va regolato perché il vetro da solo non lo accenda.
**Errore plausibile:** «induttivo = vede il metallo, punto» (corretto da S3-S4 con F1) e «capacitivo = vede tutto, lo monto
e basta» (corretto da S6 con F3-F4).

## Parlato
| Scena | Clip | Battuta |
|---|---:|---|
| S1 | 6 s | Il PLC deve sapere quando passa questo pezzo, senza toccarlo. Sembrano uguali: induttivo o capacitivo? |
| S2 | 8 s | È metallo, quindi induttivo. Fa un campo magnetico alternato: la chiave ne assorbe energia e il sensore commuta. |
| S3 | 4 s | Passa il pezzo… resta spento. Ma è metallo anche lui! |
| S4 | 8 s | Metallo sì, ma alluminio. La distanza dichiarata vale per l'acciaio: sull'alluminio è meno della metà. Lo avvicino… e lo vede. |
| S5 | 6 s | Seguiamo il pezzo in lavatrice. Lì il PLC vuole sapere il livello dell'acqua nella vasca. |
| S6 | 10 s | L'acqua non è metallo: qui va il capacitivo. Sente poco il vetro, tantissimo l'acqua. Lo regolo: col solo vetro, resta spento. |
| S7 | 10 s | Prima guardi di cosa è fatto, poi scegli. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza. |

Verità, battuta per battuta: S2 → F2 · S4 → F1 (0,35-0,45 = «meno della metà») · S6 → F3 + F4 · S1, S3, S5, S7 non
affermano fatti tecnici. Non usati: «campo elettrico» del capacitivo (non è nei fatti), i modelli «fattore 1» (veri, F1, ma
non entravano nel tempo), il capacitivo che vede anche i metalli (F4, non serve al filo).

## Piano scena per scena (corto)
**Mondo:** REALE. Due set nella stessa linea: nastro trasportatore con la staffa del sensore sulla sponda → lavatrice pezzi
con la finestra di vetro sulla vasca. Si passa da uno all'altro seguendo il pezzo (S5). Linea in marcia per tutto il reel.
| Scena | Si vede | Componente e stato | Gesto ↔ parola |
|---|---|---|---|
| S1 | nastro in marcia, mezza figura; il pezzo d'alluminio arriva | i due sensori in mano a Mister Automation | alza i due sensori affiancati ↔ «Sembrano uguali» |
| S2 | staffa sulla sponda, mani da vicino | induttivo **già montato** sulla staffa, cavo in canalina; LED da spento ad ACCESO | passa la chiave d'acciaio davanti alla faccia sensibile ↔ «commuta» |
| S3 | primo piano radente sul LED | il pezzo d'alluminio passa nello stesso punto; LED SPENTO | si sporge, sorpreso ↔ «Ma è metallo» |
| S4 | stesso asse, camera verso il LED | induttivo spostato più vicino al passaggio sulla staffa; pezzo successivo → LED ACCESO | fa scorrere il sensore verso il nastro ↔ «Lo avvicino» |
| S5 | camera segue il pezzo fino alla lavatrice | capacitivo **già montato** all'esterno della finestra di vetro, all'altezza del livello; LED ACCESO (acqua presente) | indica la vasca ↔ «lavatrice» |
| S6 | finestra della vasca, primo piano di lato | capacitivo sul vetro, acqua sopra la sua altezza; LED ACCESO | cacciavite sul trimmer di sensibilità ↔ «Lo regolo» |
| S7 | di nuovo al nastro, stesso asse di S1 | induttivo acceso al passaggio; scritta SENSORE | guarda il pezzo successivo prima di parlare ↔ «di cosa è fatto» |
Altezze e lato esatti dei due sensori: **non confermati** (servono scheda di Granite e SET-TIPO, non letti in questo collaudo).

## Deviazioni (con motivo)
- **Sensori già montati** (S2, S5): nel brief Mister Automation monta l'induttivo e «tira fuori» il capacitivo. La pagina del
  passo vuole il componente già al suo posto: montarlo in scena chiede a Flow tre azioni in una clip.
- **S4 un gesto solo**: «allenta, avvicina, stringe» diventa «fa scorrere il sensore più vicino», stesso motivo.
- **S6 aggiunge la regolazione**: è la stessa storia (capacitivo sul vetro, LED acceso) con un gesto in più, il trimmer.
  Serve a chiudere la seconda metà dell'errore plausibile («lo monto e basta»), che il brief lasciava aperta (F3).
- **S6 senza «campo elettrico»**: il brief lo diceva, ma non è fra i fatti verificati; resta solo ciò che F4 conferma.
- **S1 riprende il gancio di Astra** («Sembrano uguali») dentro la domanda del brief: il gancio promette la scelta, S7 la chiude.
- **S3 a 4 s** (era 6): il montato a 54-56 s sarebbe stato uguale al reel precedente (56 s); la battuta è una reazione, regge
  le frasi corte.
- **Durate:** 6+8+4+8+6+10+10 = 52 s (il brief: 52 s con S7 a 10, ma con le battute nuove si sforava).

## Esito del timing
`timing.py caso-01_giro2_parlato.txt --voce lipsync --precedente 56` → 🟢 **VERDE**
- nessuna scena oltre i 10 s ✅ · montato 52 s (fascia 48-56) ✅ · 4 s di differenza dal precedente (56 s) ✅
- costo animazione: 81 crediti su 7 clip
- attenzione: S3 è 4,0 s di parlato in una clip da 4 s (al limite), e il controllo veloce (parole ÷ 2) dà 58 s: se la voce
  va più lenta di 2,5 parole/s, S3 è la prima da accorciare.
- Controlli non fatti in questo collaudo: lettore fresco (Aqua Regia, vietato lanciare subagenti) e verifica sulla scheda di
  Granite (sostituita da F1-F4).
