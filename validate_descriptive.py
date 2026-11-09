#!/usr/bin/env python3
import csv, json
from pathlib import Path
root=Path(__file__).resolve().parent
def read(name):
 with (root/name).open(encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f))
co=read("COMPANY_SUMMARIES.csv"); off=read("OFFER_OBSERVATIONS.csv"); so=read("SOURCE_REGISTER.csv"); cl=read("FACT_CLAIM_MAP.csv"); li=read("CLAIM_SOURCE_LINKS.csv")
assert len(co)==23 and len(set(x["candidate_id"] for x in co))==23
assert len(off)==59 and len(so)==31 and len(set(x["url"] for x in so))==30
assert len(cl)==41 and len(li)==42
units=[x["step5_price_unit"] for x in off]
assert (units.count("MONTH"),units.count("UNKNOWN"),len(units)-units.count("MONTH")-units.count("UNKNOWN"))==(30,20,9)
r=json.loads((root/"RESULTS.json").read_text(encoding="utf-8"))
assert r["ranking"] is None and r["statistics"]["verifiedFullThreeMonthEstimates"]==0
print("PASS: documentary comparison, 23 companies, 59 observations, 31 sources, 41 claims.")
