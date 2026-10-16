# Part 14 — Portfolio Capstones

A portfolio should show the problem, design decisions, tests, trade-offs, and limitations—not just screenshots.

## Capstone A: CampusFlow Support Intelligence
Build on the ticket system you have studied:
- CLI or API for ticket creation, assignment, status changes, search, and persistence.
- Automated IDs that remain unique across restarts.
- Input validation and clear errors.
- Unit tests for business rules and JSON/SQLite storage.
- Optional AI feature: classify ticket category or summarise ticket descriptions.
- Human confirmation before consequential changes.
- README, sample data, architecture diagram, and demo.

## Capstone B: Evidence-based Knowledge Assistant
- Use a small set of public documents you are allowed to use.
- Retrieval with source metadata and answer citations.
- Abstain when evidence is missing.
- A 30+ question evaluation set, including prompt injection and no-answer cases.
- Report retrieval and answer-quality failures honestly.

## Capstone C: Small ML service
- Choose a non-sensitive public dataset.
- Define a baseline and evaluation metric before modelling.
- Build preprocessing and model pipeline.
- Prevent leakage and test on held-out data.
- Serve predictions through an API.
- Include model card, monitoring plan, and retraining triggers.

## Definition of done
- [ ] A stranger can install and run it from the README.
- [ ] Tests pass from a clean environment.
- [ ] No API keys, personal data, or machine-specific paths are committed.
- [ ] Inputs are validated and failures are handled.
- [ ] Data source, licence, assumptions, metrics, and limitations are documented.
- [ ] At least one design choice and one failed approach are explained.
- [ ] A short demo is available.
- [ ] You can explain every important function without reading line by line.

## Greydev Advanced Challenge — Portfolio Review Board

For each capstone, submit a repository that a technical reviewer can clone and run. No solution code is provided in this part.

1. **CampusFlow:** implement modular business logic, durable storage, unique IDs across restarts, validation, tests, useful logs, and a clear CLI or API. If adding AI classification, compare it with a rule-based baseline and keep a human override.
2. **Knowledge assistant:** implement retrieval with citations and abstention, a fixed evaluation set of at least 40 questions, prompt-injection tests, and a report of retrieval and answer failures.
3. **ML service:** document data provenance/licence, baseline, split strategy, leakage prevention, chosen metric, error analysis, model card, API tests, and deployment instructions.
4. For each project, provide architecture diagram, setup guide, usage examples, test instructions, known limitations, security/privacy considerations, and a short demo.
5. Conduct a self-review as if rejecting the project from production: identify five risks, prioritise them, fix at least two, and document the remaining trade-offs.
6. Defend one major design decision and one failed approach without reading your notes. A project is not complete until you can explain the important code and reproduce its behaviour.

