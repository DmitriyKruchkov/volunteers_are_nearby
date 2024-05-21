import smtplib
from datetime import datetime, timedelta
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

from models import AlertRequest

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


class SMTPClient:
    @staticmethod
    def send_email(subject, alert_request: AlertRequest):
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = alert_request.email
        msg['Subject'] = subject
        parsed_date = datetime.fromisoformat(str(alert_request.alert_date))
        formatted_date = parsed_date.strftime("%d.%m.%Y %H:%M")
        html = f"""
            <html>
            <head></head>
            <body>
                <h2>Оповещение о событии</h2>
                <h3>{alert_request.event_title}</h3>
                <p><strong>Дата начала события:</strong> {formatted_date}</p>
                <p>{alert_request.event_description}</p>
                <img src="cid:event_image">
            </body>
            </html>
            """
        msg.attach(MIMEText(html, 'html'))
        with open("static/default.jpg", 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<event_image>')
            img.add_header('Content-Disposition', 'inline', filename=os.path.basename("static/default.jpg"))
            msg.attach(img)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, alert_request.email, msg.as_string())
