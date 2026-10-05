# Ricerca · caso-03 «Stanotte questa linea si è fermata tre volte. E io so a che ora.» · 2026-10-04 · Granite

Buco trovato nel Brain 5b0396dd: l'unica fonte che tratta il buffer è l'Easy Book S7-1200 del 03/2014 (CPU di
vecchia generazione); le pagine Siemens sulla diagnostica già nel Brain sono vuote («Access Denied»). Mancavano:
web server disattivato di fabbrica, numeri per una CPU attuale, ora delle voci (orologio da impostare, fuso orario).

| # | Fonte | URL | Tipo | Esito |
|---|---|---|---|---|
| F1 | Siemens · Diagnostics Overview for SIMATIC S7-1200 and S7-1500, V1.0, 09/2018 | https://cache.industry.siemens.com/dl/files/283/109752283/att_963145/v2/109752283_Diagnostic_Overview_DOC_V10_en.pdf | documento di supporto del costruttore | caricata in Brain 2 (e2d27bcd) |
| F2 | Siemens · S7-1200 G2 Programmable Logic Controller System Manual, V1.0.1, 04/2025 | https://cache.industry.siemens.com/dl/files/293/109988293/att_1327503/v1/S71200_G2_system_manual_en-US_en-US.pdf | manuale del costruttore | caricata in Brain 2 (62fc1c26) |
| F3 | Siemens · S7-1500, ET 200SP, ET 200pro Web server Function Manual, 12/2014 | https://cache.industry.siemens.com/dl/files/560/59193560/att_109202/v1/s71500_webserver_function_manual_en-US_en-US.pdf | manuale del costruttore (è il manuale del web server a cui rimanda anche F2) | caricata in Brain 2 (914c1577) |

Scartate: manualslib.com (copia su sito terzo del manuale S7-1200), URL della versione 12/2025 del manuale G2
(«Not found»), blog e forum (dmcinfo, industrialmonitordirect, scribd, slideshare).

Verifica: la chat del Brain 2 ha risposto con errore («No parseable chunks in streaming chat response») a 5 tentativi,
anche col wrapper `nlm.py` e limitando le fonti. Le frasi usate nella scheda sono state controllate sul testo delle
fonti come lo restituisce il notebook stesso (`source fulltext -n ae39f678`). Da rifare la domanda di verifica quando la
chat del Brain 2 torna a funzionare.
