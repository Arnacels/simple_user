import datetime
from typing import Any

from common.bases import BaseRepository
from common.exceptions import RepositoryException
from .schemas import User, UpdateUser, InsertUser


class UserRepository(BaseRepository):
    _table_name = 'user'
    _EMAIL_FIELD: str = 'email'
    _PK_FIELD: str = 'pk'

    def update_one(self, *, pk: int, user_in: UpdateUser) -> User:
        self.fetch_one(pk=pk)
        self._is_uniq_email(user_in.email)
        for key, value in user_in.dict():
            self._db[pk][key] = value
        return self.fetch_one(pk=pk)

    def insert(self, *, user_in: InsertUser) -> User:
        self._is_uniq_email(user_in.email)
        pk = self._get_nex_pk()
        self._db[pk] = User(pk=pk,
                            create_on=datetime.datetime.now(),
                            **user_in.dict()).dict()
        return self._db[pk]

    def delete(self, *, pk: int) -> None:
        self.fetch_one(pk=pk)
        self._db.pop(pk)

    def delete_by_email(self, *, email: str):
        found_users = self._fetch_by_field(self._EMAIL_FIELD, email)
        for user in found_users:
            self._db.pop(user.get(self._PK_FIELD))

    def _is_uniq_email(self, email: str):
        in_stock = self._fetch_by_field(self._EMAIL_FIELD, email)
        if in_stock:
            raise RepositoryException(f'User with {email} exists')
        return not in_stock

    def _fetch_by_field(self, field: str, value: Any):
        return list(
            filter(lambda obj: obj[field] == value, self._db.values())
        )
