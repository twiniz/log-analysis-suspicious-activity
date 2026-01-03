# Log Analysis & Suspicious Activity Detection

## Overview
This project is a beginner-friendly SOC-style log analysis tool written in Python.
It analyzes authentication logs to identify suspicious activity such as brute-force
attacks and username spraying attempts.

The goal of this project is to demonstrate practical defensive security skills,
log analysis, and basic threat detection logic used in Security Operations Centers (SOC).



## What This Tool Detects
 Multiple failed login attempts from the same IP (possible brute-force)
 Multiple usernames targeted by a single IP (username spraying)
 Top IP addresses by failed login attempts



## How It Works
1. Reads an authentication log file (`sample_auth.log`)
2. Extracts IP addresses and usernames from failed login events
3. Applies simple detection thresholds
4. Generates a SOC-style alert report (`alerts_report.txt`)



## Technologies Used
 Python
 Regular Expressions (Regex)
 Linux (Kali)
 Log analysis concepts
 Defensive security fundamentals



## Files in This Repository
 `log_analyzer.py` – Analyzes logs and detects suspicious activity
 `sample_auth.log` – Sample authentication log for testing
 `alerts_report.txt` – Generated security alert report
 `README.md` – Project documentation



## Why This Project Matters
Log analysis is a core responsibility of SOC analysts.
This project demonstrates how attackers behave in logs and how defenders
can detect and document suspicious activity using simple, effective logic.

log-analysis-suspicious-activity/
├── analyzer/
│   └── log_analyzer.py
├── logs/
│   └── auth.log
├── reports/
│   └── investigation_report.txt
├── screenshots/
│   └── sample-output.png
├── README.md

## Overview
This project simulates a **SOC investigation** by analyzing Linux authentication logs to detect suspicious activity and potential compromise.

## Threats Detected
- Brute-force login attempts
- Privilege escalation via sudo/su
- Suspicious access to sensitive system files
- Post-compromise behavior indicators

## How It Works
1. Parses Linux auth logs
2. Applies detection rules
3. Flags high-risk behavior
4. Generates an investigation report

## Sample Output
(Include screenshot or pasted output)

## Why This Matters
These detections mirror what SOC analysts monitor daily to identify early-stage attacks and insider threats.


