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


## 🔧 Configuration Highlights
To allow the Wazuh server to communicate with the AI node, the Ollama service was reconfigured to bind to `0.0.0.0`, enabling cross-VM API calls within the laboratory network.
```bash
# Example of the service override used:
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
