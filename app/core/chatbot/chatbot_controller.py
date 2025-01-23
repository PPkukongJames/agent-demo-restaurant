from app.util.log_util import setup_logger
from fastapi import Response
import json
from .chatbot_manager import ChatbotManager
from .domain import UserInference

LOGGER = setup_logger('chatbot_controller')
class ChatbotController:
    
    logger = None
    manager = None
    
    def __init__(self):
        self.logger = LOGGER
        self.manager = ChatbotManager()

    def inference(self,criteria:UserInference):
        self.logger('%s',criteria)
        response = None
        
        try :
            results = self.manager.inference(criteria)
            self.logger.debug(results)
            response = Response(
                content=json.dumps(results),
                status_code=200,
                media_type='application/json'
            )
        except KeyError as e:
            error_message = {'message': str(e)}
            response = Response(
                content=json.dumps(error_message),
                status_code=400,
                media_type='application/json'
            )
        except Exception as e:
            # Handle all other exceptions
            error_message = {'message': str(e)}
            response = Response(
                content=json.dumps(error_message),
                status_code=500,
                media_type='application/json'
            )
            self.logger.error('Exception occurred', exc_info=True)
            
        return response
        