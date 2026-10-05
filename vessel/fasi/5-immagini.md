# Passo 5 · Storyboard e immagini (Euclid)

> Questa pagina la legge **Euclid**, il subagente che lavora in ChatGPT nel Chrome di Saverio. Vessel lo lancia due volte:
> **giro A** = madre + griglia; **giro B** (dopo che Saverio ha approvato la griglia) = singole + copertina.
> Input del giro A: percorso del master (parlato, piano scena per scena, mondo e set), scheda dei fatti, anchor da allegare.
> Input del giro B: le correzioni di Saverio sulla griglia, se ci sono.

## Intento
Trasformare il piano scena per scena in immagini che un tecnico guarda senza trovare niente di storto, e che Flow può animare
con un solo gesto: prima una **griglia con tutte le scene**, che Saverio approva vedendola, poi un fotogramma 9:16 per scena
(il «plate») e la copertina.

## Cosa consegni
- Giro A: `04_Riferimenti_Visivi/<slug>/plate/S1_madre.png` e `griglia-storyboard.png`, il link della chat ChatGPT, la
  **scheda del set** scritta nel master, e una riga per immagine «cosa si vede» (chi è in campo · lato · espressione · mani ·
  cosa è acceso · che testo c'è).
- Giro B: `plate/S2.png … Sn.png`, `04_Riferimenti_Visivi/<slug>/copertina.png`, logo sistemato dove serve, riga «cosa si vede»
  per ogni plate, conteggio delle generazioni.

## Come si lavora in ChatGPT
Progetto **MR. AUTOMATION ACADEMY — CREATIVE LAB** (`https://chatgpt.com/g/g-p-6aa1cfdf0cc08191a926ff19ca967087/project`),
**una chat nuova per reel** (link nel master). Comandi di Chrome (allegare, scrivere, scaricare) in `modelli/chrome.md`.
Testi dei messaggi in `modelli/chatgpt.md`; esempi veri riusciti al primo colpo in `esempi/immagini/2026-10-02_induttivo.md`.
Le immagini si guardano a piena risoluzione (download + `Read`), non in miniatura.
Il download dalla chat è già autorizzato da Saverio quando approva il parlato; i file vanno da `~/Downloads` alla cartella del reel.

## Come si fa bene
1. **La madre (S1) nasce da un brainstorming senza generare.** Si manda a ChatGPT parlato, vincoli e la tua ipotesi di regia
   e gli si chiede di demolirla, proporre 3 alternative e classificarle per «chi non sa niente capisce subito, senza audio» e
   «regge come ancora per tutte le altre scene». Si sceglie la prima, anche con innesti. La madre è l'ancora di stile,
   personaggio e set: se è debole, tutto il reel lo è.
2. **Si scrive lo stato, non l'umore**: cosa è acceso e di che colore, cosa è spento, cosa scorre. Il modello prende le parole
   alla lettera; «atmosfera tesa» non dice niente, «colonna luminosa accesa ROSSA, nastro fermo» sì. Luce: industrial
   cinematic, capannone luminoso con lucernari e neon, né scuro né infantile; rosso e verde solo come stato.
3. **Il componente sta dove lo trova un manutentore, già montato**, all'altezza e dal lato della scheda dei fatti. Prima di
   dire che un'immagine va bene, guardala come un tecnico: altezza e lato del componente contro la scheda del set.
   Il 2/10 un sensore più alto dei pezzi e uno sulla sponda sbagliata hanno costretto Saverio a rifare due plate a mano.
4. **La griglia ha tutte le scene**: una sola immagine 2:3, S1 (la madre) in cima a tutta larghezza, sotto 3 righe da 2
   riquadri verticali. Ogni riquadro: la battuta fra virgolette · camera · primo piano · il personaggio con **un verbo** in
   maiuscolo e le mani · cosa è acceso o spento. **Un set per riquadro.** Si corregge sulla griglia, una correzione per
   messaggio con «tutti gli altri riquadri restano identici»; le singole partono solo dalla griglia approvata.
5. **Il plate si pensa già per l'animazione**: componente montato, una posa da cui parte un solo gesto, nessuna azione a
   metà; ciò che in video dovrà comparire (numeri, keyword) nel plate è vuoto: fumetto senza caratteri, mano libera nella CTA.
   Ogni oggetto in mano è **impugnato**: «stretto nella sinistra, dita chiuse attorno al corpo, il cavo che pende dal pugno».
6. **Personaggio a 3/4 col volto verso camera**, sempre allegato con l'anchor e mai ridescritto. «Guarda lontano» si fa con
   lo sguardo. Un secondo personaggio può stare di spalle solo col suo anchor di spalle.

**Singola** = «SCENA n = il riquadro <posizione> della griglia, 9:16 a piena risoluzione, stesso personaggio e stesso set
<della madre | dell'ancora del set N>» + camera + mani + stato. Un set nuovo ha come ancora la prima singola che ci entra.
Posa o orientamento di un componente si scrivono giusti nel primo prompt: se esce storto si rigenera da zero (un ritocco
conserva la geometria sbagliata). Una correzione per messaggio, frase secca + «tutto il resto identico».

**Copertina**: allegate le `copertina.png` dei due reel usciti prima + `brand/logo.png`. Testo = la domanda del gancio, dettata
esatta (riga 1 bianca, riga 2 giallo-arancio), logo in alto al centro, personaggio grande in basso a 3/4, oggetto della storia
grande, **dominante di colore diversa** dalle due copertine allegate (due copertine uguali di fila hanno fatto crollare le views
da 9.046 a 1.314).

**Scheda del set** (nel master, subito dopo la madre): inventario chiuso (elemento · dove · altezza · stato) · cosa non c'è ·
planimetria in 3 righe · CAM1 = madre, CAM2… (focale · altezza · distanza · direzione · ordine dei piani). Esempio riuscito:
`esempi/immagini/2026-10-02_induttivo.md` § Scheda del set. Settore che manca in `SET-TIPO.md` → Planimetrie `d1f8acfd`.

## Generazioni e logo
- Si punta a una generazione per immagine; la seconda è l'eccezione; alla terza ti fermi e lo dici a Vessel.
- ChatGPT sbaglia spesso la M del logo: non si rigenera, si corregge in post con `scripts/fix_logo.py` (istruzioni nel file e
  in `modelli/chrome.md` § Logo). L'originale si tiene in `plate/_originali/`.
- Cosa riportare a Vessel: percorsi, «cosa si vede» per ogni immagine, generazioni usate, dubbi veri (una riga ciascuno).
