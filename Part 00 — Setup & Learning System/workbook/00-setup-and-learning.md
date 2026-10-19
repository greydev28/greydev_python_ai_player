# Part 00 — Setup & Learning System

## What an engineer does
An engineer translates a real need into a working, understandable, testable system. Coding is one part: clarify requirements, model data, design behaviour, implement, test, document, deploy, and maintain.

## Check your tools
Run:
```bash
python --version
python -m pip --version
git --version
```
If `python` is not recognised, try `python3 --version` on macOS/Linux. Use the same interpreter to install packages: `python -m pip install package_name`.

## Virtual environments
A virtual environment isolates a project's dependencies. Create one per project with `python -m venv .venv`, activate it, then install packages. A `requirements.txt` can record dependencies using `python -m pip freeze > requirements.txt`; for production, prefer deliberately maintained dependency pins.

## Git essentials
```bash
git init
git status
git add .
git commit -m "Start project"
git log --oneline
```
A commit is a named checkpoint, not a backup of secrets. Create a `.gitignore` containing `.venv/`, `__pycache__/`, `.env`, `.pytest_cache/`, and generated data that should not be committed.

## Your learning contract
For every task, record:
1. Goal and expected input/output.
2. Your plain-English algorithm.
3. What you tried.
4. The error or failing test.
5. The fix and why it works.
6. One edge case you added.

## Exercises
1. Create a folder `greydev_python_lab`, initialise Git, and make a first commit.
2. Create and activate a virtual environment. Print Python's version from a script.
3. Create `hello.py` with a `main()` function and `if __name__ == "__main__": main()`.
4. Deliberately cause a `NameError`; explain the traceback before fixing it.
5. Write a learning log entry for your first session.
