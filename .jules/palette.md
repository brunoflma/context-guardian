## 2025-02-27 - Markdown Prompt Accessibility Explicit Definitions

**Learning:** When generating HTML UI components via LLM instructions in markdown (like the Context Guardian card), accessibility cannot be implicitly relied upon. Standard a11y attributes (ARIA roles, labels, aria-hidden for decorative SVGs) must be explicitly documented and mandated in the prompt instructions.
**Action:** When creating or modifying markdown instructions that ask the LLM to output UI components, explicitly mandate the required ARIA tags and accessibility structures as part of the output requirements.
