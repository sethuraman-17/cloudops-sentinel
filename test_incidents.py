from incident_engine import investigate

scenarios = {
    "HEALTHY": {
        "application_healthy": True,
        "cpu_percent": 25,
        "error_count": 0
    },
    "HIGH CPU": {
        "application_healthy": True,
        "cpu_percent": 92,
        "error_count": 0
    },
    "APPLICATION FAILURE": {
        "application_healthy": False,
        "cpu_percent": 30,
        "error_count": 5
    }
}

for name, evidence in scenarios.items():
    report = investigate(evidence)
    print(f"\nScenario: {name}")
    print(f"Severity: {report['severity']}")
    print("Findings:", report["findings"])
from incident_engine import investigate

scenarios = {
    "HEALTHY": {
        "application_healthy": True,
        "cpu_percent": 25,
        "error_count": 0
    },
    "HIGH CPU": {
        "application_healthy": True,
        "cpu_percent": 92,
        "error_count": 0
    },
    "APPLICATION FAILURE": {
        "application_healthy": False,
        "cpu_percent": 30,
        "error_count": 5
    }
}

