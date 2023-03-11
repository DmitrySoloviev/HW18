from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request
        self.departure: AbstractStorage = storages[self.__request.departure]
        self.destination: AbstractStorage = storages[self.__request.destination]

    def move(self):
        """

        :return: Перемещает товар
        """
        self.departure.remove(title=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из '
        f'{self.__request.departure}')

        print(f'Курьер везет {self.__request.amount} {self.__request.product} '
        f'из {self.__request.departure} в {self.__request.destination}')

        self.destination.add(title=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в '
        f'{self.__request.destination}')

    def cancel(self):
        """

        :return: Отменяет доставку
        """
        self.departure.add(title=self.__request.product, amount=self.__request.amount)
