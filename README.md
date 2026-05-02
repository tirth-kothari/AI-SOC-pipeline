# AI-Powered SOC Pipeline: Automated Alert Analysis

## 📌 Project Overview
This project bridges the gap between traditional Security Operations Center (SOC) monitoring and Artificial Intelligence. By integrating **Wazuh SIEM** with a local **Llama 3.1 LLM**, this pipeline automatically intercepts high-severity security alerts, analyzes them using AI, and provides actionable mitigation strategies for security analysts.



## 🛠️ Infrastructure & Tech Stack
*   **SIEM:** Wazuh (Manager & Indexer) running on Ubuntu.
*   **AI Engine:** Ollama running Llama 3.1 on a dedicated AI Node.
*   **Virtualization:** Hosted on a Proxmox home lab environment.
*   **Networking:** Secure communication via internal virtual bridges and Tailscale.
*   **Automation:** Python-based bridge script monitoring `alerts.json`.

## 🚀 Features
*   **Real-time Monitoring:** Continuously watches `/var/ossec/logs/alerts/alerts.json` for Level 3+ security events.
*   **AI Analysis:** Sends raw JSON event data to a local Llama 3.1 instance to translate technical logs into human-readable summaries.
*   **Contextual Remediation:** The AI provides specific steps to mitigate the detected threat (e.g., blocking IPs, hardening GPOs).
*   **System Hardening:** Implementation includes advanced Windows security auditing and GPO configurations for endpoint visibility.

## 📂 Repository Structure
*   `scripts/ai_bridge.py`: The core Python logic connecting the Wazuh file system to the Ollama API.
*   `requirements.txt`: Python dependencies (Requests).
*   `README.md`: Project documentation and validation.

## 🧪 Operational Validation
The following screenshot demonstrates the pipeline successfully intercepting a security event and generating an AI-powered analysis:
<img width="1802" height="745" alt="Screenshot 2026-05-02 170517" src="https://github.com/user-attachments/assets/fe049c98-22cc-4f1a-942a-4586a38b3380" />
<img width="1912" height="867" alt="Screenshot 2026-05-02 170401" src="https://github.com/user-attachments/assets/18917fe2-8a3d-4c39-8d7b-6ee411872377" />



## 🔧 Configuration Highlights
To allow the Wazuh server to communicate with the AI node, the Ollama service was reconfigured to bind to `0.0.0.0`, enabling cross-VM API calls within the laboratory network.
```bash
# Example of the service override used:
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

## 🚀 How to Use

Follow these steps to get the AI-SOC bridge running in your environment:

### 1. Prerequisites
*   **Wazuh Manager:** Installed and receiving logs from at least one agent.
*   **Ollama Node:** Ollama installed with the `llama3.1` model pulled (`ollama pull llama3.1`).
*   **Python 3.x:** Installed on the Wazuh Manager with the `requests` library.

### 2. Configure the AI Node
Ensure Ollama is listening for external connections from the Wazuh server:
```bash
sudo systemctl edit ollama.service
# Add the following lines:
[Service]
Environment="OLLAMA_HOST=0.0.0.0"

sudo systemctl daemon-reload
sudo systemctl restart ollama
```

### 3. Setup the Bridge Script
On the **Wazuh Server**, clone this repository and set up the environment:
```bash
git clone [https://github.com/tirth-kothari/AI-SOC-pipeline.git](https://github.com/tirth-kothari/AI-SOC-pipeline.git)
cd AI-SOC-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Deployment
Run the bridge script. It will begin tailing the `alerts.json` file and sending Level 3+ alerts to the AI node for analysis:

```bash
sudo venv/bin/python3 scripts/ai_bridge.py
```
