from utils.db import db
from .exceptions import RepositoryException
from .interfaces import RepositoryInterface


class BaseRepository(RepositoryInterface):
    _table_name: str

    def __init__(self):
        if not db.get(self._table_name):
            db[self._table_name] = {}
        self._db = db[self._table_name]

    @classmethod
    def build(cls):
        return cls()

    def fetch_all(self):
        return list(self._db.values())

    def fetch_one(self, *, pk: int):
        try:
            obj = self._db[pk]
        except KeyError:
            raise RepositoryException(f'Not found obj with pk {pk}')
        return obj

    def _get_nex_pk(self):
        items = list(self._db.keys())
        if not items:
            return 0
        last_id_number = items[-1]
        return last_id_number + 1
