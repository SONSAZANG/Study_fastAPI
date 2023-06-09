# 사용자 모델
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(Document):
    email: EmailStr                 # email: 사용자 이메일
    password: str                   # password: 사용자 패스워드
    events: Optional[List[Event]]   # events: 해당 사용자가 생성한 이벤트, 처음에는 비어 있다.

    # 샘플 데이터
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
    class Settings:
        name = "users"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str