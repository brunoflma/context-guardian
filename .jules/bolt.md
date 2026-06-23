## 2024-06-18 - [Initial Learnings]\n**Learning:** This is a project called Context Guardian, a tool/skill for Claude.ai to monitor context degradation and generate transfer reports. It includes implementations for automation in Python, Node.js, Claude Code, and n8n.\n**Action:** Focus on finding performance improvements within the Python or Node.js orchestrator scripts, as these are the main executable parts of the codebase. The rest are mostly Markdown documents.

## 2024-06-18 - [Large String Parsing Optimization]

**Learning:** Using `string.includes(marker)` followed by `string.split(marker)[1]` on extremely large strings (like 800,000+ characters / 200k tokens in LLM context windows) creates massive memory pressure by allocating arrays of large string chunks and performing O(2N) passes over the text.
**Action:** Always use `.indexOf()` + `.substring()` (in JS/TS) or `.partition()` (in Python) to perform a single O(N) pass and extract only the needed part without unnecessary array allocations.
