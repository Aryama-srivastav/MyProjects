import random
import string
import smtplib
from email.mime.text import MIMEText

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_email(sender_email, app_password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        print("OTP sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def main():
    sender_email = 'your_email@gmail.com'  # Replace with your Gmail 2 step enabled 
# go to https://myaccount.google.com/apppasswords to generate a password
    app_password = 'dypj fota gjkd rsxf'     # Replace with your 16-char app password
    recipient_email = input("Enter recipient email: ").strip()

    otp = generate_otp()
    subject = "Your OTP Verification Code"
    body = f"Your OTP is: {otp}"

    send_email(sender_email, app_password, recipient_email, subject, body)

    # OTP Verification
    user_otp = input("Enter the OTP you received: ").strip()
    if user_otp == otp:
        print("OTP matched! Email verified.")
    else:
        print("Invalid OTP. Verification failed.")

if __name__ == '__main__':
    main()
