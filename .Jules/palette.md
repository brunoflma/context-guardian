## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.

## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.

## 2024-05-18 - Semantic HTML & State-Dependent Roles in Prompt-Generated UIs

**Learning:** When an LLM generates UI components directly from prompts without standard templates, accessibility elements (like `<dl>` for key-value pairs or dynamic `role="status"` vs `role="alert"`) are often overlooked unless explicitly and strictly mandated in the prompt instructions.
**Action:** Always document specific structural accessibility requirements (e.g., semantic tags) and state-dependent ARIA roles within the instructions meant for prompt-based UI generation.
