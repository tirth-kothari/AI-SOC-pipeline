import json
import requests
import time

# Configuration
WAZUH_ALERTS_PATH = "/var/ossec/logs/alerts/alerts.json"
OLLAMA_API_URL = "http://10.10.10.23:11434/api/generate"  # Your AI Node IP
SEVERITY_THRESHOLD = 3  # Only send Level 10+ alerts to AI

def ask_ai(alert_data):
    prompt = f"Analyze this security alert and provide a brief summary and mitigation steps: {alert_data}"
    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        return response.json().get("response", "No response from AI.")
    except Exception as e:
        return f"Error connecting to AI: {e}"

def monitor_alerts():
    print(f"Monitoring Wazuh alerts for Level {SEVERITY_THRESHOLD}+ events...")
    # Open the file and move to the end
    with open(WAZUH_ALERTS_PATH, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            
            alert = json.loads(line)
            level = alert.get("rule", {}).get("level", 0)
            
            if level >= SEVERITY_THRESHOLD:
                description = alert.get("rule", {}).get("description", "Unknown Alert")
                print(f"🚨 High Severity Alert Detected: {description}")
                analysis = ask_ai(description)
                print(f"🧠 AI Analysis: {analysis}\n")

if __name__ == "__main__":
    monitor_alerts()
