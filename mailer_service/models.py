from email.mime.multipart import MIMEMultipart

from pydantic import BaseModel, EmailStr
from datetime import datetime


class AlertRequest(BaseModel):
    email: EmailStr
    alert_date: datetime
    event_title: str
    message: str
    event_description: str