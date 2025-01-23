from app.util.log_util import setup_logger

LOGGER = setup_logger('generate_query')
class GenerateQuery():
    logger = None
    def __init__(self):
        self.logger = LOGGER
    