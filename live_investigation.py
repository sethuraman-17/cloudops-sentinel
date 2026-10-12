import boto3
import urllib.request
from datetime import datetime, timedelta, timezone
from incident_engine import investigate
from log_analyzer import analyze_logs

REGION = "us-east-2"
INSTANCE_ID = "i-01ab5b9f74026ff2d"
HEALTH_URL = "http://127.0.0.1:8080/health"

def check_application_health():
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=3) as response:
            return response.status == 200
    except Exception:
        return False

def run_investigation():
    cloudwatch = boto3.client("cloudwatch", region_name=REGION)

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(minutes=20)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[{"Name": "InstanceId", "Value": INSTANCE_ID}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
    )

    datapoints = sorted(
        response["Datapoints"],
        key=lambda point: point["Timestamp"]
    )

    application_healthy = check_application_health()
    log_results = analyze_logs()
    error_count = log_results["error_count"]

    if datapoints:
        latest = datapoints[-1]
        cpu = latest["Average"]
        metric_timestamp = latest["Timestamp"].isoformat()
    else:
        cpu = 0
        metric_timestamp = None

    evidence = {
        "application_healthy": application_healthy,
        "cpu_percent": cpu,
        "error_count": error_count
    }

    report = investigate(evidence)
    report["instance_id"] = INSTANCE_ID
    report["metric_timestamp"] = metric_timestamp
    report["application_warnings"] = log_results["warning_count"]
    report["cpu_metrics_available"] = bool(datapoints)

    return report

if __name__ == "__main__":
    report = run_investigation()
    import json
    print(json.dumps(report, indent=2))
