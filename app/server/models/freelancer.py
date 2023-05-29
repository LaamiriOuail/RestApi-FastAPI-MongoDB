from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class FreelanceSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    country: str = Field(...)
    phone: str = Field(...)
    description: str = Field(...)
    avatar_path: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources and environmental engineering",
                "country": "Morocco",
                "phone": "4.0",
                "description": "HAAAAAAAAAAAAAAAAA",
                "avatar_path": "..."
            }
        }

class UpdateFreelanceSchema(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    phone: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    avatar_path: Optional[str] 
    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources and environmental engineering",
                "country": "Morroco",
                "phone": "4.0",
                "description":"HAAAAAAAAAAAAAAAAA",
                "avatar_path": "Morroco",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}