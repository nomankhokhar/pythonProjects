import smtplib as s  # Import the smtplib library to handle sending emails
from dotenv import load_dotenv  # Import the function to load environment variables from a .env file
import os  # Import the os module to interact with the operating system (used to load environment variables)
from email.mime.multipart import MIMEMultipart  # Import the MIMEMultipart class to create a multipart email (for attachments)
from email.mime.text import MIMEText  # Import the MIMEText class to create the plain text part of the email
from email.mime.base import MIMEBase  # Import the MIMEBase class to handle file attachments
from email import encoders  # Import the encoders to encode the email attachments in base64 format


# Load environment variables from the .env file
load_dotenv()

# Function to login to the email server
def login():
    # Load email and password from environment variables
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

# Initialize the SMTP connection and log in
# This block of code is a function named `login()` that handles the process of logging into an email
# server using SMTP (Simple Mail Transfer Protocol). Here's a breakdown of what it does:
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

# Function to attach files (image, video, etc.)
def attach_file(msg, file_path):
    try:
        filename = os.path.basename(file_path)
        attachment = open(file_path, "rb")  # Open the file in binary mode

        # Create MIMEBase instance
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload((attachment).read())  # Read the attachment

        encoders.encode_base64(mime_base)  # Encode the attachment in base64

        # Add header for the attachment
        mime_base.add_header('Content-Disposition', f'attachment; filename= {filename}')

        # Attach the file to the message
        msg.attach(mime_base)
        attachment.close()  # Close the file after attaching
        print(f"Attached {filename}")
    except Exception as e:
        print(f"Failed to attach {file_path}: {e}")

# Function to send an email with attachments
def send_email(smtp_obj, subject, body, recipients, attachments=[]):
    # Load sender's email from environment variables
    sender = os.getenv("SENDER")

    # Create a MIMEMultipart message object
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Attach any files from the attachments list
    for attachment in attachments:
        attach_file(msg, attachment)

    try:
        # Send the email with attachments
        smtp_obj.sendmail(sender, recipients, msg.as_string())
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
        subject = "Sending email with attachments using Python"
        body = "This email contains an image and a video attachment."
        recipients = ["recipient1@example.com", "recipient2@example.com"]

        # Define the paths to the attachments (image, video, etc.)
        attachments = [
            "attachments/image.png",  # Image file path
            "attachments/video.mp4"   # Video file path
        ]

        send_email(smtp_obj, subject, body, recipients, attachments)
        print("Email sent successfully")

if __name__ == "__main__":
    main()
