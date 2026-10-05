# Tono alla cieca — skill finale contro skill del 4/10
Per ogni caso due versioni, A e B: una è della skill del 4/10, l'altra della skill finale. Tutte e due sono **primi passaggi**,
prima delle correzioni chieste dai controlli. Leggile ad alta voce e scegli quella che suona più come Mister Automation (o
«nessuna»). La chiave è in `CHIAVE-tono.md`: aprila solo dopo.

## Caso 1 · induttivo o capacitivo
**A**
1. Il PLC deve sapere quando passa questo pezzo, senza toccarlo. Sembrano uguali: induttivo o capacitivo?
2. È metallo, quindi induttivo. Fa un campo magnetico alternato: la chiave ne assorbe energia e il sensore commuta.
3. Passa il pezzo… resta spento. Ma è metallo anche lui!
4. Metallo sì, ma alluminio. La distanza dichiarata vale per l'acciaio: sull'alluminio è meno della metà. Lo avvicino… e lo vede.
5. Seguiamo il pezzo in lavatrice. Lì il PLC vuole sapere il livello dell'acqua nella vasca.
6. L'acqua non è metallo: qui va il capacitivo. Sente poco il vetro, tantissimo l'acqua. Lo regolo: col solo vetro, resta spento.
7. Prima guardi di cosa è fatto, poi scegli. Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Quando passa questo pezzo, il PLC deve saperlo. Senza toccarlo. Induttivo o capacitivo?
2. È metallo, quindi induttivo. Fa un campo magnetico alternato: il metallo che ci entra ne assorbe energia, e l'uscita commuta.
3. La chiave d'acciaio la vede. Ma passa il pezzo… il LED resta spento. Lo cambio?
4. Cambiarlo non serve: è alluminio. Nell'induttivo standard la distanza di intervento vale per l'acciaio. Sull'alluminio è meno della metà.
5. Quindi lo avvicino. Ripassa il pezzo… acceso.
6. In lavatrice il PLC vuole il livello. Ma l'acqua non è metallo: serve il capacitivo.
7. Fa un campo elettrico e sente ogni materiale: il vetro poco, l'acqua tantissimo. Così la vede attraverso il vetro.
8. Ma anche il vetro lo sente: se è troppo sensibile, resta acceso senz'acqua. Abbasso la sensibilità finché si spegne.
9. Quindi: prima guardi di cosa è fatto, poi lo provi su quel materiale.
10. Vuoi impararlo? Commenta SENSORE. Mr. Automation Italia: dove la curiosità diventa competenza.

## Caso 2 · il nodo PROFINET
**A**
1. Ho perso un nodo! Me l'hanno cambiato con uno identico, e non lo trovo.
2. Lo so cosa pensi: il LED è verde, gli rimetti lo stesso IP e riparte.
3. Verde vuol dire solo che il cavo c'è. Io i nodi non li cerco per IP: li cerco per nome.
4. Uno nuovo di fabbrica il nome non ce l'ha. E qui non posso darglielo io: il progetto non dice a quale porta è attaccato.
5. Col PC lo vedi: c'è, col suo indirizzo MAC, ma senza nome. Non è guasto.
6. Fai lampeggiare il LED per essere sicuro che sia lui, poi gli scarichi il nome del progetto: quello del vecchio.
7. Eccolo! L'ho trovato dal nome. L'IP glielo do io.
8. Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Ho perso un nodo! Il tecnico l'ha cambiato con uno nuovo, identico. Non lo trovo.
2. Lui pensa: stesso modello, stesso IP, deve andare. Ma l'IP glielo do io. Io il nodo lo cerco per nome.
3. All'avvio cerco ogni nodo del mio progetto col suo nome. E uno nuovo di fabbrica un nome non ce l'ha.
4. Eppure il LED della porta è verde! È guasto anche lui? No: quel verde dice solo che il cavo c'è.
5. Sul PC leggi «pronto per l'assegnazione», non «non raggiungibile». Gli manca solo il nome.
6. Il tecnico lo sceglie dal MAC, lo fa lampeggiare e gli dà il nome del mio progetto. Eccolo! Lo ritrovo.
7. Stesso modello non basta: serve lo stesso nome. Vuoi impararlo? Commenta NOME. Mr. Automation Italia: dove la curiosità diventa competenza.

## Caso 3 · il buffer di diagnostica
**A**
1. Stanotte questa linea si è fermata tre volte. E io so a che ora.
2. Sono il PLC. Ogni volta che vado in STOP, scrivo una riga nel buffer di diagnostica, con data e ora.
3. Il mio web server l'hanno attivato, l'orologio l'hanno regolato: apri un browser e scrivi il mio indirizzo IP.
4. Ecco le tre righe di STOP. Guardi quella in alto: «È la prima fermata, no?»
5. La prima? Non è detto. La prima te la dice l'ora, non la posizione: è quella dell'una e dodici.
6. Ma leggimi prima di spegnermi: quando il buffer è pieno, le righe nuove cancellano le vecchie, e da spento tengo solo le ultime.
7. L'ora, non la riga. Vuoi imparare a leggere la diagnostica? Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.

**B**
1. Stanotte questa linea si è fermata tre volte. E io so a che ora.
2. Sono il PLC: ogni STOP lo scrivo nel mio buffer di diagnostica, con data, ora e cosa è successo.
3. Per leggerlo non ti serve il software. Se il mio web server è attivo, scrivi il mio IP nel browser.
4. Eccole. Tu leggi la riga in cima e pensi: «È partito tutto da qui.»
5. Semmai è finito qui. Nel mio buffer la più recente sta in cima: l'ultima cosa successa, non la prima.
6. Quindi guarda l'ora: la prima fermata è delle due e dieci. Tocchi la riga e leggi i dettagli.
7. L'ora, non la posizione. Commenta DIAGNOSI. Mr. Automation Italia: dove la curiosità diventa competenza.
