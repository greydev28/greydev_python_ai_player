# Part 12 — LLM Engineering

## What makes an AI feature an engineered system?
A useful LLM product combines a model with instructions, context, application logic, data access, validation, evaluation, privacy controls, and monitoring. A clever prompt alone is not a reliable system.

## Core concepts
- **Token:** a unit used to represent text for a model.
- **Context window:** how much input/output the model can process in one request.
- **Prompt:** instructions and context supplied to a model.
- **Structured output:** constrain output to a schema, then validate it anyway.
- **Embedding:** numeric representation useful for semantic similarity.
- **Retrieval-augmented generation (RAG):** retrieve relevant source passages and give them to a model as context.
- **Tool calling:** model proposes a structured tool call; application code validates permissions and executes it.
- **Evaluation:** use representative cases and measurable criteria to judge quality.

## Prompt design
State the role/task, provide relevant context, define constraints, specify the desired output format, and include examples only when they clarify behaviour. Separate trusted instructions from user-provided content. Treat retrieved documents and user input as data, not instructions to override system policy.

## RAG pipeline
1. Collect documents only when you have permission to use them.
2. Clean and split documents into chunks that preserve meaning.
3. Attach metadata and source identifiers.
4. Embed chunks and store vectors in a searchable index.
5. Retrieve relevant chunks for each query.
6. Construct a prompt with the retrieved evidence.
7. Generate an answer with source references.
8. Evaluate retrieval quality and answer faithfulness.
9. Return an honest "I couldn't find evidence" when appropriate.

RAG does not guarantee truth. Retrieval may miss the right passage and a model may misrepresent evidence. Evaluate both retrieval and generation.

## Safety, privacy, and cost
- Never hard-code API keys or log secrets.
- Minimise personal data; get permission and define retention.
- Validate tool inputs and enforce access control in code, not in the prompt.
- Limit tool permissions, timeouts, retries, and spending.
- Protect against prompt injection in user input and retrieved content.
- Add rate limits, monitoring, and graceful error handling.
- Tell users when output may be wrong; provide sources for factual answers.
- Consider copyright, bias, and misuse risks before launch.

## Evaluation set
Build at least 30–50 representative questions before optimising. Include easy cases, ambiguous questions, no-answer cases, adversarial instructions, outdated/conflicting documents, and questions requiring source citations. Score correctness, evidence support, relevance, refusal behaviour, latency, and cost. Keep a fixed regression set.

## Exercises
1. Write a prompt that extracts a support ticket into a JSON schema; validate fields in Python.
2. Build a small FAQ assistant over 10 documents. Every answer must cite its source.
3. Add an unanswerable question and ensure the system abstains.
4. Test a prompt-injection document that says to ignore the user question.
5. Compare a plain LLM answer with a RAG answer on the same questions.
6. Record latency, token/call cost if available, failure cases, and user feedback.

## Greydev Advanced Challenge — Build and Evaluate an Evidence-Grounded LLM System

1. Build a RAG prototype over documents you are permitted to use. Preserve source IDs and metadata through chunking, retrieval, and answer generation.
2. Create a fixed evaluation set of at least 40 questions: answerable, unanswerable, ambiguous, conflicting-source, stale-source, and prompt-injection cases. Write expected evidence or scoring guidance before tuning.
3. Measure retrieval quality separately from answer quality. Compare at least two chunking or retrieval configurations and record failures, latency, and cost where available.
4. Validate structured model output with a schema and handle invalid, incomplete, or unexpected output without crashing. Do not trust a model-generated tool call until application code validates it and checks permissions.
5. Add abstention when evidence is insufficient, source citations, bounded retries/timeouts, and protections against secrets appearing in logs.
6. Write a threat model covering prompt injection, data leakage, unauthorised tool use, copyright, and harmful or misleading answers. Explain what controls are enforced by code rather than by prompting.

