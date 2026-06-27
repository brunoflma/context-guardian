## 2026-06-18 - LLM Skill UI A11y

**Learning:** When writing instructions for an LLM to generate UI components (like HTML cards), accessibility attributes (ARIA labels, roles, aria-hidden for icons) must be explicitly declared in the prompt/skill file. Otherwise, LLMs typically omit them and the generated interface will be inaccessible by default.
**Action:** Always include explicit `aria-*` and `role` instructions in `.md` files or prompts that instruct an LLM to generate UI.

## 2026-06-23 - Add accessible name to prompt-generated progress bars

**Learning:** Progress bars (`role="progressbar"`) generated via prompt injection in markdown files lack surrounding semantic context to give them an accessible name. Without an explicit `aria-label`, they are announced as just "progress bar" to screen readers, causing an accessibility violation.
**Action:** Always include an explicit `aria-label` (e.g., `aria-label="Progress to next checkpoint"`) when instructing an LLM to generate `role="progressbar"` components in UI cards.

## 2026-06-27 - Add semantic HTML and ARIA roles to generated UI cards

**Learning:** When generating complex UI components like key-value data lists or dynamic notification bars via LLM prompts, basic ARIA labels are insufficient. Structural semantics (like `<dl>`, `<dt>`, `<dd>` tags) are critical for screen reader compatibility, and dynamically changing elements (like recommendation bars) require state-appropriate roles (e.g., `role="status"` vs `role="alert"`).
**Action:** Always specify exact structural HTML tags for data lists and mandate explicit, state-dependent ARIA roles (e.g. `status`, `alert`) for dynamic UI elements when prompting an LLM to build accessible interfaces.
