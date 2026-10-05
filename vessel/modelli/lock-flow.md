# Forma del JSON per Flow e testi fissi

Un JSON per clip, chiavi piatte, **in quest'ordine** (lo controlla `valida-veo.py`):
`clip · duration_s · locked_plate · character_lock · voice · voice_lock · lip_sync · line_it · delivery · timing · action · camera · lights · sound_design · hard_constraint · negative`
Solo quando servono: `mascot_face` (componente con la faccia) · `voice_placement` (voce fuori campo).

| Campo | Cosa ci va |
|---|---|
| `clip` | nome della scena («S6 — IL CAPACITIVO · GIÀ MONTATO») |
| `duration_s` | 4 / 6 / 8 / 10, dal timing del master |
| `locked_plate` | «Use the attached frame as the locked plate for the whole clip: …» + i 4-6 elementi del plate **così come si vedono**, mani comprese + «Do not invent a different plant.» Con un evento: «WITH ONE DECLARED EXCEPTION, listed in action: …» |
| `character_lock` | solo il personaggio (aspetto + STYLE LOCK), mai la posa. Identico in tutte le clip |
| `voice` · `voice_lock` | identici parola per parola in tutte le clip del reel |
| `lip_sync` | frase fissa (sotto) |
| `line_it` | la battuta italiana alla lettera, con la punteggiatura (`…` = pausa vera) |
| `delivery` | come la dice: tono discendente, enfasi «about ten percent, no more», ritmo. Un umore da solo non basta |
| `timing` | prosa coi secondi: ogni frase, ogni silenzio e cosa fa; ultimo tratto «NO WORDS — …, mouth closed» |
| `action` | apertura fissa + **un** gesto piccolo legato a una parola + al massimo un evento dichiarato |
| `camera` | una frase sola |
| `lights` | luce del plate + «the only moving things are …» + gli stati che non cambiano |
| `sound_design` | tappeto d'ambiente a parole + «No music.» |
| `hard_constraint` | inizio fisso + cosa vale per questa clip + «The MA logo stays exactly as in the plate.» |
| `negative` | i 10 anti-fotoreale + gli errori concreti di questo plate + voce e camera |

Esempi completi che hanno retto: `esempi/flow/S6-un-gesto.json` (clip normale) · `S4-un-evento-led.json` (un LED che si accende
sulla parola) · `S7-cta.json` (keyword-ologramma + tagline).

## Testi fissi — si copiano identici
**`character_lock` di Mister Automation** (la parte descrittiva si ricontrolla sull'anchor e sul plate: un dettaglio che nel plate non si vede, come il logo sulla maglietta coperta, si toglie; da «STYLE LOCK —» alla fine
non si tocca: da quando c'è, il personaggio non è più diventato un umano reale). Nel prompt il personaggio si chiama Serafino:
è un nome interno per Flow, nel parlato non compare.
> Same man as the source frame, Serafino: same young face, dark trimmed beard with no grey, transparent-framed glasses, black MA cap, black MA t-shirt with clear safety goggles hanging around his neck, black trousers and black boots. The MA logo on the cap and on the shirt stays identical for the whole clip. Do not redesign him, do not age him. His face stays three-quarter toward camera, never pure profile. STYLE LOCK — this is a stylised 3D game-engine render in the Unreal Engine 5 / Fortnite look, NOT live action: the man is a STYLISED 3D CHARACTER with the slightly oversized head, the large expressive eyes, the smooth clean skin with no pores and no realistic wrinkles, the soft rounded shapes and the clean stylised shading he already has in the plate. The plant around him stays photoreal industrial, but HE never does. His proportions, head size, eye size and skin must stay identical to the plate in every single frame: animate his PERFORMANCE, never his DESIGN, and never let him drift toward a photorealistic human being.

**`voice`** (gli aggettivi di tono si scelgono per il reel, es. «lightly ironic» al posto di «clear and friendly», poi restano
fermi in tutte le clip):
> Serafino's voice: one male Italian voice, a young technician. Native Italian, natural Italian cadence, declarative falling intonation, clear and friendly, never cartoonish, never robotic, never salesy. Reproduce this wording exactly in every clip and do not reinterpret it.

**`voice_lock`**
> This reel has ONE fixed voice and it never changes from clip to clip: SERAFINO, exactly as described in voice. SAME SPEAKER, SAME TIMBRE, SAME PITCH from the first frame to the last. No second speaker, no narrator layered over him, no voice change part-way through.

**`lip_sync`**
> Serafino is on camera and speaking: his mouth moves in sync with the Italian line, naturally, with the small jaw and cheek movements of real speech. In the silences his mouth closes and rests.

**I 10 negativi anti-fotoreale**, sempre in testa a `negative`:
> "photorealistic human", "live-action face", "realistic human skin texture", "realistic pores and wrinkles", "the character drifting toward photoreal", "losing the stylised proportions", "the head becoming realistically proportioned", "the eyes shrinking to realistic size", "uncanny realistic face", "a different man"

**Apertura di `action`**
> Animate the plate as it is, with the minimum of movement and in the most linear way: he speaks, and only the one small gesture described here happens. Every object stays exactly where it is in the plate for the whole clip — nothing enters the frame, nothing leaves it, nothing appears, disappears or changes place. No walking, no new task, no change of set, no change of framing.

**Braccia vive** (in `action`)
> BOTH ARMS ARE ALIVE AND CONNECTED TO HIS SHOULDERS: they move together, from the shoulder, with soft elbows, small and continuous, following the rhythm of the sentence, never thrown wide, never identical twice. NEVER leave one arm locked while the other moves.

**Inizio di `hard_constraint`**
> SAY THE LINE ONCE, no repeat, no loop. Never cut the last words: the whole line fits inside the clip, at a brisk natural pace. The short pauses are REAL SILENCE — do not fill them with words, breath sounds or muttering. EXACTLY ONE VOICE in this clip: Serafino.

**`mascot_face`** (componente con la faccia)
> The mascot has EXACTLY ONE mouth. Any display panel on its body is a BLANK SCREEN — no eyes, no nose and NO MOUTH inside it. Never draw, reveal or animate a second mouth or any facial feature inside it.

Per un componente-personaggio il `character_lock` descrive il suo corpo (es. «Same IO-Link master mascot as the source frame:
same orange rectangular body with the round metal M12 ports and the small green and yellow LEDs, same two big cartoon eyes and
one cartoon mouth, same white-and-orange MA logo in the middle of the body, same black rubbery arms and legs and black boots.
The MA logo stays identical for the whole clip.») e `voice`/`voice_lock` descrivono la sua voce, sempre generata da Flow.
La voce viene sempre da Flow, anche fuori campo: due motori diversi danno due timbri.
