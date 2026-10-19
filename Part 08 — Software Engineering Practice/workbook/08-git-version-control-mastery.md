# Git Version Control Mastery for Python Developers

Git is a version-control system that records changes to files. GitHub/GitLab are hosting and collaboration platforms built around Git; they are not Git itself. You should be comfortable with local Git before relying on a graphical client.

## The mental model

- **Working tree:** the files currently in your project directory.
- **Index/staging area:** the exact changes selected for the next commit.
- **Commit:** a snapshot plus metadata and a parent reference.
- **Branch:** a movable name pointing to a commit.
- **Remote:** a named reference to another repository, often hosted online.
- **Merge/rebase:** different ways of integrating histories.

## Core workflow

```bash
git init
git status
git add README.md
git diff --staged
git commit -m "docs: add project overview"
git log --oneline --graph --decorate
```

Stage intentionally. `git add .` can stage generated files or secrets if `.gitignore` is poor. Review `git status` and `git diff --staged` before committing.

## Commands to learn deeply

```bash
git status
git diff
git diff --staged
git log --oneline --graph --decorate
git show <commit>
git switch -c feature/ticket-search
git add <path>
git commit -m "feat: add ticket search"
git stash push -m "unfinished experiment"
git stash list
git restore <path>
git restore --staged <path>
git merge <branch>
git rebase <base-branch>
git revert <commit>
git tag -a v1.0.0 -m "First stable release"
```

Understand destructive commands before using them. `git restore` can discard work; resetting or rewriting history can be dangerous. Practise recovery commands in a disposable repository. Prefer `git revert` for undoing a published commit because it creates a new commit that reverses the change.

## Branches and collaboration

Use a short-lived branch for a focused change. Keep commits understandable, pull/reconcile changes before publishing, push your branch, open a pull request, request review, respond to feedback, and merge only after checks pass. Learn merge conflicts by editing the same lines on two branches and resolving the conflict markers manually.

## `.gitignore` for Python

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/
.env
.env.*
!.env.example
.DS_Store
```

Do not commit virtual environments, generated caches, private data, or real credentials. If a secret is committed, deleting the file in a later commit does not remove it from history: revoke/rotate it immediately and follow your hosting provider's history-removal guidance.

## A professional Python Git workflow

1. Start from a clean `main` branch.
2. Create a focused feature branch.
3. Implement a small change and add tests.
4. Run tests, formatter/linter, and type checker where configured.
5. Inspect `git diff` and staged changes.
6. Commit with a meaningful message.
7. Push and open a pull request.
8. Address review, resolve conflicts, and merge.
9. Tag meaningful releases and maintain a changelog.

## Hard lab — prove you understand history

1. Create a repository with a small Python package, tests, README, `.gitignore`, and virtual environment. Make at least six meaningful commits.
2. Create `feature/search`, add a tested feature, then update `main` independently. Integrate the branch and resolve a deliberate conflict. Explain the final commit graph.
3. Stage an unwanted file by mistake. Unstage it without losing local edits. Then accidentally track a generated file and stop tracking it while retaining the local copy.
4. Introduce a bug across several commits. Use `git log`, `git show`, and `git bisect` to identify the first bad commit; write down the reproduction steps.
5. Publish to a remote repository and document branch protection/review checks you would configure.
6. Create a release tag. Then simulate a bad published change and undo it with `git revert`; explain why resetting a shared branch is not the default fix.
7. Write a one-page Git incident report describing what happened, which recovery commands you used, what data was at risk, and how you prevented recurrence.

## Exit criteria

You can explain the working tree, index, commits, branches, remotes, merge and rebase; recover from common mistakes in a practice repository; resolve conflicts; inspect history; and collaborate through reviewed pull requests without committing secrets.

## Authoritative references

- Pro Git book: https://git-scm.com/book/en/v2
- Git reference: https://git-scm.com/docs
- GitHub pull requests: https://docs.github.com/en/pull-requests
