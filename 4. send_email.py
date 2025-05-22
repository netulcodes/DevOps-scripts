import smtplib  # Import smtplib for sending emails via SMTP
from email.mime.text import MIMEText  # Import MIMEText to create email messages

def send_email(subject, body, to_email):
    # SMTP server configuration
    smtp_server = "smtp server details"  # Replace with your SMTP server address
    smtp_port = 587  # Standard port for TLS
    sender_email = "noreply@customdomain.com"  # Sender's email address
    sender_password = "xxxxxxxx"  # Sender's email password or app password

    # Create the email message
    msg = MIMEText(body)  # Set the email body
    msg['Subject'] = subject  # Set the email subject
    msg['From'] = sender_email  # Set the sender's email address
    msg['To'] = to_email  # Set the recipient's email address

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()  # Identify ourselves to the SMTP server
            server.starttls()  # Secure the connection with TLS
            server.ehlo()  # Re-identify after starting TLS
            server.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, to_email, msg.as_string())  # Send the email
        print("Email sent successfully.")  # Print success message
    except Exception as e:
        print(f"Failed to send email: {e}")  # Print error message if sending fails

# Example usage: send a test email
send_email("testing", "This is a test email", "senderemail@gmail.com")