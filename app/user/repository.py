import datetime
from typing import List, Any

from common.bases import BaseRepository
from common.exceptions import RepositoryException
from utils.db import db
from .schemas import User, UpdateUser, InsertUser


class UserRepository(BaseRepository):
    _EMAIL_FIELD: str = 'email'
    _PK_FIELD: str = 'pk'

    def fetch_all(self) -> List[User]:
        return list(db.values())

    def fetch_one(self, *, pk: int) -> User:
        try:
            obj = db[pk]
        except KeyError:
            raise RepositoryException(f'Not found obj with pk {pk}')
        return obj

    def update_one(self, *, pk: int, user_in: UpdateUser) -> User:
        self.fetch_one(pk=pk)
        self._is_uniq_email(user_in.email)
        for key, value in user_in.dict():
            db[pk][key] = value
        return self.fetch_one(pk=pk)

    def insert(self, *, user_in: InsertUser) -> User:
        self._is_uniq_email(user_in.email)
        pk = self._get_nex_pk()
        db[pk] = User(pk=pk,
                      create_on=datetime.datetime.now(),
                      **user_in.dict()).dict()
        return db[pk]

    def delete(self, *, pk: int) -> None:
        self.fetch_one(pk=pk)
        db.pop(pk)

    def delete_by_email(self, *, email: str):
        found_users = self._fetch_by_field(self._EMAIL_FIELD, email)
        for user in found_users:
            db.pop(user.get(self._PK_FIELD))

    def _is_uniq_email(self, email: str):
        in_stock = self._fetch_by_field(self._EMAIL_FIELD, email)
        if in_stock:
            raise RepositoryException(f'User with {email} exists')
        return not in_stock

    def _fetch_by_field(self, field: str, value: Any):
        return list(
            filter(lambda obj: obj[field] == value, db.values())
        )

    def _get_nex_pk(self):
        items = list(db.keys())
        if not items:
            return 0
        last_id_number = items[-1]
        return last_id_number + 1
