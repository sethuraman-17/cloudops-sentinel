import boto3
from datetime import datetime, timedelta, timezone

REGION = "us-east-2"
INSTANCE_ID = "i-01ab5b9f74026ff2d"

cloudwatch = boto3.client("cloudwatch", region_name=REGION)

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=3)

response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[
        {
            "Name": "InstanceId",
            "Value": INSTANCE_ID
        }
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average", "Maximum"]
)

datapoints = sorted(
    response["Datapoints"],
    key=lambda point: point["Timestamp"]
)

print("CloudOps Sentinel - Live CloudWatch Metrics")
print(f"Instance: {INSTANCE_ID}")
print(f"Region: {REGION}")

if not datapoints:
    print("No CPU datapoints returned for the last 3 hours.")
else:
    for point in datapoints:
        print(
            f"Time: {point['Timestamp'].isoformat()} | "
            f"Average CPU: {point['Average']:.2f}% | "
            f"Maximum CPU: {point['Maximum']:.2f}%"
        )
