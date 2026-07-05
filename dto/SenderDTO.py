from pydantic import BaseModel

class SenderDTO(BaseModel):
    subject: str
    message: str
    email: str