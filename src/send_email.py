import smtplib
from email.message import EmailMessage
from constants import EMAIL_CREDENTIALS, EMAIL_ADRESSES, EMAIL
import os

def send_emails(content=EMAIL, email_addresses=EMAIL_ADRESSES):
    subject = content.get("SUBJECT", "No Subject")
    message = content.get("MESSAGE", "No Message Content")
    for email in email_addresses:
        send_email(
            send_from=EMAIL_CREDENTIALS["USER"],
            send_to=email,
            subject=subject,
            message=message
        )


def send_email(send_from, send_to, subject, message):
    # Create the email
    msg = EmailMessage()
    msg["From"] = send_from
    msg["To"] = send_to
    msg["Subject"] = subject
    msg.set_content(message)

    
    # Credentials and SMTP server configuration
    smtp_server = EMAIL_CREDENTIALS["HOST"] #"smtp.example.com"
    smtp_port = EMAIL_CREDENTIALS["PORT"] #587  # TLS
    username = EMAIL_CREDENTIALS["USER"] #"you@example.com"
    # password = EMAIL_CREDENTIALS["PASSWORD"]
    
    # Load password from environment variable instead
    password = os.environ[EMAIL_CREDENTIALS["PASSWORD_ENV_NAME"]]


    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        print(f"Sending email with message: {message} to {send_to}")