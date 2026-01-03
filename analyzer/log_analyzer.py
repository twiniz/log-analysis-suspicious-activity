import re
from collections import Counter, defaultdict

# -----------------------------
# CONFIG (easy to change later)
# -----------------------------
FAILED_THRESHOLD = 5          # Flag an IP if it has 5+ failed logins
USERNAMES_THRESHOLD = 3       # Flag an IP if it tries 3+ different usernames

LOG_FILE = "sample_auth.log"
REPORT_FILE = "alerts_report.txt"

# -----------------------------
# Helper: extract username + IP
# -----------------------------
# Example line:
# Failed password for invalid user admin from 203.0.113.10 port 51512 ssh2
FAILED_REGEX = re.compile(r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")


def main():
    failed_ip_counts = Counter()                 # counts failures per IP
    ip_to_users = defaultdict(set)               # which usernames each IP tried
    total_lines = 0
    failed_lines = 0

    # 1) Read the log file line by line
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1

            match = FAILED_REGEX.search(line)
            if match:
                failed_lines += 1
                user = match.group("user")
                ip = match.group("ip")

                failed_ip_counts[ip] += 1
                ip_to_users[ip].add(user)

    # 2) Create a SOC-style report
    alerts = []

    for ip, count in failed_ip_counts.items():
        usernames_tried = ip_to_users[ip]

        # Rule A: Too many failed logins from one IP
        if count >= FAILED_THRESHOLD:
            alerts.append(f"[ALERT] Possible brute-force: {ip} had {count} failed login attempts")

        # Rule B: Same IP trying many usernames
        if len(usernames_tried) >= USERNAMES_THRESHOLD:
            alerts.append(f"[ALERT] Username spraying: {ip} tried {len(usernames_tried)} usernames: {sorted(usernames_tried)}")

    # 3) Build summary section
    top_5 = failed_ip_counts.most_common(5)

    report_lines = []
    report_lines.append("SOC Log Analysis Report")
    report_lines.append("=" * 24)
    report_lines.append(f"Log file: {LOG_FILE}")
    report_lines.append(f"Total lines read: {total_lines}")
    report_lines.append(f"Failed login lines found: {failed_lines}")
    report_lines.append("")

    report_lines.append("Top IPs by failed attempts:")
    if top_5:
        for ip, count in top_5:
            report_lines.append(f"- {ip}: {count} failed attempts")
    else:
        report_lines.append("- No failed attempts found")

    report_lines.append("")
    report_lines.append("Alerts:")
    if alerts:
        report_lines.extend(alerts)
    else:
        report_lines.append("No alerts triggered with current thresholds.")

    # 4) Save report to a file (like a SOC ticket/report)
    with open(REPORT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(report_lines))

    # 5) Print a short success message
    print(f"Done. Report saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
