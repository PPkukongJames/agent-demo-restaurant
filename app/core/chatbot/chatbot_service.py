from datetime import datetime, timedelta
from app.util.log_util import setup_logger
import json
import string
import random
from .domain import UserInference
from app.core.config import global_variable
from app.core.config.application import APPLICATION_CONFIG

LOGGER = setup_logger('chatbot_service')
class ChatbotService:
    logger = None
    
    def __init__(self):
        self.logger = LOGGER
        
    def inference(self,criteria:UserInference):
        self.logger.debug("service")
    
    def check_timestamp(self,criteria:UserInference):
        # ตรวจสอบว่า token ที่ส่งมา มีท่เก็บใน memory ไหม 
        if criteria.token not in list(global_variable.user_remember.keys()) :
            # ถ้าไม่มีให้สร้างเป็น key ไว้
            global_variable.user_remember[criteria.token] = {}
        try :
            self.logger.debug("user is %s",global_variable.user_remember[criteria.token][criteria.user_id])
        except :  # noqa: E722
            self.logger.debug("user is new user %s", criteria.user_id )
            
        # ดึง timestamp เวลาปัจจุบัน
        timestamp_now = datetime.now()
        
        # ตรวจสอบว่า user ดังกล่าวมีบันทึกไว้ใน memort ไหม
        if criteria.user_id not in list(global_variable.user_remember[criteria.token].keys()) :
            # ถ้าไม่มี บันทึก user_id นั้นไว้ใน token ที่ส่งมาพร้อม user
            global_variable.user_remember[criteria.token][criteria.user_id] = {
                'thread_id': self.generate_random_string(),
                'timestampe': timestamp_now,
                'history':self.new_chat()
            }
        elif abs(global_variable.user_remember[criteria.token][criteria.user_id]['timestampe'] - timestamp_now) > timedelta(seconds=APPLICATION_CONFIG['timeout']) :
            # ถ้ามี user เคยคุยไว้และยังไม่ถูกลบออก ให้ตรวจสอบว่า เวลาใน timestamp - now เกินเวลาที่กำหนดหรือยัง ถ้าเกินให้ลบ thread id เดิม และสร้างอันใหม่พร้อมกับบันทึกเวลาใหม่
            self.logger.debug("more %s min create new thread",str(APPLICATION_CONFIG['timeout']/60))
            global_variable.user_remember[criteria.token][criteria.user_id]['timestampe'] = timestamp_now
            global_variable.user_remember[criteria.token][criteria.user_id]['thread_id'] = self.generate_random_string()
            global_variable.user_remember[criteria.token][criteria.user_id]['history'] = self.new_chat()
            
        elif abs(global_variable.user_remember[criteria.token][criteria.user_id]['timestampe'] - timestamp_now) <= timedelta(seconds=APPLICATION_CONFIG['timeout']) :
            # ถ้ามี user เคยคุยไว้ แต่เวลายังไม่เกิน ให้ต่อเวลาอีกให้
            global_variable.user_remember[criteria.token][criteria.user_id]['timestampe'] = timestamp_now
        
        global_variable.user_remember[criteria.token][criteria.user_id]['history']['messages'].append({
            "role": "user",
            "content": criteria.message
        })
        
    def generate_random_string(self,length=20,thread_id=None):
        characters = string.ascii_letters + string.digits
        thread_id = 'thread_'+''.join(random.choice(characters) for _ in range(length))
        
        return thread_id
    
    def new_chat(self):
        return {
            'messages':[],
        }