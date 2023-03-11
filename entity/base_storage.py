from entity.exceptions import NotEnoughSpaceError, NotEnoughProductError, \
    UnknownProductError
from entity.abstract_storage import AbstractStorage
from typing import Dict


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, title: str, amount: int) -> None:
        """ Увеличивает количество товара """
        if self.get_free_space() <= amount:
            raise NotEnoughSpaceError
        if title in self.__items:
            self.__items[title] += amount
        else:
            self.__items[title] = amount

    def remove(self, title, amount) -> None:
        """ Уменьшает количество товара """
        if title not in self.__items:
            raise UnknownProductError
        if self.__items[title] < amount:
            raise NotEnoughProductError
        self.__items[title] -= amount
        if self.__items[title] == 0:
            self.__items.pop(title)

    def get_free_space(self) -> int:
        """ Возвращает количество свободного места """
        return self.__capacity - sum(self.__items.values())

    @property
    def get_items(self):
        """
        Возвращает словарь - {товар: количество}
        """
        return self.__items

    def get_unique_items_count(self) -> int:
        """
        :return: количество уникальных товаров
        """
        count = len(self.__items)
        return count


