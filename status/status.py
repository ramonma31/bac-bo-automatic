from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self):
        return self._state

    @abstractmethod
    def addObserver(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observer(self) -> None: pass


class ResultsCassino(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observer()

    def reset_state(self):
        self._state = {}

    def addObserver(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class RoboBacBo(IObserver):
    def __init__(self, observable: IObservable, method) -> None:
        self.observable = observable
        self.method = method

    def update(self) -> None:
        self.method()


class RoboRoletaBrasileira(IObserver):
    def __init__(self, observable: IObservable, method) -> None:
        self.observable = observable
        self.method = method

    def update(self) -> None:
        self.method()


# if __name__ == "__main__":
#     import requests
#     results = ResultsCassino()

#     def mostrar():
#         print('deucerto')

#     status_bot = RoboBacBo(results, mostrar)

#     results.addObserver(status_bot)

#     while True:
#         resultados = requests.get(
#             'https://api.scrapingcasinos.com/Evolution/Rodadas/BacBo00000000001.txt'
#         ).json()

#         results.state = resultados
