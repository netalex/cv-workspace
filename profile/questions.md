# Domande per il consolidamento

Stato: Q01–Q03 risolte; Q04 parzialmente risolta (origine del 20% chiarita; attività A-Ice da precisare); Q05–Q11 aperte. Nessuna risposta dedotta dalle riscritture dei CV.
Gli estratti seguenti sono evidenze testuali delle fonti, non fatti già confermati.
Le righe sono quelle dei file UTF-8 in sources/extracted, non le pagine degli originali.

## Q01 — Qual è la data effettiva di fine incarico Excellence Innovation?

Le versioni indicano ottobre oppure novembre 2025. Distinguere eventuale termine dello sviluppo, chiusura incarico e sovrapposizione con What If.

- [src-dcdf3c0b0866f539](../sources/extracted/src-dcdf3c0b0866f539.txt), riga 37: «***Marzo 2025 – Ottobre 2025***»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 40: «Marzo 2025 – Novembre 2025»

**Risposta confermata dall’utente il 10 ottobre 2026:** fine incarico a **ottobre 2025**. L’ultimo contatto per la chiusura dei materiali è avvenuto **lunedì 3 novembre 2025**.

Dichiarazione originale: «ottobre, l'ultimo contatto per la chiusura dei materiali è di lunedì 3 novembre 2025».

**Esito:** Q01 risolta. Nel CV usare ottobre 2025 come mese di fine incarico (`2025-10`), senza attribuire un giorno preciso. Conservare separatamente il contatto di chiusura (`2025-11-03`), che non modifica la data di fine incarico. Questa risposta non conferma le date di What If.

## Q02 — Che cosa faceva esattamente What If e qual era il cliente finale?

Una versione parla di clearing dei pagamenti, una di proiezione mutui per BFF Bank. Non assumere che le due descrizioni siano equivalenti; confermare anche la catena dei fornitori.

- [src-dcdf3c0b0866f539](../sources/extracted/src-dcdf3c0b0866f539.txt), riga 27: «Sviluppatore front-end senior e referente tecnico per la feature "What-If", uno strumento di simulazione finanziaria all'interno di un'applicazione bancaria enterprise di clearing dei pagamenti, basata su architettura a micro-frontend (**Angular 19+** con **Module Federation** e shell **React**).»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 35: «Funzionalità di proiezione mutui per BFF Bank, su piattaforma enterprise di Be Shaping the Future ed Engineering.»

**Risposta confermata dall’utente il 10 ottobre 2026:** cliente finale **BFF Bank**; What If gestiva entrambe le componenti citate nelle fonti, precisate dall’utente come **clearing dei pagamenti sui mutui**.

Dichiarazione originale: «cliente finale BFF Bank, what if gestiva entrambe le cose, clearing dei pagamenti sui mutui».

**Esito:** confermati cliente finale e ambito funzionale. Descrizione sintetica utilizzabile: “What If, funzionalità per il clearing dei pagamenti sui mutui per BFF Bank”. Non dedurre ulteriori dettagli sulle simulazioni o sui calcoli. Catena confermata dall’utente il 10 ottobre 2026:

Alessandro Aprile → Apprendo Srl (datore di lavoro diretto) → Be Shaping the Future (indicata dall’utente come “a brand of Engineering”) → Engineering → BFF Bank (cliente finale).

Dichiarazione originale: «la catena era `io -> apprendo srl (azienda per cui ho assunzione diretta) -> be shaping the future (a brand of engineering) -> engineering -> BFF bank`».

**Stato finale:** Q02 risolta. Conservare distinti datore di lavoro, intermediari e cliente finale; la descrizione del rapporto tra Be Shaping the Future ed Engineering è una dichiarazione dell’utente, non una verifica societaria indipendente.

## Q03 — L’80% era un requisito minimo o una copertura effettivamente raggiunta?

Separare requisito di progetto, risultato misurato e perimetro della misura. Confermare anche a cosa si riferiscono le 100.000 righe. Fino alla risposta evitare la metrica come risultato certo.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 9: «Writing FE Unit tests (minimum 80% coverage)»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 12: «Integrazione e qualità: API REST con modelli TypeScript tipizzati, component library condivise, test unitari ed E2E (Vitest, Jest, Playwright), copertura dell’80% su oltre 100.000 righe.»

**Risposta confermata dall’utente il 10 ottobre 2026:** l’80% era un **requisito minimo di What If**, non un risultato misurato confermato. Le 100.000 righe sono una **stima di massima**.

Dichiarazione originale: «requisito minimo di what if. le righe sono una stima di massima».

**Esito:** Q03 risolta ai fini editoriali. Descrivere l’80% esclusivamente come requisito minimo di copertura dei test nel progetto What If. Non affermare che sia stato raggiunto né associare la percentuale alle 100.000 righe come misura verificata. Conservare il numero di righe come stima, con perimetro e metodo di conteggio non precisati; ometterlo dai CV finché non sia utile e sufficientemente contestualizzato. Non attribuire quelle righe al contributo personale dell’utente.

## Q04 — Da dove provengono gli incrementi di velocità del 20%?

Il 20% è attribuito sia a NextIP sia ad A-Ice nelle versioni recenti; la versione ThinkOpen descrive A-Ice come sospeso nella fase iniziale. Chiarire benchmark, attività completate e se si tratta di stime editoriali da eliminare.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 34: «Design and rewrite in SPA technology (angular) of a legacy aircraft management application for airports. Modular structure, starting from the de-icing module. Project suspended in the initial phase due to COVID.»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 86: «Velocità dell’applicazione migliorata di circa il 20% e codice meglio organizzato.»

**Risposta confermata dall’utente il 10 ottobre 2026:** il miglioramento del 20% era una **stima personale aggiunta durante la riscrittura del CV**, non una misura verificata.

Dichiarazione originale: «una mia stima, in aggiunta durante la riscrittura.»

**Esito:** chiarita l’origine della percentuale. Omettere il 20% dai CV personalizzati in assenza di una base di misura documentata; conservare qui la stima e la sua provenienza. Non sostituirla automaticamente con affermazioni qualitative di miglioramento delle prestazioni non ancora confermate. Resta da precisare quali attività fossero state effettivamente completate per A-Ice prima della sospensione nella fase iniziale riportata dalla fonte ThinkOpen.

## Q05 — Confermi il progetto GFT 2022 in React e i progetti omessi?

Recuperare GFT loan management in React, EmmeLibri 2020, Intesi 2018–2020, Spindox 2019 e Vittoria Assicurazioni 2018 nel profilo completo. Confermare periodi e rapporti contrattuali; potranno poi essere selezionati per candidatura.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 20: «2022 - A&M and new features development in a high-profile Loan management system for a banking group - Front-end Developer - ThinkOpen/GFT (Remote)»
- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 36: «2020 - B2B Books distribution ERP Front End - Front-end Developer - ThinkOpen/EmmeLibri (Presence)»
- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 40: «2018/2020 - PSD2 Bank access management interface - Front-end Developer - ThinkOpen/Intesi (Presence)»
- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 46: «2019 - Web interface for medical devices integrated retail sales system - Front-end Developer - ThinkOpen/Spindox (Presence)»
- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 57: «2018 - - Front-end Developer - ThinkOpen/Vittoria Assicurazioni (Presence)»

## Q06 — Qual era lo stack effettivo di Winga e come descrivere l’architettura?

Le fonti riportano JavaScript/jQuery/Velocity/LifeRay, AngularJS, oppure Angular e Micro Frontend. Chiarire se erano moduli o periodi diversi e quale terminologia descrive correttamente il lavoro svolto.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 6: «Back-end Development (indirect knowledge): SQL - Oracle - Node - PHP - Laravel - Professional tomcat-based CMS (LifeRay) and server-side template engine (Apache Velocity, FreeMarker) - M.E.A.N Stack - MongoDB - Express.js - Agile methodology»
- [src-bc9944151bb7aa63](../sources/extracted/src-bc9944151bb7aa63.txt), riga 15: «Angular/AngularJs - React - React-native - Redux/RxJs - TypeScript/JavaScriptwebRtc - Ionic/PhoneGap/Cordova -»
- [src-751eabd3f2bd89e7](../sources/extracted/src-751eabd3f2bd89e7.txt), riga 202: «Sviluppo front end in Angular per un portale di casinò online basato su architettura a Micro Frontend. Ho eseguito una revisione completa e un refactoring profondo del codice esistente, migliorando l'architettura dell'applicazione e riducendo i tempi di inattività. Ho lavorato su componenti ad alte prestazioni e contribuito alla stabilità del sistema in un contesto con elevati requisiti di disponibilità.»

## Q07 — Quali sono gli anni corretti di 3Wlab e dell’attività PL/SQL?

Separare durata del rapporto con l’azienda e durata del singolo progetto. Le versioni riportano 2015–2017/2016–2017 per 3Wlab e 2010–2013/2008–2013 per PL/SQL.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 64: «2015/2017 - Integrated document management system for the public sector - Front-end Developer - 3Wlab (remote)»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 108: «3Wlab – Roma	2016 – 2017»
- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 130: «2010/2013 Junior PL/SQL Developer»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 141: «AreaTC – Milano	2008 – 2013»

## Q08 — Per Luxottica quali tecnologie e responsabilità sono confermate?

La rev2 distingue il pattern Redux implementato direttamente dall’uso della libreria Redux. Conservare questa distinzione; confermare durata, contributo su React Native, 10.000 righe per app e oltre 50 pagine di documentazione.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 32: «React / React-native, Typescript, RxJs, Java, MongoDB.»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 93: «Gestione dello stato con il pattern Redux implementato direttamente, senza librerie dedicate.»

## Q09 — Quali responsabilità ICAR e competenze backend vuoi confermare?

Confermare periodo maggio–agosto 2026, durata e ambito del ruolo ad interim, interventi C# e attività Playwright. Distinguere sviluppo backend autonomo da interventi circoscritti.

- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 20: «Principale sviluppatore front end senior del progetto, con il ruolo di team leader ad interim in assenza della figura dedicata.»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 24: «Definizione dei pattern architetturali, documentazione tecnica e traduzione dei comportamenti legacy nel nuovo stack, con interventi sul backend C# quando necessario.»

## Q10 — Quale data di revisione attribuire al CV denominato Luglio2026?

Il nome contiene Luglio2026 ma il testo reca CV Aggiornato 10/2025 e include attività fino ad agosto 2026. Non attribuire una data autorevole dal filename o da questa intestazione.

- [src-b956b8438beec18a](../sources/extracted/src-b956b8438beec18a.txt), riga 4: «CV Aggiornato 10/2025»
- [src-b956b8438beec18a](../sources/extracted/src-b956b8438beec18a.txt), riga 17: «Maggio 2026 – Agosto 2026»

## Q11 — Confermi formazione e denominazioni dei corsi?

Registrare diploma, anno universitario frequentato senza attribuire una laurea, date e titoli esatti dei corsi. Le versioni recenti non devono cancellare il diploma presente in quella inglese.

- [src-a201c479e6c03b86](../sources/extracted/src-a201c479e6c03b86.txt), riga 183: «Diploma in Classical Studies - Liceo Classico Leopardi (1990 - 1997)»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 157: «Un anno di formazione su progettazione, design del prodotto e pensiero visivo, poi applicata alla progettazione di interfacce e all’usabilità nel front end.»
- [src-7b8606e22b543740](../sources/extracted/src-7b8606e22b543740.txt), riga 159: «Architetture Enterprise in Angular 9 & NgRx 9 – online (2019)»
