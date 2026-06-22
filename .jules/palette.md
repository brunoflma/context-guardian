## 2026-10-27 - Prompt-Generated UI Accessibility

**Learning:** In purely prompt-based applications without traditional frontend codebases, accessibility rules (like ARIA labels, roles, and `aria-hidden` attributes) cannot be enforced through typical UI component libraries or linters. They must be explicitly codified as mandatory instructions within the markdown prompt files that guide the LLM's UI generation.
**Action:** When designing or updating AI skills that output HTML or UI elements, always include explicit, syntax-level accessibility requirements directly in the prompt templates (e.g., specifying `role="progressbar"` and `aria-hidden="true"` in the instruction blocks).
