
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mailer:
    def send(receiver_email, subject, mailcontent):
        sender_email = "crm.marketing1920@gmail.com"
        password = "crm@marketing@1920"

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email
        print("setted up")
        # Create the plain-text and HTML version of your message
        text = mailcontent
        """\
        Hi,
        How are you?
        CRM is there for you."""
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               CRM is there for you.
            </p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")
        print("added mime")
        message.attach(part1)
        # message.attach(part2)
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(sender_email, password)
            print("logged in")
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("sent mail")
            server.quit()
        except Exception as sm:
            print("error", sm)
