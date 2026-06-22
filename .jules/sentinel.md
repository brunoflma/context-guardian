## 2025-05-18 - [Path Traversal and XSS via LLM Instructed Actions]

**Vulnerability:** The application is purely driven by prompt instructions (`context-guardian/SKILL.md`), meaning traditional code-based security analysis doesn't fully apply. The LLM creates files (`create_file`) with user-derived slugs and renders user-input into HTML cards without explicit sanitization constraints, leading to Path Traversal and XSS risks via the agent's output.
**Learning:** Security mitigations for this purely prompt-based application cannot rely on traditional code logic. Instead, they must be codified as explicit, mandatory sanitization instructions for the LLM within the skill definition Markdown files.
**Prevention:** Always include rigorous sanitization directives inside prompt blocks that command the LLM to process unverified user input for file operations or HTML generation.
