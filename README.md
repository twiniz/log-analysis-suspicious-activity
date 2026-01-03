# Log Analysis – Suspicious Activity Investigation

## Overview
This project simulates a **SOC analyst log investigation** using Linux authentication logs.
The goal is to identify suspicious behavior such as brute-force login attempts and analyze
authentication events to determine whether a system compromise may have occurred.

This project focuses on **investigation, detection, and reporting**, not just scripting.

---

## Scenario
A Linux server experienced multiple failed SSH login attempts from an external IP address.
Security analysts were tasked with reviewing authentication logs to determine:

- Whether a brute-force attack occurred
- If any login attempts were successful
- Which IP addresses and users were involved
- What actions should be taken next

---

## Data Source
- Simulated Linux authentication logs (`auth.log`)
- Log format mirrors real `/var/log/auth.log` entries

---

## Tools & Skills Used
- Linux log analysis
- Python scripting
- Regular expressions (regex)
- Security event investigation
- Incident reporting
- SOC-style documentation

---

## Project Structure

log-analysis-suspicious-activity/
├── analyzer/
│   └── log_analyzer.py        # Python script used to analyze auth logs
├── logs/
│   └── auth.log               # Sample Linux authentication log data
├── reports/
│   └── investigation_report.txt  # Final investigation findings
├── screenshots/
│   └── sample-output.png      # Script execution output
├── README.md

---

## Detection Logic
The analysis script performs the following checks:

- Counts failed SSH login attempts per IP address
- Flags potential brute-force behavior
- Identifies successful login events
- Summarizes findings into a readable investigation report

---

## Findings Summary
- Multiple failed SSH login attempts detected from a single IP
- Activity consistent with a brute-force attempt
- A successful login was later observed from a trusted internal IP
- No evidence of successful compromise from the attacking IP

---

## Outcome
This investigation demonstrates how a SOC analyst:
- Reviews raw log data
- Identifies suspicious patterns
- Separates false positives from real threats
- Documents findings clearly for escalation or remediation

---

## Future Improvements
- Add alert thresholds (e.g., >5 failed attempts)
- Support additional log sources
- Timestamp correlation across events
- Export findings in JSON or CSV format

---

## Disclaimer
All logs and data used in this project are simulated for educational purposes only.

