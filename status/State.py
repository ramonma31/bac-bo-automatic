from __future__ import annotations

from abc import ABC, abstractmethod

from SendMessage.message import SendMessageBacBo
from utils.PercentageStrategy import CustomPercent, ValuePersentage


class Overall:
    ''' Context '''
    def __init__(self) -> None:
        self.state: InfoBotState = OverallResults(self)
        self.all_winner: int = 0
        self.one_winner: int = 0
        self.protection_winner: int = 0
        self.tie_winner: int = 0
        self.lose: int = 0
        self.consecutive_winner: int = 0
        self.all_entry: int = 0
        self.message = SendMessageBacBo()

    def winner_one(self, result: str) -> None:
        self.state.one_winner()
        self.message.SendMessageWinner()
        self.message.SendMessageOverallRessults(
            result,
            self.all_winner, self.protection_winner,
            self.one_winner, self.tie_winner,
            self.lose, self.consecutive_winner,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.protection_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.one_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.all_winner
                )
            ).total_percent_value

        )
        return

    def winner_protection(self, result: str) -> None:
        self.state.protection_winner()
        self.message.SendMessageWinner()
        self.message.SendMessageOverallRessults(
            result,
            self.all_winner, self.protection_winner,
            self.one_winner, self.tie_winner,
            self.lose, self.consecutive_winner,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.protection_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.one_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.all_winner
                )
            ).total_percent_value

        )
        return

    def winner_tie(self, result: str) -> None:
        self.state.tie_winner()
        self.message.SendMessageWinner(result, True)
        self.message.SendMessageOverallRessults(
            result,
            self.all_winner, self.protection_winner,
            self.one_winner, self.tie_winner,
            self.lose, self.consecutive_winner,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.protection_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.one_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.all_winner
                )
            ).total_percent_value

        )
        return

    def winner_protection_tie(self, result: str) -> None:
        self.state.tie_protection_winner()
        self.message.SendMessageWinner(result, True)
        self.message.SendMessageOverallRessults(
            result,
            self.all_winner, self.protection_winner,
            self.one_winner, self.tie_winner,
            self.lose, self.consecutive_winner,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.protection_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.one_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.all_winner
                )
            ).total_percent_value

        )
        return

    def loss(self, result: str) -> None:
        self.state.lose()
        self.message.SendMessageLose()
        self.message.SendMessageOverallRessults(
            result,
            self.all_winner, self.protection_winner,
            self.one_winner, self.tie_winner,
            self.lose, self.consecutive_winner,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.protection_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.one_winner
                )
            ).total_percent_value,
            ValuePersentage(
                self.all_entry, CustomPercent(
                    self.all_winner
                )
            ).total_percent_value

        )
        return


class InfoBotState(ABC):
    def __init__(self, state: Overall) -> None:
        self.overall = state

    @abstractmethod
    def one_winner(self) -> None: pass

    @abstractmethod
    def protection_winner(self) -> None: pass

    @abstractmethod
    def tie_winner(self) -> None: pass

    @abstractmethod
    def tie_protection_winner(self) -> None: pass

    @abstractmethod
    def lose(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class OverallResults(InfoBotState):
    def one_winner(self) -> None:
        self.overall.all_winner += 1
        self.overall.all_entry += 1
        self.overall.one_winner += 1
        self.overall.consecutive_winner += 1
        return

    def protection_winner(self) -> None:
        self.overall.all_winner += 1
        self.overall.all_entry += 1
        self.overall.protection_winner += 1
        self.overall.consecutive_winner += 1
        return

    def tie_winner(self) -> None:
        self.overall.all_winner += 1
        self.overall.all_entry += 1
        self.overall.tie_winner += 1
        self.overall.consecutive_winner += 1
        return

    def tie_protection_winner(self) -> None:
        self.overall.all_winner += 1
        self.overall.all_entry += 1
        self.overall.tie_winner += 1
        self.overall.consecutive_winner += 1
        return

    def lose(self) -> None:
        self.overall.all_entry += 1
        self.overall.lose += 1
        self.overall.consecutive_winner = 0
        return
