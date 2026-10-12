# CloudOps Sentinel

A Python-based cloud operations monitoring and incident investigation prototype built with AWS EC2 and CloudWatch.

## Features
- Collects EC2 CPU metrics using AWS CloudWatch and Boto3.
- Checks application availability through an HTTP health endpoint.
- Analyzes local application logs for ERROR and WARNING entries.
- Classifies incidents by severity.
- Generates a rule-based investigation explanation.
- Creates a remediation proposal in dry-run mode.
- Saves a consolidated JSON report.

## Architecture
AWS EC2 and CloudWatch
        |
        v
Python Monitoring and Health Check
        |
        v
Application Log Analyzer
        |
        v
Incident Classification Engine
        |
        v
Investigation Explanation
        |
        v
Dry-Run Remediation Plan
        |
        v
final_report.json

## Technology Stack
- AWS EC2
- AWS CloudWatch
- Python
- Boto3
- Linux
- JSON
- Git

## Run
Start the application in one terminal:
    python3 app.py

Run the investigation in another terminal:
    cd ~/cloudops-sentinel
    python3 final_report.py

## Safety
Remediation is currently a proposal only. No automatic service restart or AWS resource modification is performed.

## Limitations
- The explanation engine is rule-based, not generative AI.
- Logs are read from a local file.
- Remediation execution is not implemented.
- This is a prototype, not a production incident-management platform.

## Future Improvements
- Automated testing and structured logging.
- Optional AI-powered root-cause analysis.
- Enforced human approval before remediation.
- Secure deployment and operational monitoring.
