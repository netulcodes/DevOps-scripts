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