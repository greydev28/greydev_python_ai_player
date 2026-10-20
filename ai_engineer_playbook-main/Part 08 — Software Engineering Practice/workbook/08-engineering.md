# Part 08 — Software Engineering Practice

## Design before implementation
Write requirements as observable behaviours. Example: "When quantity is zero, borrowing is rejected and available stock remains unchanged." This is more testable than "make borrowing robust."

## Debugging method
1. Reproduce the bug consistently.
2. Read the complete traceback from the bottom upward; identify the failing line and exception.
3. Inspect the values and types at that line.
4. Reduce the program to the smallest failing example.
5. State a hypothesis, change one thing, and rerun.
6. Add a regression test so the bug does not return.

## Testing
A test has setup, action, and assertion. Test normal cases, boundary cases, invalid input, and state changes. Test public behaviour rather than implementation details where possible.

```python
def calculate_priority(urgency: str, affected_users: int) -> str:
    if urgency not in {"low", "medium", "high", "critical"}:
        raise ValueError("unsupported urgency")
    if affected_users < 1:
        raise ValueError("affected_users must be positive")
    if urgency == "critical" or (urgency == "high" and affected_users >= 20):
        return "high"
    return "normal"
```

A matching pytest test:
```python
import pytest
from priority import calculate_priority

def test_critical_is_high_priority():
    assert calculate_priority("critical", 1) == "high"

def test_zero_affected_users_is_rejected():
    with pytest.raises(ValueError):
        calculate_priority("low", 0)
```

## Architecture
Keep responsibilities separate:
- `models.py`: domain objects and validation
- `services.py`: business rules
- `storage.py`: persistence
- `cli.py`: user interaction
- `main.py`: application entry point
Avoid putting every feature in one giant function or class. Use composition when one object needs another object to do its job.

## JSON persistence gotchas
Use `"w"` to replace a JSON document, not `"a"` to append a second JSON document. JSON files must contain one valid JSON value. Handle a missing file separately from malformed JSON. Save a list/dictionary, then restore object state. If IDs must remain unique after restart, persist the next ID or derive it from loaded records.

## Exercises
1. Add unit tests for your CampusFlow ticket creation, assignment, closing, saving, and loading.
2. Ensure invalid borrowing never changes inventory.
3. Refactor a CLI script into model, service, storage, and CLI modules.
4. Add type hints and docstrings to public functions.
5. Create a bug report template with reproduction steps, expected result, actual result, and environment.
6. Write tests for empty JSON files, missing files, invalid JSON, and valid saved data.

## Greydev Advanced Challenge — Engineering Workflow and Git Mastery

Complete this using Git from the terminal; record the commands and explain the outcome of each.

1. Create a repository with a useful `.gitignore`. Accidentally stage a generated file, remove it from the index without deleting your local copy, and explain the difference between untracking and deleting.
2. Make a feature branch, implement a change in several commits, rebase it onto an updated local branch, resolve a deliberate conflict, and verify the final history. Practise on a disposable repository first.
3. Use `git diff`, `git diff --staged`, `git log --oneline --graph`, `git show`, `git restore`, `git switch`, and `git stash` to diagnose and recover from a simulated mistake. Explain which changes are preserved or discarded.
4. Add a remote, push a feature branch, open a pull request on a hosting platform, and describe a useful code-review checklist. Never force-push a shared branch without coordination.
5. Use tags for a release, write a changelog, and demonstrate how you would revert a faulty committed change without erasing shared history.
6. Add automated tests to the project and define a pre-merge checklist: formatting, tests, type checking, secrets scan, and documentation. Explain what should block a merge.
7. Refactor a monolithic CLI into layers while preserving behaviour. Use tests before refactoring and compare the old and new behaviour with representative cases.

