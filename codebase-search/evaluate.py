"""Report retrieval quality on a small, authored evaluation set."""
from pathlib import Path
from search import index, search

CASES = {
    "cancel appointment": "cancel_appointment",
    "release time slot": "cancel_appointment",
    "get waitlist": "get_waitlist",
    "patients waiting for an opening": "get_waitlist",
    "scheduled visit reminder": "reminder_message",
    "volcano telemetry": None,
}


def main():
    records = list(index(Path(__file__).with_name("demo")))
    ranks = []
    abstentions = []
    for query, expected in CASES.items():
        hits = [hit["symbol"] for hit in search(records, query, limit=3)]
        print(f"{query!r}: {hits}")
        if expected is None:
            abstentions.append(not hits)
        else:
            ranks.append(hits.index(expected) + 1 if expected in hits else 0)
    print(f"Recall@1: {sum(rank == 1 for rank in ranks)}/{len(ranks)}")
    print(f"Recall@3: {sum(rank > 0 for rank in ranks)}/{len(ranks)}")
    print(f"Correct abstentions: {sum(abstentions)}/{len(abstentions)}")
    return int(not all(ranks) or not all(abstentions))


if __name__ == "__main__":
    raise SystemExit(main())
