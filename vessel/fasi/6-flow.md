# Passo 6 · L'animato in Google Flow (Hypnosis)

> Questa pagina la legge **Hypnosis**, il subagente di Flow. Vessel lo lancia due volte: **giro A** = JSON di tutte le clip,
> validazione, upload dei plate e clip pilota S1; **giro B** (dopo l'ok di Saverio sulla pilota) = tutte le altre clip.
> Input: percorso del master (parlato approvato, piano scena per scena, timing, keyword) e della cartella `plate/`.

## Intento
Una clip per scena, che anima il plate approvato **col minimo movimento**: il personaggio dice la sua battuta e fa un solo gesto
piccolo, tutto il resto resta com'è. Il 30/9 le clip con più azioni in fila hanno rotto l'impianto e la coerenza; quelle col
plate fermo e un gesto hanno retto.

## Cosa consegni
- `02_Script_Reel/prompt/<slug>_prompt-veo.md`: un blocco ```json per clip, sopra ognuno `parole · secondi · durata`.
- Esito di `valida-veo.py` (deve uscire 🟢), clip lanciate, durate, crediti, retry.
- Giro A: «Pilota S1 lanciata in Flow, cartella <slug>: guardala tu». Giro B: «N clip lanciate. Guardale tu; dimmi quale
  rifare e cosa non va, oppure "abbiamo finito"». Le clip non si aprono per «verificarle»: le guarda Saverio.

## Prima di Flow
1. **Guarda i plate uno alla volta a piena risoluzione** (`Read`) e scrivi per ognuno: chi è in campo · da che lato ·
   espressione · dove sono le mani · cosa può muoversi · che testo c'è (di solito solo il logo MA). Il JSON descrive il plate
   **com'è**, non come era nel piano.
2. **Durate** dal master (`timing.py`): lo scalino sopra il parlato misurato, 4 / 6 / 8 / 10 s; la clip della CTA ha già i ~2 s
   in più. Se una battuta sta a margine zero: `delivery` svelto e «never cut the last words».
3. **Un JSON per clip** nella forma di `modelli/lock-flow.md` (chiavi in quell'ordine). I testi fissi (`character_lock`,
   `voice`, `voice_lock`, `lip_sync`, i 10 negativi anti-fotoreale, l'apertura di `action`, l'inizio di `hard_constraint`) si
   copiano **identici** in tutte le clip: il motore non ha memoria, e un aggettivo diverso cambia il timbro o il volto.
4. `python3 ~/.claude/skills/vessel/scripts/valida-veo.py prompt/<slug>_prompt-veo.md --keyword <KEYWORD>` sul file con
   **tutte** le clip → 🟢 (su una clip sola senza la keyword, `--keyword` non si passa). Poi ogni JSON si comprime su una
   riga, pronto da incollare.

## Come si fa bene
1. **Un fotogramma per clip, Fine vuoto.** Da un set all'altro si passa col taglio in montaggio. Un fotogramma di fine si usa
   solo per un passaggio fisicamente vero nello stesso set, con la stessa luce: altrimenti l'impianto si trasforma a metà clip.
2. **Un gesto piccolo, legato a una parola**, e al massimo **un evento** dichiarato (un LED che si accende, la keyword).
   Ciò che il plate mostra già fatto (sensore montato, LED acceso) resta così, e uno stato importante si blocca in tre campi:
   `locked_plate`, `lights`, `negative`.
3. **Si ferma il gesto, mai il braccio**: la posa del plate è il punto di partenza e le braccia restano vive per tutta la clip.
   Se nel plate si vede un braccio solo, la frase delle braccia vive parla di quello e l'altro resta fuori vista.
   Il moto continuo che il plate già racconta (nastro in marcia, acqua che ondeggia) può continuare: si dichiara in `lights`
   («the only moving things are …»). Quello che resta fermo sono gli oggetti di scena: niente che entra, esce o si sposta.
4. **La voce resta ferma, l'intonazione va in `delivery`**: tono discendente come base, enfasi misurata («about ten percent
   louder on X, no more»), pause scritte in `timing` coi secondi, ultimo tratto «NO WORDS — …, mouth closed».
5. **`camera` è una frase sola**: «Locked-off camera. Nothing else.» oppure «Very slow push-in. Nothing else.». Due movimenti
   insieme deformano il plate.
6. **La keyword CTA è un ologramma che compare esattamente sulla parola detta**, resta circa un secondo e sparisce; non c'è a
   inizio né a fine clip, ed è l'unico testo nuovo del reel. Si mette dove il plate ha una mano aperta, sennò sopra l'oggetto.
   Esempio completo: `esempi/flow/S7-cta.json`.
`negative` = i 10 anti-fotoreale + gli errori concreti **di questo plate** (oggetti che compaiono, LED che si spegne, attrezzo
che lascia la mano…) + voce e camera. Si negano azioni, non stati («static shot» fa vibrare l'inquadratura).

## In Flow
`flow.google.com` → progetto **«Mr. Automation. Academy»** → cartella del mese → cartella `<slug>` (se manca: `+` → nuova
collection → `⋮` → Rename). Upload dei plate e giro di ogni clip: `modelli/chrome.md` § Google Flow.
1. **Pilota = S1 da sola.** La lanci, controlli solo che la tile non sia «Failed», e torni da Vessel.
2. **Dopo l'ok di Saverio**, S2…Sn una dopo l'altra mentre le precedenti generano.
3. **Dopo l'ultima clip lanciata ti fermi.** Se Saverio chiede di rifarne una: un campo cambiato togliendo movimento, una clip,
   di nuovo stop. Clip deformata: un retry identico; se il difetto torna, si toglie movimento.
Crediti (Omni 1.1 Flash · 9:16 · 720p · x1): 4 s = 7 · 6 s = 10 · 8 s = 12 · 10 s = 15. Il banner «running low on credits» è
solo un avviso. Versione precedente di un'immagine in Flow: «Mostra cronologia» → click normale sulla miniatura.

**Fine fase**: quando Saverio dice «abbiamo finito», nel master si scrive lo stato di Flow (cartella, clip, durate, crediti,
retry, loop sì/no) e «Prossimo passo: Vessel fase 3».
