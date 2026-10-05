# Caso 02 · «Ho perso un nodo. Tutta la rete lo sta cercando» · storia e parlato · 2026-10-04 · Vessel

Slot lunedì 18:30 → componente con la faccia, in panico: parla **il PLC** (lip-sync), Mister Automation in scena, muto.
Keyword NOME. Scheda: `caso-02_fatti.md` (Granite). Copione: `caso-02_parlato.txt`.

## 1. Filo ed errore plausibile
**Filo:** il PLC ritrova un nodo dal **nome**, non dall'IP; un ricambio nuovo di fabbrica il nome non ce l'ha, quindi non
risponde finché non glielo dai tu (o, se c'è la topologia e il nodo lo supporta, glielo dà il PLC).
**Errore plausibile** (scheda, errori 1-2): «È identico e l'IP è giusto: se non risponde, è rotto anche il ricambio.»
L'errore opposto (scheda, errore 3: «senza nome non lo trova MAI») lo chiude S6.

## 2. Parlato
| Scena | Clip | Battuta | Fatti |
|---|---:|---|---|
| S1 | 6 s | «Ho perso un nodo! Il ricambio è identico… ma non risponde.» | termine «guasto stazione» → «nodo perso»; F1, F2 |
| S2 | 8 s | «"L'IP è giusto, sarà rotto anche questo!" No: i nodi li riconosco dal nome. L'IP glielo do io.» | errore plausibile 1-2; F3, F4 |
| S3 | 8 s | «Nuovo di fabbrica, il nome non ce l'ha. E il LED verde? Dice solo che il cavo c'è.» | F2, F9 |
| S4 | 8 s | «Rotto o senza nome? Dal PC lo vedi: rotto sarebbe "non raggiungibile"; questo è "pronto per l'assegnazione".» | F8, F10 |
| S5 | 8 s | «Lo scegli dal MAC, lo fai lampeggiare per essere sicuro che sia lui, gli dai il nome… Ritrovato!» | F6, F7 (+F3: dal nome lo riconosce) |
| S6 | 8 s | «Con la topologia nel progetto e un nodo che lo supporta, il nome glielo davo io. Qui mancava.» | F11 (con i suoi limiti: topologia + supporto; ricambio nuovo già detto in S3) |
| S7 | 10 s | «Prima il nome, poi l'IP. Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.» | F3 (IP ricavato dal nome) · CTA + tagline |

Legami: S1→S2 MA (il dubbio) · S2→S3 MA (il nuovo non ce l'ha) · S3→S4 QUINDI (rotto o senza nome?) · S4→S5 QUINDI ·
S5→S6 MA (potevo farlo da solo) · S6→S7 QUINDI (sintesi). Non usati: F5, F12-F15, numeri, tutto il «non confermato».

## 3. Piano scena per scena (corto)
**Mondo IBRIDO**: fabbrica vera + ologrammi mai toccati (un'etichetta-nome sopra ogni nodo; in S6 la mappa delle porte).
**Set unico**: linea di imbottigliamento (SET-TIPO §1), quadro a bordo linea sul lato manutenzione, sportello aperto verso
il corridoio. In basso su guida DIN: il PLC con la faccia, accanto tre nodi I/O identici e lo switch; cavi RJ45 connessi ai
due capi (scheda: caso «nel quadro», l'unico confermato). Mister Automation davanti al quadro, portatile collegato con un cavo
allo switch. Linea ferma: nastro fermo, beacon rosso in cima alla riempitrice. Sulle spie del nodo si mostra solo il LED di
link (le altre spie sono «non confermato»).

| Scena | Cosa si vede · stato | Gesto ↔ parola |
|---|---|---|
| S1 | Quadro aperto, PLC in panico. Etichette-nome accese sopra due nodi, **vuota** sopra il ricambio; LED di link verde. Beacon rosso sullo sfondo | PLC sgrana gli occhi su «perso» |
| S2 | Mister Automation col portatile davanti al quadro; PLC verso di lui | PLC scuote la «testa» su «No» |
| S3 | Primo piano porta RJ45 del ricambio: cavo inserito, LED di link verde fisso; etichetta vuota sopra | M.A. sfiora il connettore su «cavo» |
| S4 | Schermo del portatile (interfaccia generica, nessun marchio): riga del nodo «pronto per l'assegnazione» | M.A. indica la riga su «pronto» |
| S5 | Fra i tre nodi identici lampeggia il LED di link del ricambio; l'etichetta-nome si accende | M.A. preme invio su «nome»; PLC sorride su «Ritrovato» |
| S6 | Ologramma della mappa porta per porta, grigio e tratteggiato (nel progetto non c'è) | PLC fa una smorfia su «mancava» |
| S7 | Tre etichette accese, beacon verde, nastro in moto (persone fuori dalle parti in moto) | M.A. chiude il portatile su «NOME» |

## 4. Deviazioni (con motivo)
- **56 s di montato**, al bordo alto della fascia: con il reel precedente a 52 s le uniche durate che stanno in 48-56 e
  distano almeno 4 s sono 48 e 56; 48 avrebbe tolto S6, che è il limite onesto del filo (errore 3 della scheda).
- **S2 cita fra virgolette il dubbio** (del tecnico/di chi guarda) in bocca al PLC: resta una voce sola per clip.
- **S4 usa i nomi di stato di un software preciso** (limite di F8): il parlato non nomina il software e lo schermo è generico.
- **S2 «L'IP glielo do io»**: vale nel caso normale (limite di F3: alcuni dispositivi prendono l'IP in altro modo). Detto
  senza riserva perché è il caso del reel; se Saverio vuole la riserva, costa una clip.
- **S6 «glielo davo io»**: imperfetto colloquiale per «glielo avrei dato»; tono parlato.

## 5. Controlli
- **Verità**: ogni battuta ha i suoi F nella tabella; nessun numero, niente dal «non confermato».
- **Lettore fresco**: non lanciato (giro del banco di prova, niente subagenti).
- **Timing** (`timing.py caso-02_parlato.txt --voce lipsync --precedente 52`): 🟢 VERDE · clip 6+8+8+8+8+8+10 = **56 s** ·
  nessuna scena oltre i 10 s · 4 s dal precedente · 117 parole · 85 crediti su 7 clip. Spia di mestiere: 19 frasi, 12 sotto
  le 6 parole, nessuna sopra le 25.
  Prima stesura: 141 parole, S7 oltre i 10 s (la CTA prende +2 s), 🔴 ROSSO → tolte ridondanze (S1, S4 «c'è, gli manca il
  nome», S6 «da solo»), non accelerata la voce.
