from __future__ import annotations

from abc import ABC, abstractmethod

from telebot import TeleBot
from telebot.types import Message

from SendMessage.templates import TemplatesBacBo
from settings.access import Access


class SendMessage(ABC):
    def __init__(self) -> None:
        self.access: Access = Access()
        self.bot_telegram: TeleBot = TeleBot(self.access.TOKEN)

    @abstractmethod
    def SendMessageInit(self) -> None: pass

    @abstractmethod
    def SendMessageWinner(self) -> None: pass

    @abstractmethod
    def SendMessageLose(self) -> None: pass

    @abstractmethod
    def SendMessageSignal(self, sinal: str) -> None: pass

    @abstractmethod
    def SendMessageAlertSinal(self) -> None: pass

    @abstractmethod
    def SendMessageOverallRessults(
        self,
        winners: int,
        winners_gale: int,
        tiers: int,
        loses: int,
        consecutive: int,
        percent_to_gale: float,
        percent_not_gale: float,
        percent_overall: float,
    ) -> None: pass

    @abstractmethod
    def SendMessageProtection(self) -> None: pass

    @abstractmethod
    def DeleteMessage(self) -> None: pass


class SendMessageBacBo(SendMessage):
    def SendMessageInit(self) -> Message:
        return self.bot_telegram.send_message(
            self.access.CHAT_ID,
            TemplatesBacBo.INIT
        )

    def SendMessageWinner(self, result: str | None = None, tier: bool = False) -> Message:
        if tier:
            self.bot_telegram.send_sticker(
                self.access.CHAT_ID,
                TemplatesBacBo.STIKER_TIE
            )
            return self.bot_telegram.send_message(
                self.access.CHAT_ID,
                f'{TemplatesBacBo.TIER} {result}'
            )

        self.bot_telegram.send_sticker(
            self.access.CHAT_ID,
            TemplatesBacBo.STIKER_WINNER
        )

    def SendMessageLose(self) -> Message:
        return self.bot_telegram.send_sticker(
            self.access.CHAT_ID,
            TemplatesBacBo.STIKER_LOSE
        )

    def SendMessageSignal(self, signal: str) -> Message:
        return self.bot_telegram.send_message(
            self.access.CHAT_ID,
            f'''
{TemplatesBacBo.SIGNAL_PT_1}

{TemplatesBacBo.SIGNAL_PT_2} {signal}
{TemplatesBacBo.SIGNAL_PT_3}'''
        )

    def SendMessageOverallRessults(
        self,
        last_result: str,
        winners: int,
        winners_gale: int,
        winners_not_gale: int,
        tiers: int,
        loses: int,
        consecutive: int,
        percent_to_gale: float,
        percent_not_gale: float,
        percent_overall: float,    
    ) -> Message:
        return self.bot_telegram.send_message(
            self.access.CHAT_ID,
            f'''{TemplatesBacBo.OVERALL_RESULTS_PT_1} {TemplatesBacBo.OVERALL_RESULTS_WINNER}{winners} | {TemplatesBacBo.OVERALL_RESULTS_TIE}{tiers} | {TemplatesBacBo.OVERALL_RESULTS_LOSE}{loses}
{TemplatesBacBo.OVERALL_LAST_RESULT} {last_result}
{TemplatesBacBo.OVERALL_RESULTS_PT_2} {winners_not_gale}
{TemplatesBacBo.OVERALL_RESULTS_PT_3} {winners_gale}
{TemplatesBacBo.OVERALL_RESULTS_PT_4} {tiers}
{TemplatesBacBo.OVERALL_RESULTS_PT_5} {consecutive}
{TemplatesBacBo.OVERALL_RESULTS_PT_6} {percent_overall:.2f}%
{TemplatesBacBo.OVERALL_RESULTS_PT_7} {percent_to_gale:.2f}%
{TemplatesBacBo.OVERALL_RESULTS_PT_8} {percent_not_gale:.2f}%
'''
        )

    def SendMessageAlertSinal(self) -> Message:
        return self.bot_telegram.send_message(
            self.access.CHAT_ID,
            TemplatesBacBo.ALERT_SIGNAL
        )

    def SendMessageProtection(self, gale: int) -> Message:
        return self.bot_telegram.send_message(
            self.access.CHAT_ID,
            f'{TemplatesBacBo.ALERT_PROTECTION} {gale}'
        )

    def DeleteMessage(self, message_id: int) -> None:
        return self.bot_telegram.delete_message(
                self.access.CHAT_ID,
                message_id
        )
