from typing import List

from fastapi import Depends, APIRouter

from logs import schemas
from common.repository.logs import LogRepository

router = APIRouter()


@router.get('/')
def logs_all(
        *,
        repository: LogRepository = Depends(LogRepository.build),
) -> List[schemas.Log]:
    """
    List of logs
    """
    return repository.fetch_all()
