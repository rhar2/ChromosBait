import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, subject, body):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'rhjananiya@gmail.com'
    smtp_password = 'dqdy pbav ztyn mjdv'

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS for security
        server.login(smtp_user, smtp_password)

        # Send the email
        server.sendmail(smtp_user, recipient_email, msg.as_string())
        print('Email sent successfully')

        # Disconnect from the server
        server.quit()

    except Exception as e:
        print(f'Failed to send email: {e}')

# Example usage
if _name_ == '_main_':
    recipient_email = 'h0r402040@gmail.com'
    subject = 'Automated Email'
    body = 'This is an automated email sent by a Python script. https://chronosbait.onrender.com/'
    send_email(recipient_email, subject, body)