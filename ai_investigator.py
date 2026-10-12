import json
from pathlib import Path

def explain_incident(report):
    severity = report.get("severity", "UNKNOWN")
    evidence = report.get("evidence", {})
    findings = report.get("findings", [])
    recommendations = report.get("recommendations", [])

    healthy = evidence.get("application_healthy")
    cpu = evidence.get("cpu_percent")
    errors = evidence.get("error_count", 0)

    if severity == "HIGH":
        assessment = (
            "Critical application availability issue detected. "
            "Investigate the service and its logs immediately."
        )
    elif severity == "WARNING":
        assessment = (
            "Potential application or resource issue detected. "
            "Review the evidence before taking action."
        )
    elif severity == "NORMAL":
        assessment = (
            "No configured incident conditions were detected "
            "in the available evidence."
        )
    else:
        assessment = (
            "Severity is unknown. Validate the monitoring data "
            "before taking action."
        )

    return {
        "analysis_type": "Local rule-based explanation",
        "severity": severity,
        "assessment": assessment,
        "evidence_summary": {
            "application_healthy": healthy,
            "cpu_percent": cpu,
            "error_count": errors
        },
        "findings": findings,
        "recommended_next_steps": recommendations,
        "automated_action_taken": False
    }

if __name__ == "__main__":
    path = Path("sentinel_report.json")
    data = json.loads(path.read_text())
    incident = data.get("incident", data)

    explanation = explain_incident(incident)

    Path("ai_analysis.json").write_text(
        json.dumps(explanation, indent=2)
    )

    print(json.dumps(explanation, indent=2))
    print("\nSaved to ai_analysis.json")
    print("Note: This is rule-based analysis, not a generative AI model.")
