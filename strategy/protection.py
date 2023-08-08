from __future__ import annotations
from abc import ABC, abstractmethod
from utils.results_filter import FilterBacBo
from SendMessage.message import SendMessageBacBo


class Martingale(ABC):
    def __init__(self) -> None:
        self.results = FilterBacBo()
        self.message = SendMessageBacBo()

    @abstractmethod
    def is_signal(self) -> None: pass

    @abstractmethod
    def correct(self) -> None: pass


class MartingaleBacBoPlayer(Martingale):
    def __init__(self) -> None:
        super().__init__()
        self.backup_id: list[int] = []

    def is_signal(self, control: bool) -> bool:
        if control:
            return self.correct(control)
        return

    def correct(self, control: bool) -> bool:
        # return self.message.SendMessageLose()

        if self.results.result()[0] != 'b':
            if self.id_message not in self.backup_id:
                self.backup_id.append(self.id_message)
                self.message.DeleteMessage(self.id_message)
            self.message.SendMessageWinner()
            control = False
            return control

        self.id_message = self.message.SendMessageProtection(
            self.protection
        ).message_id
        return control


class MartingaleBacBoBanker(Martingale):
    def __init__(self) -> None:
        super().__init__()
        self.backup_id: list[int] = []

    def is_signal(self, control: bool) -> None:
        if control:
            self.correct(control)
        return False

    def correct(self, control: bool) -> None:

        if self.results.result()[0] != 'p':
            if self.id_message not in self.backup_id:
                self.backup_id.append(self.id_message)
                self.message.DeleteMessage(self.id_message)
            self.message.SendMessageWinner()
            control = False
            return control

        self.protection += 1
        self.id_message = self.message.SendMessageProtection(
            self.protection
        ).message_id
        return control
