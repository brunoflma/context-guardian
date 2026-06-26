## 2024-03-24 - [Explicit Security Instructions in Prompt-Based Apps]

**Vulnerability:** XSS and Path Traversal risks in LLM-generated outputs (HTML and file paths).
**Learning:** In purely prompt-based applications (like this markdown skill), security boundaries cannot be enforced by traditional code logic. If the LLM generates HTML or file paths dynamically based on user input, it may unknowingly execute XSS payloads or write files outside intended directories if not explicitly instructed to sanitize.
**Prevention:** Security mitigations must be codified as explicit, mandatory instructions in the system prompt / skill definition. Always instruct the LLM to sanitize user inputs (e.g., escape HTML characters) and validate/sanitize file paths/slugs (remove slashes, dots, etc.) before generating artifacts.

## 2024-05-18 - Fix missing error handling exposing stack traces

**Vulnerability:** Missing error handling in API calls exposing stack traces and internal details on failure.
**Learning:** In automated orchestrator scripts, unhandled exceptions during API calls can leak sensitive information like stack traces, request details, and internal execution paths to the terminal or logs. This violates the principle of failing securely.
**Prevention:** Always wrap external API calls in secure `try...catch` (or `try...except`) blocks. Catch exceptions gracefully, log safe and generic error messages, and ensure the application state remains consistent instead of crashing and exposing internals.
