def analyze_log(file_path, keyword):
    # Open the specified log file in read mode
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the keyword is present in the current line
            if keyword in line:
                # Print the line after removing leading/trailing whitespace
                print(line.strip())

# Call the function to analyze "/var/log/syslog" for lines containing "error"
analyze_log("/var/log/syslog", "error")
