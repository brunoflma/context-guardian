## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.

## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.

## 2026-06-26 - Improve semantic accessibility and context-aware ARIA roles for LLM UI generation

**Learning:** When generating UI components like HTML cards using an LLM, it's not enough to just add generic ARIA labels and roles. Structural accessibility elements (e.g., semantic tags like `<dl>`, `<dt>`, `<dd>`) and context-dependent ARIA roles (e.g., `role="status"` vs `role="alert"`) must be explicitly mandated in the markdown prompts. If these semantics are missing, the output HTML will lack proper structure for screen readers, and dynamic state changes might not be properly announced.
**Action:** Always include explicit instructions for structural semantic HTML (like `<dl>` for key/value pairs) and context-aware ARIA roles (like `role="status"` or `role="alert"`) in the `.md` files or prompts that instruct an LLM to generate UI.
