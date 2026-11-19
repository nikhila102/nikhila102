"""Search Python source by identifier and description, with line citations."""
import argparse
import ast
import json
import math
from collections import Counter
from pathlib import Path
import re
import tokenize

WORD = re.compile(r"[A-Z]+(?=[A-Z][a-z]|\b)|[A-Z]?[a-z]+|\d+")
SKIP = {".git", ".venv", "venv", "__pycache__", "node_modules"}


def terms(value):
    return Counter(word.lower() for word in WORD.findall(value.replace("_", " ")))


def index(root):
    for path in sorted(root.rglob("*.py")):
        relative = path.relative_to(root)
        if SKIP.intersection(relative.parts) or path.is_symlink():
            continue
        try:
            with tokenize.open(path) as stream:
                source = stream.read()
            tree = ast.parse(source)
        except (OSError, SyntaxError, UnicodeError):
            continue
        lines = source.splitlines()
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                yield {
                    "path": relative.as_posix(), "symbol": node.name,
                    "start": node.lineno, "end": node.end_lineno,
                    "source": "\n".join(lines[node.lineno - 1:node.end_lineno]),
                }


def search(records, query, limit=5):
    query_terms = terms(query)
    scored = []
    for record in records:
        name = terms(record["symbol"])
        body = terms(record["source"])
        matched = query_terms.keys() & body.keys()
        if matched:
            score = sum(3 * (term in name) + math.log1p(body[term]) for term in sorted(matched))
            scored.append((score, record))
    scored.sort(key=lambda item: (-item[0], item[1]["path"], item[1]["start"]))
    return [record for _, record in scored[:limit]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("query")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("root must be a local directory")
    print(json.dumps(search(index(args.root), args.query), indent=2))


if __name__ == "__main__":
    main()
