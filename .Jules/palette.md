## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.

## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.
## 2024-05-15 - Explicit Accessibility Directives in LLM Prompts

**Learning:** When instructing an LLM to generate UI components (like HTML cards), relying on general "make it accessible" instructions is insufficient. Structural accessibility elements (like `<dl>`, `<dt>`, `<dd>` for key-value data) and context-dependent ARIA roles (`role="status"`, `role="alert"`) must be explicitly mandated in the prompt to guarantee their inclusion in the final output.
**Action:** Always include explicit, detailed instructions for semantic HTML structures and appropriate ARIA roles in markdown prompts that dictate UI generation.
