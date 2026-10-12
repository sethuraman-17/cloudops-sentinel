from datetime import datetime, timezone
import json

def investigate(data):
    findings = []
    recommendations = []

    if not data.get("application_healthy", True):
        findings.append("Application health check failed")
        recommendations.append(
            "Inspect application logs and service status"
        )

    cpu = data.get("cpu_percent", 0)
    if cpu >= 80:
        findings.append(f"High CPU utilization: {cpu}%")
        recommendations.append(
            "Inspect running processes and recent workload changes"
        )

    errors = data.get("error_count", 0)
    if errors > 0:
        findings.append(f"Application errors detected: {errors}")
        recommendations.append(
            "Review the relevant error logs"
        )

    if not findings:
        findings.append("No configured incident conditions detected")
        recommendations.append("Continue monitoring")

    return {
        "project": "CloudOps Sentinel",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": (
            "HIGH" if not data.get("application_healthy", True)
            else "WARNING" if cpu >= 80 or errors > 0
            else "NORMAL"
        ),
        "findings": findings,
        "recommendations": recommendations,
        "evidence": data,
    }


if __name__ == "__main__":
    sample = {
        "application_healthy": False,
        "cpu_percent": 87,
        "error_count": 5,
    }

    report = investigate(sample)
    print(json.dumps(report, indent=2))
from datetime import datetime, timezone
import json

def investigate(data):
    findings = []
    recommendations = []

    if not data.get("application_healthy", True):
        findings.append("Application health check failed")
        recommendations.append(
            "Inspect application logs and service status"
        )

    cpu = data.get("cpu_percent", 0)
    if cpu >= 80:
        findings.append(f"High CPU utilization: {cpu}%")
        recommendations.append(
            "Inspect running processes and recent workload changes"
        )

    errors = data.get("error_count", 0)
    if errors > 0:
        findings.append(f"Application errors detected: {errors}")
        recommendations.append(
            "Review the relevant error logs"
        )

    if not findings:
        findings.append("No configured incident conditions detected")
        recommendations.append("Continue monitoring")

    return {
        "project": "CloudOps Sentinel",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": (
            "HIGH" if not data.get("application_healthy", True)
            else "WARNING" if cpu >= 80 or errors > 0
            else "NORMAL"
        ),
        "findings": findings,
        "recommendations": recommendations,
        "evidence": data,
    }


