## 2024-06-18 - [Initial Learnings]

**Learning:** This is a project called Context Guardian, a tool/skill for Claude.ai to monitor context degradation and generate transfer reports. It includes implementations for automation in Python, Node.js, Claude Code, and n8n.
**Action:** Focus on finding performance improvements within the Python or Node.js orchestrator scripts, as these are the main executable parts of the codebase. The rest are mostly Markdown documents.

## 2024-06-18 - [Large String Parsing Optimization]

**Learning:** Using `string.includes(marker)` followed by `string.split(marker)[1]` on extremely large strings (like 800,000+ characters / 200k tokens in LLM context windows) creates massive memory pressure by allocating arrays of large string chunks and performing O(2N) passes over the text.
**Action:** Always use `.indexOf()` + `.substring()` (in JS/TS) or `.partition()` (in Python) to perform a single O(N) pass and extract only the needed part without unnecessary array allocations.

## 2024-03-08 - [Token Limit Monitoring Optimization]

**Learning:** In LLM orchestrator scripts, heuristically estimating token counts by iterating through the entire message history string `O(N)` is an unnecessary performance bottleneck when the API already returns the exact token usage in `usage.input_tokens` and `usage.output_tokens`.
**Action:** Track exact token usage directly in the state variables and update them immediately after each API call, enabling `O(1)` limit checks instead of recalculating the entire history length on every turn.

## 2024-05-20 - Avoid memory allocation with str.partition on massive strings

**Learning:** Using `str.partition()` on extremely large strings (like 200k+ token LLM contexts) forces the allocation of the prefix string, which can cause significant memory pressure even if the prefix is unused (e.g. assigned to `_`).
**Action:** Use `str.find()` combined with string slicing when only the suffix is needed after a marker. This avoids allocating a massive unused prefix string in memory.
