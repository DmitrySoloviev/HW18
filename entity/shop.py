from typing import Dict
from entity.exceptions import TooManyDifferentProductsError
from entity.base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int, max_unique_items: int) -> object:
        self.max_unique_items = max_unique_items
        super().__init__(items, capacity)

    def add(self, title: str, amount: int) -> None:
        """
        :return: Добавляет товар
        """

        if self.get_unique_items_count() > self.max_unique_items:
            raise TooManyDifferentProductsError

        super().add(title, amount)
