## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.
## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.

## 2026-06-30 - Enforcing Structural Accessibility in Prompt Generated UI
**Learning:** When instructing LLMs to generate UI components (like HTML cards), semantic meaning and structural accessibility elements (like `<dl>`, `<dt>`, `<dd>` for data rows) along with context-dependent ARIA roles (e.g., `role="status"`, `role="alert"`) must be explicitly mandated in the prompt. LLMs often default to generic wrappers (like `div` or markdown tables) if semantic tags aren't required, which harms screen reader experiences.
**Action:** Always include explicit, mandatory instructions for semantic tags and context-dependent ARIA roles (along with the states that trigger them) in the system prompts/skills definitions that generate UI artifacts.
