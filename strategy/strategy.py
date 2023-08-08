from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from SendMessage.message import SendMessageBacBo
from strategy.Patterns import (PATERN_BANKER, PATERN_BANKER_SIMPLE,
                               PATERN_BLACK, PATERN_PLAYER,
                               PATERN_PLAYER_SIMPLE, PATERN_RED)
from utils.results_filter import FilterBacBo


class Strategy(ABC):
    def __init__(self) -> None:
        self.successor: Strategy
        self.message: SendMessageBacBo
        self.lock: bool
        self.unlock: bool

    @abstractmethod
    def strategy(self, pattern: List[str]) -> str: pass


class PatternRed(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_RED
        self.successor = successor

    def strategy(self) -> bool:
        pattern = self.result.result()

        if pattern in self.patterns.values():
            # self.bot.send_message(Access.CHAT_ID, 'Apostar Player')
            return
        return self.successor.strategy(pattern)


class PatternBlack(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_BLACK
        self.successor = successor

    def strategy(self, pattern: List[str]) -> bool:
        if pattern in self.patterns.values():
            # self.bot.send_message(Access.CHAT_ID, 'Apostar Banker')
            return
        return self.successor.strategy(pattern)


class PatternPlayer(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_PLAYER
        self.successor = successor
        self.result = FilterBacBo()

    def strategy(self) -> None:
        pattern = self.result.result()
        if pattern in self.patterns.values():
            return f'{self.__class__.__name__}'
        return self.successor.strategy(pattern)


class PatternBanker(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_BANKER
        self.successor = successor
        self.lock = False

    def strategy(self, pattern: List[str]) -> bool:
        if pattern in self.patterns.values():
            return f'{self.__class__.__name__}'
        return self.successor.strategy(pattern)


class PatternPlayerTwo(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_PLAYER_SIMPLE
        self.successor = successor
        self.result = FilterBacBo()

    def strategy(self, pattern: List[str]) -> None:
        if pattern[0:2] in self.patterns.values():
            return f'{self.__class__.__name__}'
        return self.successor.strategy(pattern)


class PatternBankerTwo(Strategy):
    def __init__(self, successor: Strategy) -> None:
        super().__init__()
        self.patterns = PATERN_BANKER
        self.successor = successor
        self.lock = False

    def strategy(self, pattern: List[str]) -> bool:
        if pattern[0:2] in self.patterns.values():
            return f'{self.__class__.__name__}'
        return self.successor.strategy(pattern)


class PatternPlayerSimple(Strategy):
    def __init__(self, successor: Strategy) -> None:
        self.patterns = PATERN_PLAYER_SIMPLE
        self.successor = successor
        self.result = FilterBacBo()

    def strategy(self) -> str:
        pattern = self.result.result()
        if pattern[0] == self.patterns['patterns_1'][0]:
            return 'PatternPlayerSimple'
        return self.successor.strategy(pattern)


class PatternBankerSimple(Strategy):
    def __init__(self, successor: Strategy) -> None:
        self.patterns = PATERN_BANKER_SIMPLE
        self.successor = successor

    def strategy(self, pattern: List[str]) -> str:
        if pattern[0] == self.patterns['patterns_1'][0]:
            return 'PatternBankerSimple'
        return self.successor.strategy(pattern)


class NotPattern(Strategy):
    def strategy(self, pattern: List[str]) -> bool:
        return 'NotPattern'


# if __name__ == '__main__':
#     result1 = ['v', 'p', 'v', 'v']
#     result2 = ['p', 'p', 'v', 'p']
#     result3 = ['v', 'p', 'v', 'v']

#     no_patern = NotPattern()
#     patern_black = PatternBlack(no_patern)
#     patern_red = PatternRed(patern_black)

#     print(patern_red.strategy(result1))
#     print(patern_red.strategy(result2))
#     print(patern_red.strategy(result3))
