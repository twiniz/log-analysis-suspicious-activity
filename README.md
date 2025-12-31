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
