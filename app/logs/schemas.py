from datetime import datetime

from pydantic import BaseModel


class InsertLog(BaseModel):
    request_schema: dict
    response_schema: dict
    date: datetime


class Log(InsertLog):
    pk: int
