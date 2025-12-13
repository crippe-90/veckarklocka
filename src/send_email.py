import smtplib
from email.message import EmailMessage
from constants import EMAIL_CREDENTIALS


def send_emails(message, email_addresses):
    for email in email_addresses:
        send_email(
            send_from=EMAIL_CREDENTIALS["USER"],
            send_to=email,
            subject="Notification",
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
    password = EMAIL_CREDENTIALS["PASSWORD"] #"your_password"


    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        print(f"Sending email with message: {message} to {send_to}")