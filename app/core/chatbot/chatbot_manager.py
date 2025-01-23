from app.util.log_util import setup_logger
import json
from .chatbot_service import ChatbotService
from .domain import UserInference

LOGGER = setup_logger('chatbot_manager')
class ChatbotManager:
    
    logger = None
    service = None
    
    def __init__(self):
        self.logger = LOGGER
        self.service = ChatbotService()

    def inference(self,criteria:UserInference):
        self.logger.debug("%s","manager")
        
        # ตรวจสอบว่า Token หมดอายุหรือยัง
        self.service.check_timestamp(criteria)
        
        
        