# Part 13 — Shipping AI Systems

## API basics
An API exposes defined operations to another program. Learn HTTP methods, status codes, request/response JSON, validation, authentication, timeouts, and error contracts. FastAPI is a good Python framework for typed HTTP APIs.

## Reliability checklist
- Validate every request.
- Return useful error codes without leaking stack traces or secrets.
- Set timeouts on network calls.
- Use bounded retries only for transient failures; avoid retry storms.
- Log request IDs and operational facts, not passwords or private prompts.
- Add tests for success, invalid input, missing resources, and downstream failures.
- Keep configuration outside source code.
- Track latency, error rate, model quality, and approximate cost.
- Have a rollback and data recovery plan.

## Deployment path
1. Build locally and run automated tests.
2. Add a lock/pinned dependency strategy.
3. Configure environment variables and secrets.
4. Run the application behind a production server.
5. Add health checks and structured logs.
6. Deploy to a platform you understand.
7. Test the deployed endpoint and document how to reproduce it.
8. Monitor and patch dependencies.

Docker is useful for repeatable environments, but learn Python, HTTP, and environment configuration first.

## Exercises
1. Build a FastAPI endpoint that validates and stores support tickets.
2. Add SQLite persistence and a migration/backup note.
3. Add a health endpoint and request validation tests.
4. Simulate a model provider timeout and return a controlled error.
5. Write a deployment README with setup, tests, environment variables, API examples, limitations, and rollback steps.

## Greydev Advanced Challenge — Production Readiness

1. Build a FastAPI service with request/response schemas, validation, clear error contracts, health checks, and tests for success, invalid input, missing resources, and downstream failure.
2. Persist data in SQLite with explicit transaction boundaries. Add a backup/restore procedure and test it. Explain how concurrent requests could affect writes.
3. Simulate a slow or unavailable external model provider. Use timeouts and bounded retries only for suitable transient errors; prevent retry storms and return a safe response.
4. Configure secrets through environment variables. Add a test or repository check that catches accidental committed credentials; do not include real secrets in examples.
5. Add structured logs and request IDs, but exclude secrets and unnecessary personal data. Define metrics for latency, error rate, availability, and AI cost/quality.
6. Containerise the application if appropriate, document reproducible setup, and perform a deployment smoke test. Write a rollback plan and describe how you would respond to a broken release.

