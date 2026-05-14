# STYX OBLIVION v1.5
**Logic Suppression & Adaptive Deception Engine**

## Tactical Objective
**STYX OBLIVION** is engineered to neutralize the analytical capabilities of Blue Teams. Unlike traditional DoS tools, it targets the **Logic Layer** of Security Information and Event Management (SIEM) and Intrusion Prevention Systems (IPS).


## Key Features
- **Protocol Fuzzing:** Injects malformed TCP/UDP flags (FSRPAU) to force deep packet inspection (DPI) latency.
- **AI Poisoning:** Generates high-entropy packets designed to confuse Machine Learning-based anomaly detection.
- **HP-Deception Module:** Implements proprietary noise generation to trigger "Alert Fatigue" in Security Operation Centers (SOC).

## Installation & Usage
```bash
# Install dependencies
pip3 install -r requirements.txt

# Execute Suppression (Requires Root)
sudo python3 styx_oblivion.py <TARGET_IP>
