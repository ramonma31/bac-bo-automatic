# from abc import ABC, abstractmethod
from typing import List


class Click:
    def click_event(lista: List[int]):
        for itm in lista:
            yield itm
