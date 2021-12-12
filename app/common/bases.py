from .interfaces import RepositoryInterface


class BaseRepository(RepositoryInterface):

    @classmethod
    def build(cls):
        return cls()
