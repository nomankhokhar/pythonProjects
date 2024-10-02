import smtplib as s
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Function to login to the email server
def login():
    # Load email and password from environment variables
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    # Initialize the SMTP connection and log in
    try:
        ob = s.SMTP("smtp.gmail.com", 587)
        ob.ehlo()  # Start the connection
        ob.starttls()  # Secure the connection
        ob.login(email, password)
        print("Login success")
        return ob  # Return the SMTP object if login is successful
    except s.SMTPAuthenticationError:
        print("Login failed: Incorrect email or password")
    except s.SMTPException as e:
        print(f"Login failed due to an SMTP error: {e}")
    return None  # Return None if login fails

# Function to send an email
def send_email(smtp_obj, subject, body, recipients):
    # Load sender's email from the environment variables
    sender = os.getenv("SENDER")

    # Format the email message
    message = f"Subject: {subject}\n\n{body}"

    try:
        smtp_obj.sendmail(sender, recipients, message)
        print("Mailing to all participants")
    except s.SMTPRecipientsRefused:
        print("Failed to send email: All recipients were refused")
    except s.SMTPException as e:
        print(f"Internal server error: {e}")
    finally:
        smtp_obj.quit()  # Close the SMTP connection

# Main function to use the login and send_email functions
def main():
    # Call login function
    smtp_obj = login()

    # If login was successful, send an email
    if smtp_obj:
        subject = "Sending email using Python"
        body = "This is a test email sent using Python"
        recipients = ["recipient1@example.com", "recipient2@example.com"]
        
        send_email(smtp_obj, subject, body, recipients)
        print("Email sent successfully")

if __name__ == "__main__":
    main()
