## 2024-05-24 - O(N²) String Context Tracing

**Learning:** Calculating context sizes heuristically by iterating over conversation arrays (O(N) operation on each turn) results in an O(N²) overall time complexity across session lifetime while accumulating estimation drift. Anthropic APIs directly return accurate usage tokens per exchange.
**Action:** Instead of iterating arrays on every turn (`estimateTokens()`), maintain a `currentContextTokens` state directly populated by exactly returning the `usage` from the API, turning a heavy array scan into a precision O(1) state lookup.
