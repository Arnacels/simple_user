from pydantic import BaseModel


class DefaultDeleteResponse(BaseModel):
    detail: str = 'success'
