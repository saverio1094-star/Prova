# Scheda dei fatti · «Sensore induttivo o capacitivo: quale scegliere per rilevare il pezzo?» · Granite (verifica del 4/10)

> Ricostruita il 5/10 dai fatti F1-F5 che Granite ha verificato il 4/10 (`esiti-2026-10-04/caso-01_parlato.md`, «Fatti v2»).
> Per il giro del 5/10 la sezione «errore plausibile» è lasciata vuota apposta: lo trova chi scrive.

**Copertura del tema:** buona per i due sensori · colore del LED e posizione esatta rispetto a SET-TIPO: non verificati.

## Fatti (solo questi entrano nel parlato)
| # | Fatto, per il caso delimitato | Fonte | Limite che va con il fatto | Stato |
|---|---|---|---|---|
| F1 | La distanza di intervento dichiarata di un induttivo è riferita all'acciaio (Fe 235). Sull'alluminio il fattore di correzione è 0,35-0,45: la distanza utile è 0,35-0,45 volte quella dichiarata (meno della metà). | Eaton, manuale sensori, p. 1-28 | vale per gli induttivi **standard**; non vale per i modelli a **fattore 1**, che hanno la stessa distanza su tutti i metalli | CONFERMATO |
| F2 | L'induttivo genera un campo magnetico alternato davanti alla faccia sensibile; il metallo che entra nel campo ne assorbe energia (correnti indotte) e l'uscita del sensore commuta. | Eaton, p. 1-27 | solo metalli | CONFERMATO |
| F3 | Il capacitivo rileva un materiale anche attraverso una parete non metallica (es. vetro, plastica) se il materiale dietro ha permittività più alta della parete; pareti fino a circa 10-20 mm. La sensibilità si regola con potenziometro o teach-in: se è troppo alta il sensore resta acceso (vede la parete). | SICK; ifm | dipende da spessore e materiale della parete e dal modello | CONFERMATO |
| F4 | Permittività relativa: vetro circa 5, acqua circa 80. Il capacitivo rileva anche i metalli. | Eaton, p. 1-34 | valori indicativi | CONFERMATO |
| F5 | Condensa o schiuma sulla parete disturbano il capacitivo. | — | — | NON CONFERMATO |

## Termini veri
- distanza di intervento (distanza dichiarata) · fattore di correzione · faccia sensibile · sensibilità (potenziometro / teach-in)

## Errore plausibile di chi guarda
*(lasciato a chi scrive in questo giro)*

## Dove sta davvero il componente
Induttivo su staffa fissata alla sponda del nastro, faccia verso il passaggio del pezzo · capacitivo all'esterno della parete
di vetro della vasca, all'altezza del livello da rilevare. Altezze e lato esatti: non verificati su SET-TIPO.

## Non confermato — il parlato non lo usa
- F5 condensa/schiuma · colore del LED di uscita
