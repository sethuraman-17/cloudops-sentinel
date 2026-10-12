import json
from datetime import datetime, timezone

def propose_remediation(report):
    severity = report.get("severity", "UNKNOWN")

    if severity == "HIGH":
        action = "Investigate application failure and consider restarting the service"
    elif severity == "WARNING":
        action = "Review application error and warning logs"
    elif severity == "NORMAL":
        action = "No remediation required"
    else:
        action = "Investigate unknown incident state"

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": severity,
        "proposed_action": action,
        "execution_mode": "DRY_RUN",
        "executed": False
    }

if __name__ == "__main__":
    simulated_report = {
        "severity": "HIGH",
        "findings": ["Application health check failed"]
    }

    plan = propose_remediation(simulated_report)

    print(json.dumps(plan, indent=2))
    print("\nDRY RUN: No service or AWS resource was changed.")

    approval = input(
        "\nType APPROVE to record approval for this proposed action: "
    )

    if approval == "APPROVE":
        plan["approval"] = "APPROVED"
        print("Approval recorded. No remediation was executed.")
    else:
        plan["approval"] = "NOT_APPROVED"
        print("Action not approved. No changes made.")

    with open("remediation_report.json", "w") as file:
        json.dump(plan, file, indent=2)

    print("Report saved to remediation_report.json")
