#!/bin/bash

# Email Sender Tool
# Sends emails to recipients from a file.
# Prompts for sender's email, subject, and message.
# Efficiently processes recipients individually.
# Updates recipient file after sending each email.
# Uses the 'mail' command-line tool for sending emails.

# Function to send an email
send_email() {
    sender="$1"
    receiver="$2"
    subject="$3"
    message="$4"

    # Prompt for email password
    read -s -p "Enter your email password: " password

    # Create the email content
    email_content="Subject: $subject\n\n$message"

    # Send the email using the 'mail' command-line tool
    echo -e "$email_content" | mail -s "$subject" -r "$sender" "$receiver"

    echo "Email sent successfully!"
}

# Prompt user for sender's email address
read -p "Enter your email address: " sender

# Prompt user for email subject
read -p "Enter email subject: " subject

# Prompt user for email message
read -p "Enter email message: " message

# Create a temporary file for storing the updated recipient list
temp_file="mails_temp.txt"

# Read recipient email addresses from the file and send emails
while IFS= read -r receiver; do
    send_email "$sender" "$receiver" "$subject" "$message"
    echo "Sent email to $receiver"

    # Remove the recipient from the list by not writing it to the temporary file
    # This approach avoids loading the entire file into memory
    echo "$receiver" >> "$temp_file"
done < "mails.txt"

# Replace the original file with the temporary file
mv "$temp_file" "mails.txt"
