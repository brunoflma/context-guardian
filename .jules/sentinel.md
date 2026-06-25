## 2024-03-24 - [Explicit Security Instructions in Prompt-Based Apps]
**Vulnerability:** XSS and Path Traversal risks in LLM-generated outputs (HTML and file paths).
**Learning:** In purely prompt-based applications (like this markdown skill), security boundaries cannot be enforced by traditional code logic. If the LLM generates HTML or file paths dynamically based on user input, it may unknowingly execute XSS payloads or write files outside intended directories if not explicitly instructed to sanitize.
**Prevention:** Security mitigations must be codified as explicit, mandatory instructions in the system prompt / skill definition. Always instruct the LLM to sanitize user inputs (e.g., escape HTML characters) and validate/sanitize file paths/slugs (remove slashes, dots, etc.) before generating artifacts.
## 2026-06-25 - [Arbitrary Code Execution via Prompt Injection in Automated CLI]
**Vulnerability:** Automated CLI tools (like `claude` in Claude Code scripts) using the `--dangerously-skip-permissions` flag are vulnerable to Arbitrary Code Execution (ACE) via prompt injection.
**Learning:** If an LLM orchestration script passes context dynamically (e.g., passing a generated report) to an LLM CLI that has safety prompts disabled, prompt injection in the context could trick the LLM into executing harmful shell commands without any user consent.
**Prevention:** Never use `--dangerously-skip-permissions` or similar flags in automated scripts that process dynamically generated context or user input. Always require explicit user confirmation for potentially dangerous actions.
