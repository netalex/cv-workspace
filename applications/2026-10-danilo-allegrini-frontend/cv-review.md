# Revisione del CV per Danilo

## Problema della prima bozza

Il profilo dichiara Angular ma le esperienze principali mostrano soprattutto React,
AI e coordinamento. ICAR perde il lavoro di implementazione UI; What If è ridotto
al dominio funzionale e al requisito di copertura test. Mancano progetti recenti
che dimostrano modernizzazione Angular e continuità del percorso.
Il consolidamento precedente ha confermato solo sottoinsiemi dei progetti e la
selezione automatica dei soli record confirmed ha impoverito il CV.

## Correzioni applicabili con le conferme già raccolte

- Intesi: rendere esplicito Angular nel titolo del progetto e la responsabilità
  frontend nel team di tre, con analisi funzionale e formazione dei colleghi.
- Luxottica: evidenziare implementazione personale di app complete, componenti
  condivisi e BI multilivello; la documentazione non deve oscurare lo sviluppo.
- ICAR: conservare FE lead e automazione AI come competenze distinte; non presentare
  il coordinamento temporaneo come ruolo principale o PM formale.
- Winga: AngularJS con Liferay, chiaramente distinto da Angular moderno.
- A-ICE: recuperare il lavoro del team sulle fondamenta modulari FE/BE, senza
  attribuire sviluppo backend personale o applicazione completata.

## Integrazioni proposte dalle fonti, da confermare prima del CV finale

| Progetto | Capacità sottovalutate e formulazione proposta | Fonte |
|---|---|---|
| ICAR | Sviluppo Angular standalone/zoneless, DevExtreme, form e validazioni, integrazione REST e migrazione gestionale legacy | src-b956b8438beec18a, riga 19 |
| What If | Sviluppo Angular, traduzione requisiti in componenti e integrazione backend; microfrontend Module Federation con shell React | src-b956b8438beec18a, riga 27; src-dcdf3c0b0866f539, sezione What If |
| Excellence | Migrazione Angular 19, monorepo Nx, librerie condivise, strict typing, build/deploy e integrazione Laravel | src-b956b8438beec18a, sezione Excellence; src-dcdf3c0b0866f539, sezione Excellence |
| Simplify | Sviluppo Angular per telemedicina, ambienti/repository, integrazione modelli FE/API | src-b956b8438beec18a, sezione Simplify |
| NextIP | React, migrazione PHP e uso intenso di web worker | src-20510e4bba7a5595, sezione NextIP |
| GFT 2023 / Marina Militare | Componenti Angular personalizzati per editor PrimeNG/Ace.js, mentoring e organizzazione Agile | fonti storiche e CV recenti; distinguere GFT 2022 React da GFT 2023 |
| Lutech | Angular/PrimeNG, documentazione SDS/TP in contesto di laboratorio clinico | src-dcdf3c0b0866f539, sezione Lutech |
| RFI / 3WLab | AngularJS, architettura autonoma della demo e coordinamento con grafici/HTML | src-dcdf3c0b0866f539, sezione RFI |
| DS Group | CMS da zero con JavaScript/Java, offline e cross-platform | src-20510e4bba7a5595, sezione DS Group |

Non promuovere queste affermazioni a confirmed solo perché ripetute nelle fonti.
Per ICAR è sufficiente confermare Angular moderno senza pubblicare una versione
specifica: le versioni numeriche e la cronologia vanno verificate separatamente.
Anche TypeScript, RxJS, REST, Git, CI/CD, Nx e librerie UI meritano una mappatura
esplicita ai progetti, non un elenco generico privo di evidenze.

## Ordine proposto per il CV completo

ICAR; Simplify; What If; Excellence; precedenti esperienze selezionate (Luxottica,
GFT React, Intesi Angular), poi sintesi storica. Ripristinare date attendibili e
raggruppamento per datore di lavoro; le catene complete rimangono nel profilo,
nel CV usare formule brevi “tramite …”. Nessuna sovrapposizione va cancellata.

Le date mancanti rendono il CV precedente poco utile per valutare continuità e
seniority. Contatti e lingue sono ancora incompleti; confermare email/telefono,
inglese e francese prima di inserirli. Evitare la dicitura “25 anni di frontend”:
la storia comprende anche supporto IT e PL/SQL.

## Stato della revisione

cv.md viene migliorato usando i soli fatti confermati. I PDF/DOCX caricati dal
candidato restano preservati come versione precedente e non sono sovrascritti.
La versione ampliata con gli stack recenti richiede la conferma mirata sopra,
poi rigenerazione e revisione del layout. Il test del sistema ha evidenziato una
lacuna di copertura editoriale che la sola validazione strutturale non rileva.
