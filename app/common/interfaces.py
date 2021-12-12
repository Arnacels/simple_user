from abc import ABC, abstractmethod
from typing import Any


class ServiceInterface(ABC):

    @abstractmethod
    def execute(self):
        pass


class PresenterInterface(ABC):

    @abstractmethod
    def present(self):
        pass


class RepositoryInterface(ABC):

    @abstractmethod
    def fetch_all(self):
        pass

    @abstractmethod
    def fetch_one(self, pk: Any):
        pass

    @abstractmethod
    def insert(self, obj_in):
        pass

    @abstractmethod
    def delete(self, pk: Any):
        pass

    @abstractmethod
    def update_one(self, pk: Any, obj_in):
        pass

