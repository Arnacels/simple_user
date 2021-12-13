from datetime import datetime

from fastapi import Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from common.interfaces import ServiceInterface
from common.repository.logs import LogRepository
from logs.schemas import InsertLog


class Schema(BaseModel):
    url: str
    body: str


class LogsCreator(ServiceInterface):

    def __init__(
            self,
            request: Request,
            response: StreamingResponse,
    ):
        self._request = request
        self._response = response
        self._repo = LogRepository.build()

    async def execute(self):
        response_schema = await self._get_request()
        log_data = InsertLog(
            request_schema=response_schema.dict(),
            response_schema=self._get_response().dict(),
            date=datetime.now()
        )
        self._repo.insert(obj_in=log_data)

    async def _get_request(self):
        body = await self._request.body()
        return Schema(
            url=str(self._request.url),
            body=body.decode(),
        )

    def _get_response(self):
        return Schema(
            url=str(self._request.url),
            body='',
        )
