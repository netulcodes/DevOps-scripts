# DevOps-scripts

1. Port Scanner
✅ Purpose:
Check for open TCP ports on a given IP or hostname.

📋 Description:
Helps detect which ports are open on a machine—useful for troubleshooting firewalls or verifying service availability.

🛠️ How to Use:
python port_scanner.py

🧪 Example Output:

Port 22 is open
Port 80 is open

🖥️ 2. Server Health Check Script
✅ Purpose:
Monitor key system metrics like CPU, RAM, and disk usage.

📋 Description:
This script uses the psutil library to print out system health metrics. Useful for setting up regular system audits or quick diagnostics.

🛠️ How to Use:
pip install psutil
python server_health_check.py

🧪 Example Output:

Hostname: myserver
CPU Usage: 15.5 %
Memory Usage: 67.3 %
Disk Usage: 52.1 %

📑 3. Log File Analyzer
✅ Purpose:
Find important messages or error lines in log files.

📋 Description:
Scans any log file for specific keywords like "error", "fail", or custom patterns.

🛠️ How to Use:

enter the log filepath and keyword which needs to be analysed.
analyze_log("/var/log/syslog", "error")
python log_analyzer.py

this script can be added in the cron job which will anlayze the log file as per schedule and trigger the email ( extra code snippet)

📧 4. Send Email via SMTP
✅ Purpose:
Send automated notification or alert emails using an SMTP server.

📋 Description:
This script uses Python’s built-in smtplib and email.mime.text.MIMEText to send plain text emails. It’s ideal for alerting system admins, notifying developers of CI/CD status, or sending updates from monitoring systems.

Supports TLS encryption.

Requires SMTP credentials (e.g., Gmail, custom mail server).

Easily integratable with other tools or scripts.

🛠️ How to Use:
1. Install Requirements:
This script uses standard libraries. No external packages are needed.

2. Configure the Script:
Update these lines with your SMTP details:

smtp_server = "smtp.example.com"     # e.g., smtp.gmail.com
smtp_port = 587                      # 587 for TLS
sender_email = "you@example.com"
sender_password = "your_password_or_app_token"
3. Call the Function:

send_email("Subject Line", "This is the body of the email", "recipient@example.com")
4. Run the Script:

python send_email.py

🧪 Example Use Case:

send_email(
    subject="Build Failed",
    body="The latest deployment failed. Check the Jenkins logs.",
    to_email="devops.team@company.com"
)