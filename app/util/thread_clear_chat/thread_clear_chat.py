

from app.util.log_util import setup_logger
from datetime import datetime, timedelta
from app.core.config import global_variable
from app.core.config.application import APPLICATION_CONFIG

LOGGER = setup_logger('thread run')
class ThreadClearChat():
    
    _instance = None
    logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls.logger = LOGGER
            cls._instance = super(ThreadClearChat, cls).__new__(cls)
            
        return cls._instance
    
    def check_user(self):
        timestamp_now = datetime.now()
        tokens = list(global_variable.user_remember.keys())
        self.logger.debug("tokens all : %s",tokens)
        for token in tokens :
            users = list(global_variable.user_remember[token].keys())
            self.logger.debug("users all : %s",users)
            for user in users :
                if abs(global_variable.user_remember[token][user]['timestampe'] - timestamp_now) > timedelta(seconds=APPLICATION_CONFIG['expired']) :
                    del global_variable.user_remember[token][user]