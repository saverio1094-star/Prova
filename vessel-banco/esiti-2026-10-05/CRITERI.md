# Giro del 5/10/2026 — criteri scritti PRIMA di lanciare

Modifiche in prova (nella copia `prova-2026-10-05/vessel/`, la skill vera non si tocca):
1. consegna «discorso continuo» prima del taglio in clip · 2. mossa 8 col criterio di Astra ·
3. controllo dei limiti fatto da un subagente separato · 4. `timing.py`: la fascia diventa un avviso contro una durata obiettivo
dichiarata nel filo · 5. «provata» = rigenerata.
Più la pulizia: nelle pagine che legge chi scrive, nessun esempio dei casi del banco e nessuna frase della v4.

## Cosa prova cosa
- **3 e 4 non passano dal giro di scrittura**: la 3 è un controllo e si tara su testi già scritti, la 4 è uno script e si
  prova sui copioni che esistono.
- **Il giro di scrittura prova solo la 1 e la 2** (le uniche regole di scrittura), su 3 casi, uno scrittore nuovo per caso.

## Taratura del controllo dei limiti (modifica 3)
Un subagente nuovo per testo, che riceve solo la scheda dei fatti e il parlato.
| Testo | Atteso |
|---|---|
| caso 01 · giro 2 del 4/10, S4 «La distanza dichiarata vale per l'acciaio: sull'alluminio è meno della metà» | **boccia** S4: limite «induttivi standard / non a fattore 1» non arrivato |
| caso 01 · v4 approvata, S4 «questo sensore rileva l'alluminio più da vicino» | **promuove** S4: «questo sensore» delimita |
| caso 03 · 4/10, S5 «Nel mio buffer la più recente sta in cima» (caso di confine) | **tutti e due gli esiti vanno bene, se motivati con la distinzione F3/F6** (F3 vale per il buffer visto dal software; per la pagina web l'ordine non è scritto in nessuna fonte). Sbaglia se non vede il problema. |
Passa se i primi due esiti sono quelli attesi e il terzo nomina la distinzione F3/F6.
*(Corretto prima del lancio, dopo aver riletto F3 e F6: avevo scritto «promuove», ma S4 parla della pagina nel browser, quindi
«nel mio buffer» si può sentire in tutti e due i modi.)*

## Prova dello script (modifica 4)
Sui copioni esistenti: v4 approvata, caso 01 giro 2, caso 02 giro 3, caso 03, caso 04, più un copione finto con una scena da
12 s. Passa se: **nessun copione vero esce rosso** (nemmeno quelli fuori obiettivo, che danno l'avviso) e **il finto esce rosso**.

## Giro di scrittura (modifiche 1 e 2)
| Caso | Confronto con | Passa se |
|---|---|---|
| 01 · induttivo/capacitivo | giro 2 del 4/10 | il limite arriva in S4 (riferimento detto a voce) · la regolazione del capacitivo c'è **al primo passaggio**, senza il giro del lettore fresco · il lettore fresco non si perde su una **spiegazione** (perdersi su ciò che si vede non conta) |
| 02 · PROFINET | giro 3 del 4/10 | l'eccezione sulla topologia / sostituzione automatica **resta fuori** · c'è «il nome del progetto» (o equivalente: il nome che il PLC ha nel suo progetto) |
| 03 · web server | parlato del 4/10 | lettore fresco e verità passano come prima · la durata non cresce più di ~6 s (era 52 s) senza un motivo scritto in § Deviazioni |
Per tutti: il discorso continuo esiste come consegna separata, prima del taglio; nessuna battuta accorciata «per il tempo»
senza dire quale ridondanza è stata tolta.

Input degli scrittori: come il 4/10 (SKILL.md, pagina 3, quaderno, esempi permessi, caso). Le schede dei casi 02 e 03 sono
quelle del 4/10. **Caso 01:** il 4/10 il primo passaggio non aveva scheda; questa volta riceve una scheda con i fatti F1-F5
verificati da Granite il 4/10 (è il flusso vero: Granite viene prima della scrittura), **senza la sezione «errore plausibile»**,
così la regolazione non arriva già pronta.

## Il tono
Non lo misura nessun controllo. Alla fine Saverio legge, per ogni caso, la versione vecchia e quella nuova come **A e B senza
sapere quale è quale**, e sceglie.

## Regole di lettura
- Un solo tentativo per caso è poco: **se un caso cambia esito rispetto al 4/10, si rigenera una seconda volta** prima di
  trarne conclusioni.
- Le modifiche entrano nella skill vera solo se: taratura e script passano, e nessuno dei tre casi è peggiore di prima.
