# Tono alla cieca — 5/10/2026
Per ogni caso due versioni, A e B. Una è del 4/10, l'altra di oggi: non è detto quale. Leggile ad alta voce e scegli quella
che suona più come Mister Automation (o «nessuna delle due»). La chiave è in `CHIAVE-tono.md`: aprila solo dopo aver scelto.

## Caso 1 · induttivo o capacitivo
**A**
1. Questo pezzo passa sul nastro, e il PLC deve saperlo senza toccarlo. Induttivo o capacitivo?
2. È metallo, quindi induttivo: fa un campo magnetico. Ci passo una chiave d'acciaio, ne assorbe energia, e lui si accende.
3. Ma passa il pezzo… spento. È alluminio. Allora non lo vede: ci vuole il capacitivo?
4. No: lo vede, ma più vicino. Su un induttivo standard, la distanza di intervento dichiarata vale per l'acciaio. Sull'alluminio è meno della metà.
5. Quindi non lo cambio: lo avvicino. Stesso pezzo… acceso.
6. In lavatrice serve il livello dell'acqua, e l'acqua non è metallo: quindi capacitivo. La sente attraverso questo vetro: ha una permittività molto più alta.
7. Prima il materiale, poi sensore e distanza. Vuoi impararlo? Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Il PLC deve sapere quando passa questo pezzo, senza toccarlo. Sembrano uguali: induttivo o capacitivo?
2. È metallo, quindi induttivo. Fa un campo magnetico alternato: la chiave ne assorbe energia e il sensore commuta.
3. Passa il pezzo… resta spento. Ma è metallo anche lui!
4. Metallo sì, ma alluminio. La distanza dichiarata vale per l'acciaio: sull'alluminio è meno della metà. Lo avvicino… e lo vede.
5. Seguiamo il pezzo in lavatrice. Lì il PLC vuole sapere il livello dell'acqua nella vasca.
6. L'acqua non è metallo: qui va il capacitivo. Sente poco il vetro, tantissimo l'acqua. Lo regolo: col solo vetro, resta spento.
7. Prima guardi di cosa è fatto, poi scegli. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

## Caso 2 · il nodo PROFINET
**A**
1. Ho perso un nodo! Il tecnico l'ha cambiato con uno nuovo, identico. Non lo trovo.
2. Lui pensa: stesso modello, stesso IP, deve andare. Ma l'IP glielo do io. Io il nodo lo cerco per nome.
3. All'avvio cerco ogni nodo del mio progetto col suo nome. E uno nuovo di fabbrica un nome non ce l'ha.
4. Eppure il LED della porta è verde! È guasto anche lui? No: quel verde dice solo che il cavo c'è.
5. Sul PC leggi «pronto per l'assegnazione», non «non raggiungibile». Gli manca solo il nome.
6. Il tecnico lo sceglie dal MAC, lo fa lampeggiare e gli dà il nome del mio progetto. Eccolo! Lo ritrovo.
7. Stesso modello non basta: serve lo stesso nome. Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Ho perso un nodo! L'hanno sostituito con uno identico. Lo cerco su tutta la rete… e non risponde.
2. «È guasto anche il nuovo?» No. Il PC non dice «non raggiungibile», dice «pronto per l'assegnazione»: il MAC c'è, il nome no.
3. «Il nome? Ma l'IP gliel'ho messo uguale!» Non basta: io i nodi li riconosco dal nome. L'IP glielo do io, dopo.
4. Ma nuovo di fabbrica, il nome non ce l'ha. Se non glielo do io da solo, glielo dai tu.
5. Lo scegli dal MAC, fai lampeggiare il suo LED per sicurezza, e gli assegni il nome che ha nel progetto.
6. Eccolo! Lo riconosco e gli do l'IP. Prima il nome, poi l'IP.
7. Vuoi imparare le reti? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

## Caso 3 · il buffer di diagnostica
**A**
1. Stanotte questa linea si è fermata tre volte. E io so a che ora.
2. Sono il PLC: ogni STOP lo scrivo nel mio buffer di diagnostica, con data, ora e cosa è successo.
3. Per leggerlo non ti serve il software. Se il mio web server è attivo, scrivi il mio IP nel browser.
4. Eccole. Tu leggi la riga in cima e pensi: «È partito tutto da qui.»
5. Semmai è finito qui. Nel mio buffer la più recente sta in cima: l'ultima cosa successa, non la prima.
6. Quindi guarda l'ora: la prima fermata è delle due e dieci. Tocchi la riga e leggi i dettagli.
7. L'ora, non la posizione. Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Stanotte questa linea si è fermata tre volte. E io so a che ora.
2. Sono la CPU. Ogni volta che vado in STOP scrivo una riga nel mio buffer di diagnostica, con l'ora.
3. Non ti serve il software di programmazione: il web server l'hanno attivato. Apri il browser e scrivi il mio IP.
4. Ecco il buffer. La prima riga dice: passaggio a STOP, 4:51. E pensi: «È cominciato tutto lì.»
5. È la prima che leggi, non la prima che è successa. Guarda l'ora: la prima fermata è alle 23:40.
6. Vai alla riga delle 23:40 e cliccala: sotto compaiono i dettagli. È da lì che cominci a cercare il perché.
7. Guarda l'ora, non la posizione. Vuoi impararlo? Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.
