from fastapi import FastAPI,Request
from app.util.log_util import setup_logger,set_submit_id
from app.util.thread_clear_chat import ThreadClearChat
from app.core.example import router as example_router
from app.core.config.application import APPLICATION_CONFIG
import uvicorn
import time
import threading
import json
import contextvars
import random
import string
from contextlib import asynccontextmanager  # noqa: E402

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Application startup")
    yield
    # Shutdown
    logger.info("Application shutdown")

    
logger = setup_logger('main')
app = FastAPI(lifespan=lifespan)

submit_id_var = contextvars.ContextVar('submit_id', default='')

@app.middleware("http")
async def log_request(request: Request, call_next):
    # ดึงค่าจาก body
    body = await request.body()
    body_str = None
    try :
        body_str = dict(json.loads(body.decode("utf-8")))# แปลงเป็น string
    except :  # noqa: E722
        None
    #ตั้งค่า submitId ใน ContextVar
    submit_id = None
    if 'submitId' in list(request.query_params.keys()) :
        submit_id = request.query_params['submitId']
    else :
        submit_id = generate_random_string()
        
    set_submit_id("-submitId-"+submit_id+"-path-"+request.url.path)
    
    logger.debug(f"New request: {request.method} {request.url}")
    logger.debug(f"body : {body_str}")

    response = await call_next(request)
    
    return response

def generate_random_string(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

app.include_router(example_router, prefix="/api")

THREAD_CLEAR_CHAT = ThreadClearChat()
def check_user():
    while True :
        try :
            THREAD_CLEAR_CHAT.check_user()
        except:  # noqa: E722
            None
        time.sleep(APPLICATION_CONFIG['start_check_expire'])
        logger.debug("Check user")

if __name__ == "__main__":
    task_thread = threading.Thread(target=check_user)
    task_thread.daemon = True  # ทำให้ thread ปิดเมื่อโปรแกรมหลักปิด
    task_thread.start()
    if APPLICATION_CONFIG['environment'] == 'local': # enable auto-reload
        uvicorn.run("main:app", host=APPLICATION_CONFIG['host'], port=APPLICATION_CONFIG['port'],workers=1,log_level="info",reload=True)
    else :
        uvicorn.run(app, host=APPLICATION_CONFIG['host'], port=APPLICATION_CONFIG['port'])