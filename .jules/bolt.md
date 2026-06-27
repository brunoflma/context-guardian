## 2024-06-18 - [Initial Learnings]
**Learning:** This is a project called Context Guardian, a tool/skill for Claude.ai to monitor context degradation and generate transfer reports. It includes implementations for automation in Python, Node.js, Claude Code, and n8n.
**Action:** Focus on finding performance improvements within the Python or Node.js orchestrator scripts, as these are the main executable parts of the codebase. The rest are mostly Markdown documents.

## 2024-06-18 - [Large String Parsing Optimization]

**Learning:** Using `string.includes(marker)` followed by `string.split(marker)[1]` on extremely large strings (like 800,000+ characters / 200k tokens in LLM context windows) creates massive memory pressure by allocating arrays of large string chunks and performing O(2N) passes over the text.
**Action:** Always use `.indexOf()` + `.substring()` (in JS/TS) or `.partition()` (in Python) to perform a single O(N) pass and extract only the needed part without unnecessary array allocations.

## 2024-03-08 - [Token Limit Monitoring Optimization]

**Learning:** In LLM orchestrator scripts, heuristically estimating token counts by iterating through the entire message history string `O(N)` is an unnecessary performance bottleneck when the API already returns the exact token usage in `usage.input_tokens` and `usage.output_tokens`.
**Action:** Track exact token usage directly in the state variables and update them immediately after each API call, enabling `O(1)` limit checks instead of recalculating the entire history length on every turn.

## 2024-05-24 - Optimize massive string parsing in embedded orchestrator
**Learning:** In Python, when extracting a suffix after a marker from a very large string (like a 200k+ token LLM response), `str.partition()` allocates memory for three strings: prefix, separator, and suffix. If the prefix is massive and unused, this causes significant unnecessary memory pressure.
**Action:** Prefer using `str.find()` combined with string slicing (e.g., `text[idx + len(marker):]`) instead of `str.partition()` when only the suffix is needed from a large string.
