import json
from datetime import datetime, timezone
from live_investigation import run_investigation
from remediation import propose_remediation

print("Running CloudOps Sentinel investigation...")

incident = run_investigation()
remediation = propose_remediation(incident)

result = {
    "project": "CloudOps Sentinel",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "incident": incident,
    "remediation": remediation
}

with open("sentinel_report.json", "w") as file:
    json.dump(result, file, indent=2)

print(json.dumps(result, indent=2))
print("\nReport saved to sentinel_report.json")
print("DRY RUN: No service or AWS resource was changed.")
