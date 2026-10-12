import json
from datetime import datetime, timezone
from pathlib import Path
from live_investigation import run_investigation
from remediation import propose_remediation
from ai_investigator import explain_incident

print("Running CloudOps Sentinel...")

incident = run_investigation()
remediation = propose_remediation(incident)
analysis = explain_incident(incident)

result = {
    "project": "CloudOps Sentinel",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "incident": incident,
    "investigation_analysis": analysis,
    "remediation_plan": remediation,
    "safety": {
        "automatic_remediation_enabled": False,
        "human_approval_required": True
    }
}

Path("final_report.json").write_text(json.dumps(result, indent=2))

print(json.dumps(result, indent=2))
print("\nFinal report saved to final_report.json")
print("No remediation was executed.")
