from typing import Dict

from entity.courier import Courier
from entity.exceptions import BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from entity.abstract_storage import AbstractStorage

store = Store(
    items={
        "товар_1": 40,
        "печеньки": 40,
        "товар_3": 10,
        "товар_4": 4,
    },
    capacity=100)

shop = Shop(
    items={
        "товар_1": 5,
        "товар_2": 10,
    },
    capacity=20,
    max_unique_items=10
)

storages: Dict[str, AbstractStorage] = {
    "склад": store,
    "магазин": shop
}


def main():
    while True:
        print("new")
        for s_name, storage in storages.items():
            print(f"В {s_name} храниться: {storage.get_items}")

        raw_request = input(
            "Введите запрос, или введите 'стоп' чтобы закончить"
        )
        if raw_request in 'стоп':
            break

        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cancel()



if __name__ == '__main__':
    main()
