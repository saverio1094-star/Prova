# Caso 03 · Storia e parlato · «Stanotte questa linea si è fermata tre volte. E io so a che ora.» · 2026-10-04 · Vessel
Slot lunedì 18:30 → componente con la faccia: **il PLC parla in prima persona**, al tu. Keyword DIAGNOSI. Lip-sync.
Fonte unica dei fatti: `caso-03_fatti.md` (Granite).

## Filo ed errore plausibile
**Filo:** il PLC scrive ogni suo STOP nel buffer di diagnostica con data e ora, e lo leggi dal browser; ma la riga in cima
è l'ultima cosa successa, non la causa: per trovare la prima fermata guardi l'ora, non la posizione.
**Errore plausibile:** «la prima riga è la causa» (scheda, errore 1, corretto da F3).

## Parlato
| Scena | Clip | Battuta | Fatti usati |
|---|---:|---|---|
| S1 | 6 s | Stanotte questa linea si è fermata tre volte. E io so a che ora. | F1, F2 (tre STOP = tre voci con l'ora) |
| S2 | 8 s | Sono il PLC: ogni STOP lo scrivo nel mio buffer di diagnostica, con data, ora e cosa è successo. | F1 (data, ora, descrizione), F2 (passaggio a STOP) |
| S3 | 8 s | Per leggerlo non ti serve il software. Se il mio web server è attivo, scrivi il mio IP nel browser. | F5 (senza software), F7 (di fabbrica spento → «se è attivo»), F8 (IP nel browser) |
| S4 | 6 s | Eccole. Tu leggi la riga in cima e pensi: «È partito tutto da qui.» | errore plausibile 1; F6 (la pagina mostra le voci con data e ora) |
| S5 | 8 s | Semmai è finito qui. Nel mio buffer la più recente sta in cima: l'ultima cosa successa, non la prima. | F3 (detto del buffer, «nel mio buffer»: vedi Verificato e no) |
| S6 | 8 s | Quindi guarda l'ora: la prima fermata è delle due e dieci. Tocchi la riga e leggi i dettagli. | F1 (ora per voce), F6 (si clicca una riga → dettagli sotto); «due e dieci» = valore di storia |
| S7 | 8 s | L'ora, non la posizione. Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza. | sintesi di F3+F6; CTA e tagline da LIBRERIA-CTA |

Catena: S1 →(come lo sai?) QUINDI S2 →(e dove lo leggo?) MA S3 → QUINDI S4 → MA S5 → QUINDI S6 → QUINDI S7.
Dubbio e risposta: «È partito tutto da qui» → «Semmai è finito qui» (riprende la parola, chiude sull'effetto).

## Piano scena per scena
**Mondo:** IBRIDO — fabbrica vera + un ologramma delle righe del buffer sopra la CPU (mai toccato).
**Set:** fine linea packaging (SET-TIPO §3, senza la cella robot in campo): nastro → formatrice → nastratrice; quadro di
bordo macchina a bordo linea, lato manutenzione, sportello aperto verso il corridoio. CPU con la faccia su guida DIN **in
basso** nel quadro, accanto a moduli I/O e switch; relè di sicurezza accanto; drive e contattori nella zona di mezzo;
alimentatore 24 V e sezionatore in alto. Cavo dalla porta PROFINET **sul fondo** della CPU allo switch, e dallo switch
in canalina verso la rete dell'impianto. Logo MA sulla CPU. Nessun marchio.
**Stato:** mattina, linea ripartita: CPU in RUN, **LED verde fisso** (F13) in tutte le scene; nastro in moto lento sullo
sfondo, beacon verde. Mister Automation c'è ma non parla: tiene lo smartphone collegato alla rete dell'impianto.

| Scena | Cosa si vede | Gesto ↔ parola |
|---|---|---|
| S1 | quadro aperto, la CPU guarda in camera; linea che gira dietro, beacon verde; luce dell'alba | strizza l'occhio su «a che ora» |
| S2 | primo piano della CPU; sopra, ologramma di tre righe che si scrivono una dopo l'altra, ognuna con data e ora | gli occhi seguono la riga che si scrive su «scrivo» |
| S3 | Mister Automation davanti al quadro, smartphone in mano; la CPU in secondo piano, il cavo dal fondo allo switch | il pollice digita l'indirizzo su «scrivi il mio IP» |
| S4 | sopra la spalla: lo schermo con la pagina «Buffer di diagnostica» (senza marchi), righe con data e ora; la CPU dietro | il dito si posa sulla riga in cima su «in cima» |
| S5 | di nuovo la CPU con l'ologramma della colonna di righe; la riga in alto si accende come «ultima» | la CPU alza gli occhi verso la riga in alto su «in cima» |
| S6 | schermo: il dito scende alla riga delle 02:10 (STOP), la tocca, sotto si apre il pannello dei dettagli; la CPU annuisce | il dito tocca la riga su «tocchi la riga» |
| S7 | la CPU in camera, quadro aperto, linea che gira; gag ologramma «DIAGNOSI» | la CPU fa l'occhiolino su «DIAGNOSI» |

Righe di storia sullo schermo (S4/S6): STOP 02:10, RUN, STOP 03:40, RUN, STOP 05:25, RUN 06:05 in cima. Il contenuto dei
dettagli non si mostra leggibile (che contenga il motivo dello STOP non è confermato).

## Verificato e no
- Ogni affermazione del parlato sta nella scheda (F1, F2, F3, F5, F6, F7, F8). Nessun numero (50/500 voci) perché la CPU
  in scena non ha modello. Non usati: F4 (buffer pieno), F9/F10 (orologio e UTC), F11, F12 — un'idea per reel.
- **Rischio da guardare:** F3 («più recente in cima») è confermato per il buffer, non per la pagina web (F6 PARZIALE). Per
  questo S5 lo dice del buffer («nel mio buffer») sull'ologramma, non sullo schermo, e la regola operativa (S6-S7) è
  «guarda l'ora, non la posizione», che regge in ogni caso. Lo schermo di storia mette comunque la più recente in alto:
  se Saverio vuole zero rischio, in S4/S6 lo schermo non deve far vedere l'ordine.
- «So a che ora» vale con l'orologio della CPU impostato bene (F9): nel parlato non c'è, la storia lo dà per fatto.
- Lettore fresco (Aqua Regia) **non lanciato**: questo giro chiedeva niente subagenti.

## Deviazioni
- **CTA senza frase d'invito** («Commenta DIAGNOSI.» secco dopo la sintesi): con «Vuoi impararlo?» S7 passava a 10 s e il
  montato a 54 s, a 2 s dal reel precedente (56 s). Tenuta la sintesi, tolto l'invito.
- **S2 «ogni STOP lo scrivo»** invece di «ogni volta che vado in STOP»: stessa ragione di tempo (S2 da 10 a 8 s).

## Esito del timing
`timing.py caso-03_parlato.txt --voce lipsync --precedente 56` → 🟢 VERDE.
Clip 6+8+8+6+8+8+8 = **52 s** di montato (fascia 48-56 ✅, nessuna scena oltre 10 s ✅), 4 s meno del reel precedente
(al limite della spia). 118 parole, 80 crediti su 7 clip. Il controllo veloce (parole ÷ 2,0) dà 59 s: S3 (8,0 s su clip
da 8) è la battuta più a rischio se la voce va più lenta.
