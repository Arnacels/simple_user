from typing import Any

from common.bases import BaseRepository
from common.exceptions import RepositoryException
from logs.schemas import InsertLog, Log


class LogRepository(BaseRepository):
    _table_name = 'logs'

    def insert(self, obj_in: InsertLog) -> Log:
        pk = self._get_nex_pk()
        self._db[pk] = Log(pk=pk,
                           **obj_in.dict()).dict()
        return self._db[pk]

    def delete(self, pk: Any):
        raise RepositoryException('Cannot delete logs')

    def update_one(self, pk: Any, obj_in):
        raise RepositoryException('Cannot update logs')
