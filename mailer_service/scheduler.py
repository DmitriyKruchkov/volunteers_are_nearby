from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from smtp_client import SMTPClient

scheduler = BackgroundScheduler()
scheduler.start()


def schedule_email(alert_request):
    scheduler.add_job(
        send_scheduled_email,
        'date',
        run_date=alert_request.alert_date - timedelta(hours=3),
        args=[alert_request]
    )


def send_scheduled_email(alert_request):
    SMTPClient.send_email("Волонтеры рядом: уведомление о событии", alert_request)
