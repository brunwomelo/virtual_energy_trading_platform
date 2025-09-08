from pydantic import BaseModel, field_validator, EmailStr, ConfigDict
from uuid import UUID
from typing import ClassVar, Optional
from passlib.context import CryptContext
from enum import Enum

class Role(str, Enum):
    CUSTOMER = "CUSTOMER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"

class UserBase(BaseModel):
    pwd_context: ClassVar = CryptContext(schemes=["bcrypt"], deprecated="auto")
    username: str
    role: Role


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not any(char in "!@#?.,[]" for char in value):
            raise ValueError("Password must contain at least one symbol (!, @, #, ?, ., ,).")
        return cls.pwd_context.hash(value)

class UserUpdate(BaseModel):
    role: Optional[Role] = None
    password: Optional[str] = None

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not any(char in "!@#?.,[]" for char in value):
            raise ValueError("Password must contain at least one symbol (!, @, #, ?, ., ,).")
        return cls.pwd_context.hash(value)

class UserResponse(UserBase):
    id: UUID

    class Config:
        orm_mode = True
