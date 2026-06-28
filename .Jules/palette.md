## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.

## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.

## 2026-06-28 - Mandate structural accessibility elements in LLM prompts

**Learning:** When instructing the LLM to generate UI components, structural accessibility elements like `<dl>`, `<dt>`, `<dd>` and ARIA roles `role="status"`, `role="alert"` must be explicitly mandated in the markdown prompts to ensure the output is accessible.
**Action:** Update the prompt template in SKILL.md to explicitly instruct the LLM to use these accessible elements.
