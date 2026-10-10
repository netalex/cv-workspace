# CV workspace

Archivio professionale e candidature su misura, gestiti con file leggibili.
Il profilo reale è consolidato con le conferme del 10 ottobre 2026.
`examples/demo` contiene esclusivamente dati fittizi. I CV importati sono inventariati
in `sources/inventory.yaml`; le evidenze sono in `profile/evidence.md`.
I record `to_verify` restano esclusi dalle evidenze utilizzabili nelle candidature.
Contatti e località del profilo sono ancora da completare.

## Avvio su Windows

Clonare il repository (oppure estrarre lo ZIP) e aprire la cartella `cv-workspace` in VS Code. Nel terminale
PowerShell, dalla radice del progetto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/cv.py doctor
.\.venv\Scripts\python.exe scripts/cv.py validate
.\.venv\Scripts\python.exe scripts/cv.py validate examples/demo --demo
.\.venv\Scripts\python.exe scripts/cv.py build examples/demo --demo
```

Non serve attivare l'ambiente virtuale né cambiare la execution policy.
Se il comando `python` non è disponibile, usare `py -3` per creare `.venv`.
Requisiti: Python 3.10+, Pandoc e LibreOffice. Unica dipendenza Python: PyYAML.
Il progetto non usa Node, API AI, chiavi o servizi a pagamento aggiuntivi.

`doctor` verifica che i programmi siano richiamabili. Su Windows lo script
preferisce `soffice.com`, l'eseguibile console di LibreOffice. Cerca nel PATH,
nelle cartelle standard e nelle installazioni Scoop utente/globali, includendo
`apps/libreoffice/current/LibreOffice/program`. Riconosce anche `SCOOP` e
`SCOOP_GLOBAL` per percorsi personalizzati.

Se necessario, impostare il percorso esplicito nella sessione PowerShell:

```powershell
$env:SOFFICE_PATH = 'C:\Users\netal\scoop\apps\libreoffice\current\LibreOffice\program\soffice.com'
# Adattare il percorso alla propria installazione.
# Per conservarlo nelle sessioni future:
[Environment]::SetEnvironmentVariable('SOFFICE_PATH', $env:SOFFICE_PATH, 'User')
# Solo se Pandoc non è nel PATH, impostare PANDOC_PATH al suo eseguibile.
```

Un override `SOFFICE_PATH` valido ha precedenza sulla ricerca automatica.
Se indica `soffice.exe` e accanto esiste `soffice.com`, viene usato quest'ultimo.
In PowerShell usare `where.exe soffice`, non `where` (alias di `Where-Object`).
Se `--version` termina correttamente ma non produce testo, doctor e build
riportano "Versione non disponibile (output vuoto)" senza generare IndexError.
Gli errori di esecuzione e le conversioni PDF fallite restano bloccanti.

Aprire entrambi i PDF nella cartella stampata dal comando build. Sono presenti
anche DOCX modificabili, messaggio Markdown e manifest con hash e versioni tool.
I risultati dimostrativi già generati sono in `examples/rendered-demo/`.
La demo è stata eseguita anche su Windows con Python 3.14.8, Pandoc 3.12 e
LibreOffice tramite `soffice.com`. La ricerca automatica Scoop è coperta da test
simulati; font e impaginazione vanno verificati nella propria installazione.

## Come è organizzato

| Percorso | Contenuto |
|---|---|
| sources/ | Documenti originali non modificati |
| profile/ | Profilo verificato, provenienza e domande aperte |
| rules/ | Regole editoriali e adattamento agli annunci |
| prompts/ | Istruzioni per importazione, candidatura e revisione |
| templates/reference.docx | Stili Word usati da Pandoc |
| applications/ | Una cartella per posizione |
| examples/ | Dati e output dimostrativi separati |
| scripts/cv.py | Comandi locali senza accesso alla rete |
| tests/ | Verifiche dei vincoli di archiviazione e validazione |

Il contratto dei dati è in `profile/SCHEMA.md`. I contenuti estesi sono Markdown;
YAML conserva metadati, fatti e ID. Il validatore controlla il nucleo del contratto,
non tutti gli eventuali campi aggiuntivi e non la verità delle affermazioni.

## Primo caricamento dei CV

1. Copiare le versioni in `sources/`, con nomi distinguibili.
2. Chiedere all'assistente di seguire `prompts/01-import.md`.
3. Esaminare discrepanze e domande prima di consolidare `profile/profile.yaml`.
4. Eseguire `validate`. Un profilo vuoto è strutturalmente valido, ma non può
   produrre una candidatura reale.

Le note negoziali possono stare in `private/`, esclusa da Git: occorre un backup
separato se scegli di usarla. Il resto dei dati reali sarà versionato: usare un
repository GitHub privato e rivedere i file prima di ogni push.

## Preparare una candidatura

```powershell
.\.venv\Scripts\python.exe scripts/cv.py new 2026-10-azienda-ruolo --company 'Nome azienda' --role 'Ruolo'
```

Lo slug è libero, composto da lettere minuscole, numeri e trattini; una cartella
esistente non viene sovrascritta. Per l'inglese aggiungere `--language en`.

1. Incollare testo integrale, URL e data dell'annuncio in `job.md`.
2. Chiedere all'assistente di seguire `prompts/02-tailor.md`, indicando la cartella.
3. Rivedere `analysis.md`, `cv.md`, `cover-letter.md`, `message.md` ed `evidence_ids`.
4. Eseguire i comandi seguenti, sostituendo lo slug:

```powershell
.\.venv\Scripts\python.exe scripts/cv.py validate applications/2026-10-azienda-ruolo
.\.venv\Scripts\python.exe scripts/cv.py build applications/2026-10-azienda-ruolo
```

`build` può generare una bozza non approvata ma blocca segnaposto, evidenze
inesistenti o non confermate. La versione iniziale richiede tutti e tre i testi;
puoi inviare solo quelli appropriati al canale. I file vengono sempre generati
in una cartella nuova. Non modificare direttamente i DOCX finali: riportare le
correzioni nei Markdown e rigenerare, altrimenti snapshot rileva una divergenza.

## Approvare e archiviare

Dopo la revisione dei contenuti e di ogni pagina dei PDF, impostare in
`application.yaml`:

```yaml
content_approved: true
layout_checked: true
```

Archiviare indicando l'esatto nome della cartella build:

```powershell
.\.venv\Scripts\python.exe scripts/cv.py snapshot applications/2026-10-azienda-ruolo --build NOME_CARTELLA_BUILD
```

Il comando richiede le approvazioni, verifica gli hash e conserva output, testi,
profilo, fonti e modello sotto `sent/`. La cartella è una convenzione di archivio:
**il comando non invia nulla**. Per preservare la copia effettivamente inviata,
archiviare il pacchetto scelto e usare quegli stessi file per l'invio manuale.
Aggiornare poi `status: sent`, canale, prossima azione e data nei metadati correnti.
Gli snapshot precedenti non devono essere modificati.

Le due approvazioni possono cambiare dopo il build; altre modifiche a metadati,
testi, profilo, fonti, regole, script o modello richiedono un nuovo build e controllo.
Lo script verifica l'integrità del pacchetto, non la correttezza semantica dei testi.

```powershell
.\.venv\Scripts\python.exe scripts/cv.py register
```

Rigenera `applications/register.csv` dai metadati delle candidature. È un indice,
non va modificato a mano. La demo è esclusa.

## Assistenti

`AGENTS.md` è il punto di ingresso condiviso. `CLAUDE.md`,
`.github/copilot-instructions.md` e `.clinerules/01-project.md` rimandano alle stesse
regole. Se usi una chat web, allega i file necessari e chiedi esplicitamente di
leggere AGENTS.md: una chat non vede automaticamente il workspace locale.

Prompt iniziale suggerito:

> Leggi AGENTS.md e README.md. Verifica il progetto con doctor e validate.
> Non importare ancora fonti. Aiutami a eseguire la demo e a controllarne i PDF.

## Modello e limiti

Il modello è sobrio, a colonna singola, formato Letter, carattere Calibri.
Puoi modificare formato pagina (anche A4), margini e stili in LibreOffice e salvare
come DOCX. Pandoc usa gli stili, non il testo di esempio del modello. Fare sempre
un nuovo build e controllo visivo dopo una modifica. La prima versione non
include estrazione automatica affidabile dai CV, matching semantico automatico,
invii, reminder o interfaccia web: importazione e adattamento sono assistiti.

## Git e GitHub

Lo ZIP non include una cartella `.git`. Per inizializzare il repository:

```powershell
git init -b main
git add .
git commit -m "chore: bootstrap CV workspace with synthetic demo"
```

Creare su GitHub un repository **privato e vuoto**. Poi, con l'URL reale:

```powershell
git remote add origin URL_DEL_REPOSITORY_PRIVATO
git push -u origin main
```

Nessun repository remoto viene creato da questo pacchetto.

## Verifiche

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Le verifiche coprono separazione demo, riferimenti non validi, evidenze non
confermate, blocco delle modifiche dopo il build e mancata sovrascrittura degli
snapshot. Il rendering effettivo si controlla con la demo e i PDF.

