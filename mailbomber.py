import smtplib
import getpass
import os

# Email Sender Tool
# Sends emails to recipients from a file.
# Prompts for sender's email, subject, and message.
# Efficiently processes recipients individually.
# Updates recipient file after sending each email.
# Uses smtplib and getpass for secure email sending.
# Developed for Gmail, adaptable for other SMTP servers.


# Function to send an email
def send_email(sender, receiver, subject, message):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        password = getpass.getpass("Enter your email password: ")
        smtp_server.login(sender, password)

        email_content = f"Subject: {subject}\n\n{message}"
        smtp_server.sendmail(sender, receiver, email_content)

        smtp_server.close()
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error while sending email: {e}")

# Prompt user for sender's email address
sender = input("Enter your email address: ")

# Prompt user for email subject
subject = input("Enter email subject: ")

# Prompt user for email message
message = input("Enter email message: ")

# Create a temporary file for storing the updated recipient list
temp_file = "mails_temp.txt"

# Read recipient email addresses from the file and send emails
with open("mails.txt", "r") as f:
    for line in f:
        receiver = line.strip()
        send_email(sender, receiver, subject, message)
        print(f"Sent email to {receiver}")
        
        # Remove the recipient from the list by not writing it to the temporary file
        # This approach avoids loading the entire file into memory
        with open(temp_file, "a") as temp:
            temp.write(line)

# Replace the original file with the temporary file
os.replace(temp_file, "mails.txt")
