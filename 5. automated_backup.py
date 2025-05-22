import shutil  # Import shutil for file operations like copying directories
import time    # Import time to generate timestamps

def backup(src, dest):
    # Generate a timestamp in the format YYYYMMDD-HHMMSS
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    # Create the destination path with the timestamp
    dest_with_time = f"{dest}/backup_{timestamp}"
    # Copy the entire source directory to the new destination
    shutil.copytree(src, dest_with_time)
    # Print a message indicating the backup is complete
    print(f"Backup completed: {dest_with_time}")

# Call the backup function to back up the /etc directory to /backups
backup("/etc", "/backups")

# This script creates a backup of the /etc directory and saves it to the /backups directory with a timestamp.
# It uses the shutil library to copy the directory and its contents.