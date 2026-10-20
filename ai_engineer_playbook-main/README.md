# Greydev AI Engineer Playbook
**Learn by building. Understand before copying. Ship reliable software.**

This repository combines the existing Python foundations course (Parts 02–07) with a structured route to Python proficiency first, then data, machine learning, and practical AI engineering. It is a curriculum and workbook, not a promise that a fixed number of days makes anyone an expert. Mastery comes from repeated practice, feedback, testing, reading documentation, and shipping projects.

## How to use this repository
1. Read one workbook lesson at a time.
2. Create your own solution in a `practice/` folder or the exercise's starter file. Parts 05–14 intentionally have empty `solutions/` folders: these are challenge-only sections, so you must solve them yourself.
3. Write down your approach in plain English, then code.
4. Run examples, test edge cases, and explain the code aloud.
5. Compare with the solution only after a serious attempt. There may be multiple valid solutions.
6. Commit work to Git regularly. Keep a learning log. Git is taught in Part 05 and reinforced with advanced workflows in Part 08.
7. At each checkpoint, rebuild a small version without looking at notes.

### Daily learning loop (2–4 focused hours; scale to your life)
- 20 min: retrieve yesterday's ideas from memory.
- 45 min: study the lesson and official documentation.
- 60–90 min: solve exercises independently.
- 20 min: test, debug, and refactor.
- 10 min: write what you learned, what failed, and the next question.

For longer days, add project work rather than watching more tutorials. Avoid spending all day passively consuming content.

## Curriculum map
| Stage | Folder | Outcome |
|---|---|---|
| 0 | `Part 00 — Setup & Learning System` | Python environment, Git, learning workflow |
| 1 | `Part 01 — Python Foundations` | Variables, expressions, branching, loops, strings |
| 2 | Existing `Part 02 — Collections` | Lists, tuples, dictionaries, sets |
| 3 | Existing `Part 03 — Functions` | Functions, scope, parameters, decomposition |
| 4 | Existing `Part 04 — Object-Oriented Programming` | Classes, objects, composition, inheritance |
| 5 | Existing `Part 05 — Files & Python Ecosystem` | Files, JSON, modules, packages, environments |
| 6 | Existing `Part 06 — Pythonic Features` | Iteration, generators, decorators, context managers |
| 7 | Existing `Part 07 — Professional Python` | Exceptions, typing, docs, tests |
| 8 | `Part 08 — Software Engineering Practice` | Git, debugging, testing, clean architecture |
| 9 | `Part 09 — Data & Mathematics for AI` | NumPy, pandas, visualisation, probability, linear algebra |
| 10 | `Part 10 — Machine Learning` | Baselines, leakage prevention, evaluation, scikit-learn |
| 11 | `Part 11 — Deep Learning` | Tensors, gradients, training loops, PyTorch |
| 12 | `Part 12 — LLM Engineering` | APIs, prompting, structured outputs, embeddings, RAG, evaluation |
| 13 | `Part 13 — Shipping AI Systems` | FastAPI, persistence, Docker basics, deployment, monitoring |
| 14 | `Part 14 — Portfolio Capstones` | Three portfolio-ready projects |

## Recommended sequence and checkpoints
- **Weeks 1–3:** Parts 00–03. Build small CLI programs. You should be able to trace a loop, write functions, and explain data structures.
- **Weeks 4–6:** Parts 04–08. Build and test a file-backed CLI app. Use Git, clear modules, exceptions, and automated tests.
- **Weeks 7–8:** Part 09. Analyse a real dataset and explain charts and summary statistics.
- **Weeks 9–10:** Part 10. Train a baseline ML model, compare metrics, and document limitations.
- **Weeks 11–12:** Part 11. Train and evaluate a small neural network. GPU is optional at first.
- **Weeks 13–15:** Part 12. Build an LLM application with evidence-grounded answers and an evaluation set.
- **Weeks 16–18+:** Parts 13–14. Deploy, document, test, and improve capstones.

This is a flexible guide, not a deadline. If you cannot explain a checkpoint, repeat it before moving on.

## Suggested setup
Use a supported Python 3 version, a code editor, terminal, and Git. In a project directory:
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python --version
```
Install libraries per project inside the activated environment. Never commit `.venv/`, secrets, API keys, or private data. Use `.env` locally and a safe secret manager in production.

## Ground rules for becoming an engineer
- Understand the problem before choosing a library.
- Start with a simple baseline; measure before adding complexity.
- Separate training data from validation/test data. Prevent data leakage.
- Treat LLM output as untrusted input. Validate it.
- Do not put secrets in source code or logs.
- Use small, meaningful functions and tests.
- Read errors fully; reproduce bugs with the smallest example.
- Document data sources, assumptions, failure modes, costs, and privacy risks.
- AI tools may explain or review your code, but you must verify every claim and be able to defend your design.

## Reference shelf
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python library reference: https://docs.python.org/3/library/
- Python Crash Course, 3rd edition by Eric Matthes: https://nostarch.com/Python-crash-course-3rd-edition
- Author's official companion resources: https://ehmatthes.github.io/pcc_3e/
- NumPy quickstart: https://numpy.org/doc/stable/user/quickstart.html
- pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- scikit-learn getting started: https://scikit-learn.org/stable/getting_started.html
- PyTorch beginner tutorials: https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- Git book: https://git-scm.com/book/en/v2

The course uses the *learning approach* of project-based introductory books such as Python Crash Course—small exercises followed by projects. It does not reproduce the book's copyrighted chapters or exercises; use the book and its official companion material alongside this original workbook.


## Challenge-only policy (Parts 05–14)

The `solutions/` directories in Parts 05–14 are intentionally empty. Workbooks contain harder, multi-step challenges instead of ready-made answers. Build your own solution in a separate `practice/` directory, test it, document your decisions, and ask for review only after making a genuine attempt. This is designed to develop independent Python problem-solving ability.

## Python proficiency gate before AI

Before treating the AI stages as your main focus, prove you can independently build a modular Python application with file/JSON or SQLite persistence, validation, exceptions, tests, Git history, documentation, and a clean setup process. If that gate is not met, repeat Parts 02–08 and improve CampusFlow.
