from app.util.log_util import setup_logger

LOGGER = setup_logger('understand_question')
class UnderstandQuestion():
    logger = None
    def __init__(self):
        self.logger = LOGGER
    