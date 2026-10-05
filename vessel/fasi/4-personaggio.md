# Passo 4 · Personaggio (solo se manca)

## Intento
Avere un personaggio riconoscibile e coerente in tutte le immagini e le clip. Si fa **solo** se il reel ha bisogno di un
personaggio che non c'è in `04_Riferimenti_Visivi/personaggi/` (indice in `personaggi/LEGGIMI.md`) o di una sua variante.

## Cosa ricevi
Dalla scheda dei fatti: com'è fatto il componente e da cosa lo riconosce un tecnico. Una foto vera, se Saverio la dà.

## Cosa consegni
`04_Riferimenti_Visivi/personaggi/<nome>_anchor.png` (fondo bianco, figura intera a 3/4) + una riga in `personaggi/LEGGIMI.md`
(data, 3 tratti che lo identificano) + la riga nel master. Lo sceglie Saverio vedendolo.

## Come si fa bene
1. **Un personaggio che esiste si allega, non si ridescrive.** Mister Automation = `serafino_anchor.webp` (cappellino MA,
   occhiali da vista, occhiali protettivi al collo, polo nera MA, pantaloni neri). Il secondo personaggio umano è il capo
   manutenzione (`capo-manutenzione_anchor.png`, e `_schiena.png` quando sta di spalle). Mr. PLC, la scatola, non è il tecnico.
   Descriverlo a parole fa nascere un altro personaggio; l'anchor allegato no.
2. **Parti da «da cosa lo riconosce un tecnico?»**: le parti che lo identificano (porte, LED, ghiere, display) e le proporzioni.
   Le proporzioni si **allegano** (foto o figura d'ingombro della scheda), non si scrivono in millimetri. Senza foto, le parti
   si prendono dal «com'è fatto» della scheda dei fatti: resistenza, vibrante, telecamera e relè sono venuti bene così.
3. **Tre reference col loro ruolo, in un messaggio**: CORPO (foto vera o figura d'ingombro) · MARCHIO (`brand/logo.png`) ·
   STILE (l'anchor più simile per forma, di solito `mr-m12_anchor.webp`). Ricetta completa in `modelli/chatgpt.md` § Personaggio.
4. **Stile dei componenti**: render 3D Unreal Engine 5 / Fortnite, occhi grandi con palpebre, sopracciglia, braccine e gambette
   sottili nere con mani a tre dita, materiali veri. **Una bocca sola**: porte e display non sono bocche.
5. **Il logo MA è stampato sul corpo** come serigrafia integrata, al posto delle scritte del produttore; nessun altro segno.
6. **Mister Automation è un trentenne con barba corta tutta scura.** Se un'immagine lo invecchia: «stessa immagine, cambia
   SOLO il volto: trentenne, barba corta tutta scura, niente grigio, pelle liscia».

Anchor col logo vecchio da ri-brandizzare (es. `mr-servomotore_vecchio-logo_con-albero.png`): «Sostituisci SOLO il badge vecchio
col logo MA allegato, stampato sul corpo come serigrafia integrata, sotto la stessa luce: niente piastra, niente adesivo. Tutto
il resto identico.»
