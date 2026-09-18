import csv
from pathlib import Path

ROOT = Path(__file__).parent

weights = {}
with open(ROOT / "SCORING_MODEL.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        weights[row["metric_id"]] = float(row["weight"])

rows = []
with open(ROOT / "SCORE_MATRIX.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        calc = sum(float(row[m]) / 5.0 * weight for m, weight in weights.items())
        declared = float(row["final_score"])
        if round(calc, 6) != round(declared, 6):
            raise SystemExit(f"Mismatch for {row['participant']}: calculated={calc}, declared={declared}")
        rows.append({
            "rank": row["rank"],
            "participant": row["participant"],
            "eligible": row["eligible"],
            "score": calc
        })

for row in rows:
    marker = "" if row["eligible"] == "TRUE" else " [OUTSIDE ELIGIBILITY GATE]"
    print(f"{row['rank'] or '--':>2}. {row['participant']}: {row['score']:g}/100{marker}")

print("OK: weights =", sum(weights.values()), "participants =", len(rows))
