# Comandi di Chrome (estensione Claude in Chrome) — ChatGPT e Flow

## Strumenti — caricati tutti insieme, in una sola ToolSearch
```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__file_upload,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__browser_batch,mcp__claude-in-chrome__read_network_requests
```
Si lavora in una scheda nuova. Il testo si legge con `get_page_text` (a risposta finita: due letture uguali a 10 s di distanza);
un'immagine si guarda con `zoom` o, meglio, scaricata e aperta con `Read`.

## ChatGPT
- **Allegare**: `find "file input for attaching files to the message"` → il primo ref (quello del composer) → `file_upload` coi
  percorsi assoluti (anche più file insieme) → attesa 4 s, poi il testo.
- **Scrivere e inviare**: `javascript_tool` con
  `const t=`<il prompt>`; const ed=document.querySelector('#prompt-textarea')||document.querySelector('div.ProseMirror[contenteditable="true"]'); ed.focus(); document.execCommand('insertText', false, t);`
  → `key Return` → circa 60 s di attesa («Creating image»).
- **Due immagini a confronto** («Image 1 is better / Image 2 is better»): sul personaggio nuovo sceglie Saverio; sulle altre
  si sceglie quella giusta per posizione e stato.

## Scaricare le immagini dalla chat
Le `img` dentro `main` più grandi di 500 px sono le generate, in ordine di conversazione; ognuna compare più volte (anteprime).
Primo giro, solo guardare:
```js
const imgs=[...document.querySelectorAll('main img')].filter(i=>i.naturalWidth>500 && i.naturalHeight>500);
imgs.map((i,n)=>[n,i.naturalWidth,i.naturalHeight,(i.alt||'').slice(0,30)])
```
Secondo giro, scaricare con i nomi giusti (si compila `plan` con gli indici visti):
```js
const imgs=[...document.querySelectorAll('main img')].filter(i=>i.naturalWidth>500 && i.naturalHeight>500);
const plan=[[0,'S1_madre'],[3,'griglia-storyboard']];
const out=[];
for(const [n,name] of plan){
  try{ const r=await fetch(imgs[n].src); const b=await r.blob();
    const u=URL.createObjectURL(b); const a=document.createElement('a'); a.href=u;
    a.download='<SLUGCORTO>_'+name+'.png'; document.body.appendChild(a); a.click(); a.remove();
    out.push([name,b.size,b.type]); await new Promise(r=>setTimeout(r,700));
  }catch(e){out.push([name,'ERR',String(e)])}
}
out
```
I file arrivano in `~/Downloads/<SLUGCORTO>_*.png` → si spostano in `04_Riferimenti_Visivi/<slug>/plate/S1_madre.png`, `S2.png`…,
`griglia-storyboard.png`, e `04_Riferimenti_Visivi/<slug>/copertina.png`. Controllo: `file` + dimensioni (tipiche: plate 941×1672,
griglia 1024×1536).

## Logo in post (`scripts/fix_logo.py`)
Sostituisce la «MA» disegnata da ChatGPT col monogramma vero, in prospettiva sui 4 angoli, cancellando la scritta vecchia.
```
uv run --with numpy --with opencv-python-headless python ~/.claude/skills/vessel/scripts/fix_logo.py src.png out.png TLx TLy TRx TRy BRx BRy BLx BLy [--pad 6] [--dark] [--erase 8 numeri] [--white 150] [--tint 0.5]
```
`--dark` = M scura su superficie chiara · `--erase` = zona della scritta vecchia se diversa · `--tint` = il logo prende la luce
della scena. Coordinate: si leggono sul PNG a piena risoluzione; per un logo largo `w` il rettangolo è alto circa `w/2,38`.
Fa solo il monogramma (non il logo completo del cappellino). L'originale si tiene in `plate/_originali/`.

## Google Flow — caricare i plate (la finestra di scelta file non si manovra)
1. **Prima** di cliccare Upload, con `javascript_tool`:
```js
window.__capturedInputs=[];const oc=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'){window.__capturedInputs.push(this);if(!this.isConnected){document.body.appendChild(this);}this.id='claude-file-input-'+window.__capturedInputs.length;this.style.cssText='position:fixed;top:0;left:0;width:200px;height:40px;opacity:0.01;z-index:99999';this.setAttribute('aria-label','claude file input');return;}return oc.apply(this,arguments)};'hooked'
```
2. `+` (in alto a destra) → «Upload»: la finestra non si apre, l'input resta nella pagina.
3. `find "claude file input"` → ref → `file_upload` coi percorsi assoluti dei plate. **Una chiamata per gruppo fino a 10 MB**,
   fuori da `browser_batch` (il batch somma i byte).
4. L'upload è lento: circa 2 minuti a gruppo, la barra ferma al 99% è normale. La pagina non si ricarica, sennò l'upload si
   perde. Controllo: le tile mostrano le immagini (oppure `read_network_requests` con `urlPattern: "maseQ"` → 200).
5. Se l'hook non prende l'input (input creato prima dell'hook): si ricarica **prima** di qualsiasi upload e si rifà l'hook.

## Google Flow — il giro per ogni clip
Impostazioni (chip in basso a destra): Video · Fotogrammi · 9:16 · Omni 1.1 Flash · 720p · x1 · **durata della clip**.
**Inizio** → «Select a frame image» → il plate dalla lista → **zoom sull'anteprima a destra** (la lista si riordina a ogni
apertura) → «Aggiungi al prompt». **Fine resta vuoto.** Click nel campo «What do you want to create?» → incolla il JSON
compatto (una riga) → zoom sul chip della durata (il popover a volte non si apre al primo click e resta la durata di prima) →
freccia di invio. Frame sbagliato già aggiunto: click sulla miniatura accanto a Inizio per toglierlo.
Tile «Failed — unusual activity» = blocco anti-automazione, non addebitato → icona ↻ sulla tile, una volta.
