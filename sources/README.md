# Archivio delle fonti

## Consultazione

- `inventory.yaml`: tutti i contenuti, hash SHA-256, ID, percorsi e stato di estrazione.
- `INDEX.md`: indice navigabile dei documenti estratti, duplicati e collegamenti da esportare.
- `REVIEW.md`: risultati del primo confronto e limiti dell'analisi.
- `raw/`: copie originali, mai riscritte dallo script.
- `extracted/`: testo UTF-8 di ogni contenuto estraibile, con nome uguale all'ID.
- `../profile/questions.md`: domande con riferimenti alle evidenze.

Un ID `src-...` identifica i byte del documento: più copie identiche condividono
lo stesso ID, tutti i percorsi rimangono nell'inventario. Una modifica ai byte
produce un nuovo ID; non equivale a una nuova esperienza professionale.
Il profilo principale non viene aggiornato dall'inventario.

## Rigenerazione

Dalla radice, con il venv attivo:

```powershell
python scripts/inventory_sources.py
```

Richiede PyYAML (già nelle dipendenze); usa Pandoc per HTML/RTF/EPUB,
LibreOffice per DOC e `pdftotext` di Poppler per PDF. DOCX e ODT sono letti
come XML con la libreria standard. Su Windows `pdftotext` deve essere nel PATH.
Un tool mancante produce un errore registrato per i file coinvolti: non una
falsa estrazione riuscita. I programmi dei vecchi siti non vengono eseguiti.

Il comando rigenera inventory.yaml e i testi; INDEX.md e REVIEW.md sono documenti
di revisione di questo lotto e non vengono aggiornati automaticamente. I testi
precedenti non più referenziati non vengono cancellati: fa fede inventory.yaml.

## Limiti

`extracted` indica disponibilità di testo, non accuratezza biografica, completezza
visiva o approvazione. Il testo può perdere colonne, caselle di testo, immagini,
revisioni, legami fra celle e formattazione. Nessun OCR automatico. Le estrazioni
Office non sono una verifica di tutti gli oggetti incorporati. Per le versioni
che useremo come fonti definitive verificare le sezioni rilevanti sull'originale.

`document_candidate` include anche Markdown/JSON e pagine dei vecchi siti:
non tutti sono CV. I flag automatici su placeholder e nomi `template` richiedono
revisione: un nome con `template` può contenere un CV reale.
Le date non vengono inferite dal nome né dal timestamp del file. Tutti i record
restano senza data normalizzata finché non viene verificata.

I collegamenti `.gdoc`, `.glink` e `.lnk` non sono documenti completi: esportare
quelli utili dal servizio originale e conservare il riferimento di provenienza.
Duplicati binari e testi uguali non sono conferme indipendenti dei fatti.
