from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr


class InsertUser(BaseUser):
    pass


class UpdateUser(BaseUser):
    pass


class User(BaseUser):
    pk: Optional[int]
    create_on: Optional[datetime]
