import json

LOG_FILE = "app.log"

def analyze_logs():
    error_count = 0
    warning_count = 0
    error_messages = []
    warning_messages = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            entry = line.strip()
            upper_entry = entry.upper()

            if "ERROR" in upper_entry:
                error_count += 1
                error_messages.append(entry)
            elif "WARNING" in upper_entry or " WARN " in f" {upper_entry} ":
                warning_count += 1
                warning_messages.append(entry)

    return {
        "error_count": error_count,
        "warning_count": warning_count,
        "error_messages": error_messages,
        "warning_messages": warning_messages
    }

if __name__ == "__main__":
    print(json.dumps(analyze_logs(), indent=2))
