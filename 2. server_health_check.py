import psutil  # Import psutil for accessing system resource information
import socket  # Import socket to get the system's hostname

def check_health():
    # Print the hostname of the current machine
    print("Hostname:", socket.gethostname())
    # Print the CPU usage percentage over a 1 second interval
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    # Print the percentage of memory used
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
    # Print the percentage of disk space used on the root directory
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")

if __name__ == "__main__":
    check_health()  # Run the health check if the script is executed directly

# This script checks the health of the server by printing the hostname, CPU usage, memory usage, and disk usage.
# It uses the psutil library to gather system information and the socket library to get the hostname.