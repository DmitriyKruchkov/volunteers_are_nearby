from datetime import datetime
from models import AlertRequest
from smtp_client import SMTPClient
from scheduler import schedule_email


class AlertController:
    @staticmethod
    def create_alert(alert_request: AlertRequest):
        SMTPClient.send_email("Волонтеры рядом: уведомление о записи", alert_request)
        schedule_email(alert_request)
        return {"detail": "Alert scheduled and initial notification sent"}
