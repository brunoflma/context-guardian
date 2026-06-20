## 2025-02-28 - [Path Traversal in Prompt-Based Apps]

**Vulnerability:** Path Traversal
**Learning:** In purely prompt-based applications (like Claude skills), security mitigations (such as preventing XSS or Path Traversal) cannot rely on traditional code logic. If a prompt uses an unsanitized value (e.g., `[slug]`) to generate a filename (e.g., `/mnt/user-data/outputs/context-guardian-[slug]-turno-[N].md`), the LLM could be tricked into generating a path outside the intended directory.
**Prevention:** These vulnerabilities must be codified as explicit, mandatory sanitization instructions for the LLM within the skill definition Markdown files, telling the LLM exactly how to sanitize variables before using them in sensitive contexts (like file paths).
