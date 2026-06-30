## 2024-03-24 - [Explicit Security Instructions in Prompt-Based Apps]
**Vulnerability:** XSS and Path Traversal risks in LLM-generated outputs (HTML and file paths).
**Learning:** In purely prompt-based applications (like this markdown skill), security boundaries cannot be enforced by traditional code logic. If the LLM generates HTML or file paths dynamically based on user input, it may unknowingly execute XSS payloads or write files outside intended directories if not explicitly instructed to sanitize.
**Prevention:** Security mitigations must be codified as explicit, mandatory instructions in the system prompt / skill definition. Always instruct the LLM to sanitize user inputs (e.g., escape HTML characters) and validate/sanitize file paths/slugs (remove slashes, dots, etc.) before generating artifacts.

## 2024-06-30 - Fix Information Disclosure via Stack Traces
**Vulnerability:** External API calls to Anthropic's SDK within `context-guardian/references/automation-orchestrator.md` were not wrapped in try-except/catch blocks, meaning unhandled exceptions could leak internal execution paths and stack traces to standard error output.
**Learning:** For command line orchestration scripts relying on external APIs, network failures or API errors must be handled gracefully. This is especially true for purely prompt-based applications where security mitigations are codified as instructions or orchestrator behaviors.
**Prevention:** Always wrap external API calls (e.g. Anthropic SDK interactions) with `try...except` (Python) or `try...catch` (Node.js/TypeScript) blocks and use generic error logging to prevent unhandled exceptions from leaking sensitive stack trace details.
