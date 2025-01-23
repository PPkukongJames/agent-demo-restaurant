from fastapi import APIRouter
from app.util.log_util import setup_logger
from .chatbot_controller import ChatbotController
from .domain import UserInference

router = APIRouter()
logger = setup_logger('chatbot_init')
CONTROLER = ChatbotController()
@router.post("/inference")
def inference(criteria:UserInference):
    logger.debug('chatbot inference')
    return CONTROLER.inference(criteria)

