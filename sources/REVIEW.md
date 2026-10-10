# Prima revisione delle fonti

Lotto acquisito dal branch data, commit e8c8523, il 9 ottobre 2026.
Questa è la revisione storica del lotto iniziale. Il 10 ottobre 2026 le risposte
Q01–Q11 sono state consolidate in profile/profile.yaml; per lo stato corrente
consultare profile/evidence.md. Le tabelle seguenti descrivono il lotto iniziale.

## Copertura tecnica

| Misura | Totale |
|---|---:|
| File originali | 472 |
| Contenuti binari distinti | 362 |
| Copie identiche aggiuntive | 110 |
| Contenuti con testo estratto | 198 |
| Contenuti di supporto non estratti | 146 |
| Collegamenti distinti da recuperare | 12 |
| File con testo troppo breve o non testuale | 6 |
| Estrazioni terminate con errore | 0 |
| Gruppi con testo estratto esattamente uguale ma byte diversi | 5 |

I 198 testi includono CV, template e sorgenti testuali dei vecchi siti; non sono
198 CV indipendenti. Nessun OCR eseguito e nessuna attestazione di completezza
visiva dei documenti. Tutti i file raw conservano i byte originali.

## Fonti prioritarie

| Fonte | Utilità | Cautela |
|---|---|---|
| [src-a201c479e6c03b86](extracted/src-a201c479e6c03b86.txt) | ThinkOpen inglese dettagliato: progetti e stack fino al 2023 | Date ampie; competenze backend indicate come indirette |
| [src-7b8606e22b543740](extracted/src-7b8606e22b543740.txt) | Leonardo rev2: esperienze recenti e focus React | Testo adattato a una posizione; metriche e responsabilità da verificare |
| [src-b956b8438beec18a](extracted/src-b956b8438beec18a.txt) | Apprendo Luglio2026: ICAR, Simplify e cronologia estesa | Intestazione di aggiornamento incoerente |
| [src-dcdf3c0b0866f539](extracted/src-dcdf3c0b0866f539.txt) | Versione Markdown estesa utile al confronto | Alcune date e descrizioni differiscono |
| [src-bc9944151bb7aa63](extracted/src-bc9944151bb7aa63.txt) | CV grafico sintetico con cronologia e stack | Estrazione compatta; non sostituisce le versioni dettagliate |

## Risultati del confronto

Le versioni recenti comprimono o omettono EmmeLibri, Intesi, Spindox e Vittoria
Assicurazioni. Il CV ThinkOpen associa inoltre React al progetto GFT loan
management del 2022, dettaglio utile perso nelle riscritture generiche.

Sono da risolvere la fine di Excellence Innovation, la descrizione di What If,
lo stack Winga, le date 3Wlab/PLSQL e la natura di Redux a Luxottica. Metriche
come +20% o 80% non vanno promosse a risultati confermati senza il loro contesto.
[Le 11 domande con riscontri](../profile/questions.md) separano questi punti.

## Template e contenuti incompleti

Il flag placeholder_content segnala contenuti dimostrativi effettivamente
rilevati. Non basta il nome: AAprile_CV_Apprendo.docx e CV_Apprendo_FINAL.docx
contengono placeholder, mentre file chiamati template possono contenere CV reali.
Il DOC ministeriale [src-5f81afe7ad1d863f](extracted/src-5f81afe7ad1d863f.txt) contiene sezioni esperienza e
formazione vuote nell'estrazione: non va scelto come fonte completa senza
verificare l'originale e confrontarlo con il DOCX ministeriale.

I collegamenti cloud sono elencati nell'[indice](INDEX.md). Conservare i link,
ma esportare i documenti utili prima di considerarli fonti. Gli asset e i vecchi
progetti web non sono stati eseguiti né rimossi.

## Limiti e prossimo passaggio

L'inventario e l'estrazione coprono tutto il lotto secondo i formati supportati.
Il confronto semantico è una prima revisione mirata delle fonti prioritarie,
non una lettura umana riga per riga di tutti i 198 testi. Prima di consolidare
ogni esperienza si controlleranno i relativi originali e le risposte del candidato.
Nessun aggiornamento automatico di profile.yaml, nessuna cancellazione di duplicati.

## Aggiornamento del 10 ottobre 2026

Importato solo il testo della nuova versione Leonardo `src-20510e4bba7a5595` e conservate le conferme dirette.
Il profilo distingue i record confirmed dai dettagli di sola fonte to_verify.
Le nuove aggiunte del CV (web worker NextIP, CMS DS Group, Talent Garden) sono
tracciate; Talent Garden è stato confermato direttamente, le altre rimangono da verificare.
