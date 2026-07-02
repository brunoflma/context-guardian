## 2024-03-24 - [Explicit Security Instructions in Prompt-Based Apps]
**Vulnerability:** XSS and Path Traversal risks in LLM-generated outputs (HTML and file paths).
**Learning:** In purely prompt-based applications (like this markdown skill), security boundaries cannot be enforced by traditional code logic. If the LLM generates HTML or file paths dynamically based on user input, it may unknowingly execute XSS payloads or write files outside intended directories if not explicitly instructed to sanitize.
**Prevention:** Security mitigations must be codified as explicit, mandatory instructions in the system prompt / skill definition. Always instruct the LLM to sanitize user inputs (e.g., escape HTML characters) and validate/sanitize file paths/slugs (remove slashes, dots, etc.) before generating artifacts.

## 2024-07-01 - Prevent unhandled exception leaks in automation orchestrator API calls
**Vulnerability:** External API calls to Anthropic in the Python and TypeScript reference automation orchestrators lacked error handling. An API failure could result in unhandled exceptions that leak stack traces or underlying request payloads, which is contrary to the fail-secure principle.
**Learning:** For prompt-based tools with embedded orchestration scripts in Markdown, standard operational code (like network requests) must be proactively fortified.
**Prevention:** Always wrap external HTTP or API calls in `try/except` or `try/catch` blocks. Return generic error messages to the user without exposing raw error object details.

## 2024-05-18 - Prevent Command Injection in LLM CLI Scripts
**Vulnerability:** Command injection risk via prompt injection when using permission-bypassing flags (`--dangerously-skip-permissions`) in automated scripts utilizing LLM CLIs (like Claude Code).
**Learning:** Embedded automation orchestrators might execute arbitrary system commands if the LLM output (which could be influenced by a malicious prompt) is directly passed to a CLI running with skipped permissions. This allows prompt injection to escalate into arbitrary remote code execution on the host system.
**Prevention:** Never use flags that bypass permission prompts (e.g., `--dangerously-skip-permissions`) in automated scripts utilizing LLM CLIs. Always require user confirmation for potentially dangerous actions, especially when the LLM's input or execution flow can be manipulated.
