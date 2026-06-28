## 2024-03-24 - [Explicit Security Instructions in Prompt-Based Apps]

**Vulnerability:** XSS and Path Traversal risks in LLM-generated outputs (HTML and file paths).
**Learning:** In purely prompt-based applications (like this markdown skill), security boundaries cannot be enforced by traditional code logic. If the LLM generates HTML or file paths dynamically based on user input, it may unknowingly execute XSS payloads or write files outside intended directories if not explicitly instructed to sanitize.
**Prevention:** Security mitigations must be codified as explicit, mandatory instructions in the system prompt / skill definition. Always instruct the LLM to sanitize user inputs (e.g., escape HTML characters) and validate/sanitize file paths/slugs (remove slashes, dots, etc.) before generating artifacts.

## 2024-06-28 - Masking external API exceptions in Python and TypeScript

**Vulnerability:** External API calls (Anthropic SDK interactions) in orchestrator scripts (`context-guardian/references/automation-orchestrator.md`) lacked error handling, exposing unhandled exceptions, internal execution paths, and stack traces on network failure or API error.
**Learning:** Security mitigations for this application cannot rely on traditional code logic. Instead, when scripts use third-party APIs or external commands, exceptions must be explicitly wrapped in `try...except` (Python) or `try...catch` (TypeScript) to prevent unhandled exceptions leaking sensitive system data or internal paths to output logs.
**Prevention:** Ensure that any external interaction or API call within orchestrator code is wrapped with generic exception handlers that log a sanitized error message and conceal stack trace details.
