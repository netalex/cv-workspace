# Contratto dei dati versione 1

`profile.yaml` è YAML UTF-8. I campi minimi sono verificati da `validate`.
Campi aggiuntivi sono ammessi e vanno documentati se diventano stabili.

- schema_version: 1
- identity: name, email, location (stringhe, inizialmente vuote)
- sources: elenco di {id, path, note}; path relativo alla radice del progetto.
- experiences, projects, skills, education, languages: elenchi di record.
- Ogni record: id univoco, label, status (`confirmed`, `to_verify`), source_ids.
- Record confirmed: almeno una fonte esistente.
- Esperienze: aggiungere employer, role, start, end, responsibilities, outcomes.
- Progetti: aggiungere experience_id, context, contribution, technologies, outcomes.
- Competenze: aggiungere usage (`professional`, `study`, `experiment`), last_used, context_ids.
- Formazione: aggiungere institution, qualification, start, end.
- Lingue: aggiungere level e basis (autovalutazione o certificazione).
- Date in stringhe tra virgolette: "2024", "2024-06", "present"; non inventare precisione.

Il validatore controlla il nucleo comune, gli ID e le fonti, non i campi facoltativi
né la verità dei fatti. L'importazione è assistita e richiede revisione.
Le note negoziali possono essere conservate in private/ (esclusa da Git).

`application.yaml`: schema_version, company, role, language (`it`/`en`), demo,
status (`draft`, `ready`, `sent`, `interview`, `closed`), evidence_ids,
content_approved, layout_checked. job_url, captured_on, channel, next_action,
next_action_on sono campi informativi facoltativi. Lo stato non invia nulla.

## Campi del consolidamento

- `source_locator`: sezione Q della fonte di conferma.
- `relationship`, `delivery_chain`, `client`: rapporto e catena, senza inferire forma contrattuale.
- `contract_date`, `closure_contact`, `coordination_until`: date distinte dalle date dell’esperienza; le approssimazioni restano testuali.
- `contribution` e `team_contribution`: contributi personali e del team separati.
- `requirements`: vincoli del progetto, non risultati.
- `metrics`: oggetti con metric, value, kind (estimate/personal_estimate), scope/unit/usage facoltativi. La precisione e le qualificazioni vanno preservate.
- `objectives`: finalità, non risultati misurati.
- `completion`, `duration`, `specialization`, `completion_detail`: formazione e stato del percorso.
- `reported_claim`: contenuto della fonte in un record to_verify, non un fatto confermato.
- `notes`, `practices`, `consolidated_on`: contesto editoriale e data del consolidamento.

I campi facoltativi restano soggetti a revisione editoriale. Un record confirmed
contiene solo il sottoinsieme confermato: i dettagli non confermati sono record
to_verify separati, non campi utilizzabili del record confirmed.
