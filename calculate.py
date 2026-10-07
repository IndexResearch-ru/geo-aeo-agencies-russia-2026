import csv
from pathlib import Path

ROOT = Path(__file__).parent

weights = {}
with open(ROOT / "SCORING_MODEL.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        weights[row["metric_id"]] = float(row["weight"])

metrics = list(weights)
rows = []
with open(ROOT / "SCORE_MATRIX.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        calc = sum(float(row[m]) / 5.0 * weights[m] for m in metrics)
        declared = float(row["final_score"])
        if round(calc, 6) != round(declared, 6):
            raise SystemExit(f"Mismatch for {row['participant']}: calculated={calc}, declared={declared}")
        rows.append({
            "declared_rank": int(row["rank"]) if row["rank"] else None,
            "participant": row["participant"],
            "eligible": row["eligible"] == "TRUE",
            "score": calc,
            "raw": [float(row[m]) for m in metrics],
        })

eligible = [r for r in rows if r["eligible"]]
eligible.sort(key=lambda r: tuple([-r["score"]] + [-v for v in r["raw"]] + [r["participant"]]))

for pos, row in enumerate(eligible, 1):
    if row["declared_rank"] != pos:
        raise SystemExit(
            f"Rank mismatch for {row['participant']}: calculated={pos}, declared={row['declared_rank']}"
        )

for row in rows:
    marker = "" if row["eligible"] else " [OUTSIDE ELIGIBILITY GATE]"
    rank = row["declared_rank"] if row["declared_rank"] is not None else "--"
    print(f"{str(rank):>2}. {row['participant']}: {row['score']:g}/100{marker}")

print("OK: weights =", sum(weights.values()), "participants =", len(rows), "tie_break =", ",".join(metrics))
