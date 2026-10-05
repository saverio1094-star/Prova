# Passo 7 · Consegna (Offering)

> Questa pagina la legge **Offering**, il subagente della consegna. Vessel lo lancia con: percorso del master, slot di
> pubblicazione dalla coda, e se serve il foglio di editing (se il master non lo dice, Vessel lo chiede a Saverio in una riga).

## Intento
Dare a chi pubblica e a chi monta **tutto quello che serve, pronto da copiare**, nel formato che Saverio usa: due RTF a blocchi
e un PDF. Chi pubblica è il socio, Serafino: deve poter fare tutto dal telefono senza chiedere niente.

## Cosa consegni
Sorgenti in `02_Script_Reel/prompt/`, uscite in `02_Script_Reel/_export/`:
1. `<slug>_PACCHETTO.md` → `_export/<slug>_PACCHETTO-PUBBLICAZIONE.rtf` (per chi pubblica)
2. `<slug>_foglio-editing.md` → `_export/<slug>_EDITING-ASTRA.rtf` (per chi monta), **solo se serve**. Se il reel si monta a
   mano senza foglio, nel pacchetto entrano invece `🎼 Prompt musica` e `✂️ Foglio tagli musica`, subito dopo il nome traccia.
3. `<slug>_PIANO-LANCIO.md` → `_export/<slug>_PIANO-LANCIO.pdf` (per Serafino)
E a Vessel le 5 righe di consegna (in fondo a questa pagina).

## Come si fa bene
0. **Si parte solo da un master col parlato approvato da Saverio e la scheda dei fatti.** Se mancano, ti fermi e lo dici a
   Vessel: senza fatti verificati non si scrivono caption e messaggi che usciranno a nome del canale.
1. **Tutto esce dal master.** Titolo, slug, keyword, battute e durate si copiano, non si inventano. Se un campo manca:
   `⬜ manca nel master: <cosa>`. Un'informazione inventata in caption arriva a migliaia di persone.
2. **Il pacchetto ha i suoi blocchi in ordine fisso** (`## titolo con emoji` + testo): 📄 Nome file · 🖼️ Copertina (file già
   pronto) · 📝 Caption IG (2-3 righe, il tema nelle prime 150 battute, chiude con keyword + 👇) · #️⃣ Hashtag (3-5 di nicchia,
   italiano e inglese) · 🔎 Alt-text (1-2 frasi su cosa si vede, col tema dentro) · 🏷️ Argomenti (1-3, separati da « · ») ·
   🎵 Nome traccia (`<KEYWORD> — Mr Automation Academy (bed)`) · ▶️ Titolo YT (il tema nei primi 40 caratteri) · 📃 Descrizione YT
   (~200 parole che raccontano il reel, poi la CTA, la tagline e gli hashtag) · 📱 TikTok («Stesso video, stessa caption, stessi
   hashtag. Etichetta «contenuto generato con IA» attiva.») · 📅 Data di pubblicazione (lo slot della coda; se è già passato:
   «da decidere con Saverio, non pubblicare senza conferma») · 🧪 Trial (solo se il master dice TRIAL) · ℹ️ Note per chi pubblica
   (se la keyword non è fra quelle già usate in `ARCHIVIO-CONTENUTI.md` § Parole chiave, la nota dice «Keyword nuova: va
   configurata in ManyChat prima di pubblicare»; altrimenti «già configurata per i DM»).
   Modelli: `esempi/consegna/pacchetto_2026-09-28_rele.md` e `pacchetto-con-musica_2026-10-02_induttivo.md`.
3. **Caption e descrizione dicono solo cose che il reel e la scheda dei fatti dicono.** La descrizione YT può spiegare un po' di
   più, ma ogni frase in più viene dalla scheda, coi suoi limiti.
4. **La CTA chiede di commentare la keyword per arrivare al prossimo contenuto** (corsi, webinar). Niente date, prezzi, nomi di
   prodotto, materiali gratis: il link arriva in DM.
5. **Il piano di lancio ha 5 schede, sempre queste, in ordine di tempo**: 1 Subito: pubblica + Ripubblica · 2 +5 min: commento
   da fissare con keyword + 👇 · 3 +5 min: reel nel canale broadcast + messaggio · 4 primi 20 min: rispondi e risveglia ·
   5 entro 1 ora: 3 storie facoltative, un reel sì e uno no. In fondo le regole del canale. Modello:
   `esempi/consegna/piano-lancio_2026-09-28_rele.md`; decisioni del canale in `01_Piano_Editoriale/BROADCAST.md`.
6. **Il messaggio nel canale porta una cosa vera che nel reel non c'è** (un numero, la trappola, il punto esatto dove sta il
   componente), presa dalla scheda dei fatti, e una domanda a cui si risponde sotto il reel. Voce «noi», al massimo 3 paragrafi.
   Se la scheda non ha niente in più, nel canale si condivide solo il reel.

**Foglio di editing** (quando serve): struttura del modello `esempi/consegna/foglio-editing_2026-09-28_rele.md`, dati di questo
reel. Sottotitoli presi dal `line_it` delle clip: tutto maiuscolo, bold condensato, bianco con ombra, una parola per card in
arancione MA, 3-5 parole su una riga, card secche, centro a y ≈ 1160 (a y 1330 solo nelle scene dove a 1160 c'è un oggetto della
storia). Le clip si usano intere: se la voce scivola si spostano le card. A schermo si aggiungono solo i sottotitoli: keyword e
tagline sono già nelle clip. Musica: mood, 120 BPM (una battuta = 2 s), strumenti, sezioni da `[Intro]` a `[End]`, banda
300 Hz-3 kHz libera per la voce, niente secondi nel prompt (stanno nel foglio dei tagli); il carattere lo decide la recitazione:
reel comico, musica comica. Template: `esempi/consegna/musica-template.md`. Il finale in loop si copia dal master (lo decide la fase 2); se il master non lo dice, il finale non è in loop.

## Gli script
```
S=~/.claude/skills/vessel/scripts
python3 $S/rtf-consegna.py prompt/<slug>_PACCHETTO.md -o _export/<slug>_PACCHETTO-PUBBLICAZIONE.rtf
python3 $S/rtf-consegna.py prompt/<slug>_foglio-editing.md --editing -o _export/<slug>_EDITING-ASTRA.rtf
python3 $S/lancio-pdf.py prompt/<slug>_PIANO-LANCIO.md -o _export/<slug>_PIANO-LANCIO.pdf
```
`-o` va sempre messo (senza, il file esce in `prompt/` col nome sbagliato). Il PDF ha bisogno di Google Chrome in /Applications.
Controlli dopo: `textutil -convert txt -stdout <file.rtf> | head -40` (12-14 blocchi nel pacchetto) e il PDF aperto con `Read`
(schede e blocchi «COPIA E INCOLLA» ci sono). In `_export/` va solo quello che esce: un reel rimandato si rinomina `IN-PAUSA_…`.

## La consegna in chat (Vessel la gira a Saverio)
```
📦 <slug>_PACCHETTO-PUBBLICAZIONE.rtf   → a chi pubblica
🎬 <slug>_EDITING-ASTRA.rtf             → a chi monta (se c'è)
🚀 <slug>_PIANO-LANCIO.pdf              → a Serafino
📂 02_Script_Reel/_export/
Quando hai incollato tutto, scrivi «fatto» e chiudo.
```
