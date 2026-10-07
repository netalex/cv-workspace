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
