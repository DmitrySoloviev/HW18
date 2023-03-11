from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def add(self, title: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, title, amount) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @property
    @abstractmethod
    def get_items(self) -> Dict:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass


