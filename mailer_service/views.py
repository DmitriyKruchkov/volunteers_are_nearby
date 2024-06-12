from fastapi import APIRouter
from models import AlertRequest
from controllers import AlertController

router = APIRouter()

@router.post("/alert/")
def create_alert(alert_request: AlertRequest):
    return AlertController.create_alert(alert_request)
