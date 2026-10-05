<example>
# Il metodo di Astra su due temi nuovi — PNP/NPN e il relè termico
Scritti da Astra (l'assistente di Serafino) come dimostrazione di metodo, **non sono reel usciti né approvati**: servono a vedere
come si decide cosa dire prima di scrivere, come si delimita il caso a voce e come si annota la battuta con l'alternativa scartata.
Le durate sono le sue ipotesi (70-90 e 80-100 s), non la nostra misura: i reel di Mr. Automation stanno di solito sui 48-56 s.
CTA di Astra («salva questo reel»): la nostra è in pagina 3.

**Prima della prima battuta (B, il termico)** — chi deve capire: chi riconosce i componenti ma non il circuito interno ·
cosa distingue alla fine: riarmo e rimozione della causa · caso: relè a bimetallo con comando a contattore · semplificazione
che porterebbe a sbagliare: «il termico è il termometro del motore» · indispensabile: meccanismo, comando, limite diagnostico,
condizioni del riarmo (per questo il budget è lungo).

## A · «PNP o NPN: cosa cambia?»
A1 Il sensore vede il pezzo. Ma il PLC riceve il segnale?
A2 PNP e NPN ti dicono come lavora l'uscita, non che materiale rileva il sensore.
A3 Prendiamo un sensore a tre fili, alimentato a ventiquattro volt in continua.
A4 Quando l'uscita si attiva, un PNP la collega al positivo. Un NPN la collega allo zero volt.
A5 La corrente deve comunque fare un percorso completo: nel primo caso attraversa l'ingresso del PLC verso lo zero volt; nel secondo arriva dal positivo, attraversa l'ingresso e torna allo zero attraverso il sensore.
A6 Ecco quando conta: se sostituisci il sensore, l'ingresso deve essere compatibile. Stesso connettore non basta.
A7 E PNP non significa normalmente aperto: quello ti dice quando si attiva l'uscita. Sono due caratteristiche diverse.
A8 Prima di scegliere il ricambio, confronta lo schema del sensore con quello dell'ingresso.

## B · «Il termico è scattato: lo riarmi o prima controlli?»
B1 È scattato il termico. Premi reset e riparti?
B2 Prima cerca il motivo. Il reset riabilita il relè; non elimina la causa dello scatto.
B3 Nel termico a bimetallo, la corrente riscalda delle lamelle. Se il riscaldamento supera il limite d'intervento, il relè scatta.
B4 Nel classico comando con contattore, apre il circuito della bobina: il contattore si disinserisce e toglie alimentazione al motore.
B5 Ma questo non ti dice ancora perché è successo. Il carico è aumentato? Manca una fase? La taratura è corretta per quel motore e quel circuito?
B6 Prima dei controlli sulla macchina, mettila in sicurezza e impedisci riavvii inattesi.
B7 Si cerca e si risolve la causa, poi si rispettano raffreddamento e procedura di riarmo del costruttore. Alzare la taratura solo per non farlo scattare può lasciare il motore senza la protezione corretta.
B8 La domanda, quindi, è: perché è scattato?

## Le note battuta per battuta (cosa fa · alternativa scartata)
| | Cosa fa | Scartata, e perché |
|---|---|---|
| A1 | apre il divario fra rilevare e ricevere | «Oggi parliamo di PNP e NPN»: annuncia, non apre niente |
| A3 | fissa il caso prima di parlare di positivo e zero | una regola detta come valida per qualunque sensore |
| A4 | la differenza essenziale, con due frasi parallele | «uno dà corrente e l'altro no»: falso |
| A5 | chiude il circuito, così positivo e zero non restano etichette | la lista dei colori dei fili: suggerisce un cablaggio universale |
| A6 | trasforma il meccanismo nel criterio per il ricambio | «il PNP è migliore»: compatibile non vuol dire migliore |
| A7 | l'equivoco NA/NC, dopo che PNP/NPN è capito | spiegare tutte le uscite: aprirebbe un altro reel |
| B2 | il criterio utile subito | tenere la risposta fino alla fine |
| B3 | perché la corrente fa scattare, delimitato al bimetallo | «sente la temperatura del motore»: è un'altra misura |
| B4 | dallo scatto all'arresto, per la catena di comando | «stacca direttamente tutta la potenza»: inesatto in quel circuito |
| B5 | il limite diagnostico dopo il meccanismo | «il motore è sicuramente sovraccarico» |
| B7 | causa, ripristino, condizioni di riarmo, in ordine | «aspetta cinque minuti» (manca il modello) · «alza un po' gli ampere» (toglie la protezione) |

**Le mosse.** Il caso si nomina a voce prima della regola («Prendiamo un sensore a tre fili», «Nel termico a bimetallo»,
«Nel classico comando con contattore»): così la regola che chi guarda si porta via è vera nel suo caso. Il limite che cambia la
decisione resta anche se toglierlo renderebbe la frase più secca. Ogni battuta risponde alla domanda lasciata dalla precedente.
</example>
