# Nikhila Vankayalapati

**Applied AI · Retrieval and evaluation · Machine learning**

I build Python projects that show how an AI workflow retrieves evidence, handles uncertainty, and measures its results.

## Featured project · Healthcare claims workflow

[Health-care_claims](https://github.com/nikhila102/Health-care_claims) is an educational project using fictional policies and synthetic data.

- **Retrieval and citations** — Rank fictional policy passages and return exact source quotes in structured JSON.
- **Human review** — Route unverified or external policy questions to a reviewer before retrieval. In-scope questions with weak matches also go to review.
- **Reproducible evaluation** — Inspect retrieval ranking and abstention on authored questions. A separate synthetic regression experiment compares a linear model with a training-mean baseline on held-out data.

From the project checkout, run the routing demo with Python 3.10+ and no extra packages.

```bash
python -m src.claims_workflow "appeal denial" --scope demo-policy
python -m unittest discover -s tests -p test_claims_workflow.py -v
```

The demo uses lexical retrieval and rule-based routing. Its citations are candidates for review. The synthetic evaluations measure behavior on the included examples.

## Python codebase search

[Python Codebase Search](codebase-search/) finds relevant functions and classes in local Python files and returns exact line references. On the included fictional clinic fixture, it ranked the expected function first for five queries and returned no result for one unrelated query. The demo uses keyword retrieval.

## More projects

- [HR analytics](https://github.com/nikhila102/HR-ANALYTICS)
- [Portfolio](https://github.com/nikhila102/portfolio)

[LinkedIn](https://www.linkedin.com/in/nikhila-reddy-0839b51b7)
