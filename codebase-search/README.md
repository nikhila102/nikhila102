# Python Codebase Search

Find the Python function or class that handles a task and see the exact file and line range. The CLI reads local source using Python's syntax tree and ranks matches using words in identifiers, docstrings, and code. It reads source without importing it.

## Run the demo

Requires Python 3.10+ and the standard library. Run these commands from this directory.

```bash
python search.py demo "release time slot"
python evaluate.py
```

To search another checkout, replace `demo` with its local path. Output is JSON with the relative path, symbol, start and end lines, and source excerpt. An empty array means the query shared no indexed terms with the code.

## Evaluation

| Metric | Fictional clinic fixture |
| --- | --- |
| Expected symbol ranked first | 5 of 5 |
| Expected symbol in top three | 5 of 5 |
| Out-of-scope query returned no hits | 1 of 1 |

The evaluation uses authored queries on three functions. It measures lexical retrieval on those examples. The current scope is local Python source and keyword ranking. Semantic retrieval and generated answers are planned extensions.

Inspired by [5 BEST AI Projects for 2026](https://devshreebharatia.substack.com/p/5-best-ai-projects-for-2026).
