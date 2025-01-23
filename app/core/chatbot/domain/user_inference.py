from pydantic import BaseModel
class UserInference(BaseModel):
    message: str
    user_id: str
    token: str