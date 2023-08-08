from time import sleep

from SendMessage.message import SendMessageBacBo
from settings.access import Access
from settings.urls import UrlsBlaze
from status.State import Overall
from status.status import ResultsCassino, RoboBacBo
from strategy.strategy import (NotPattern, PatternBanker, PatternBankerTwo,
                               PatternPlayer, PatternPlayerTwo)
from utils.results_filter import FilterBacBo
from WebScreaper.browsethepage import (BrowseThePage, ChangeFrameGame,
                                       ChangeResultsFormat, ClickButtonBanker,
                                       ClickButtonChips5, ClickButtonChips10,
                                       ClickButtonChips25, ClickButtonDraw,
                                       ClickButtonPlayer, CloseDialogBox,
                                       CurrentCommander, LoginPlayBlaze,
                                       Refresh)


class BacBoAutomaticPlayer:
    def __init__(self):
        self.list_ids: list[int] = []
        self.init: bool = False
        self.refresh_: int = 0
        self.number_gale: int = 0

        # ===Browser da pagina do Bac-Bo=== #
        self.browser = BrowseThePage(
            UrlsBlaze.URL_BAC_BOB_LAZE,
            Access.USER_NAME,
            Access.PASSWORD,
            'Bac_Bo'
        )

        # ===Botões da pagina do Bac-Bo=== #
        self.login = LoginPlayBlaze(self.browser)
        self.chand_frame = ChangeFrameGame(self.browser)
        self.click_banker = ClickButtonBanker(self.browser)
        self.click_player = ClickButtonPlayer(self.browser)
        self.click_draw = ClickButtonDraw(self.browser)
        self.click_chips_05 = ClickButtonChips5(self.browser)
        self.click_chips_10 = ClickButtonChips10(self.browser)
        self.click_chips_25 = ClickButtonChips25(self.browser)
        self.chand_results_format = ChangeResultsFormat(self.browser)
        self.close_dialog_box = CloseDialogBox(self.browser)
        self.refresh = Refresh(self.browser)

        # ===Commandos para jogar do Bac-Bo=== #
        self.commander = CurrentCommander()
        self.commander.button_add_command('login', self.login)
        self.commander.button_add_command('chand_frame', self.chand_frame)
        self.commander.button_add_command('click_player', self.click_player)
        self.commander.button_add_command('click_banker', self.click_banker)
        self.commander.button_add_command('click_draw', self.click_draw)
        self.commander.button_add_command('clickchips5', self.click_chips_05)
        self.commander.button_add_command('clickchips10', self.click_chips_10)
        self.commander.button_add_command('clickchips25', self.click_chips_25)
        self.commander.button_add_command(
            'closedialogbox',
            self.close_dialog_box
        )
        self.commander.button_add_command(
            'clickresult',
            self.chand_results_format
        )
        self.commander.button_add_command('refresh', self.refresh)
        self.wait_custom(self.commander, 'login')
        self.wait_custom(self.commander, 'chand_frame')
        self.wait_custom(self.commander, 'closedialogbox')
        self.wait_custom(self.commander, 'clickresult')
        self.wait_custom(self.commander, 'clickresult')

        # ===Menssagens para o Telegram=== #
        self.message = SendMessageBacBo()

        # ===Estrategia do bac bo=== #
        self.no_strategy = NotPattern()
        self.strategy_banker_two = PatternBankerTwo(self.no_strategy)
        self.strategy_player_two = PatternPlayerTwo(self.strategy_banker_two)
        self.strategy_banker = PatternBanker(self.strategy_player_two)
        self.strategy_player = PatternPlayer(self.strategy_banker)

        # ===Status do Game=== #
        self._state = Overall()
        self.status = 'Signal_open'
        self.direction = ''

    def wait_custom(self, commander: CurrentCommander, name: str) -> None:
        for count in range(60):
            try:
                commander._execute(name)
                return
            except Exception:
                sleep(1)
                continue

    def check_pattern(self) -> str:
        self.refresh_ += 1
        if self.refresh_ >= 15:
            self.wait_custom(self.commander, 'refresh')
            self.wait_custom(self.commander, 'chand_frame')
            self.wait_custom(self.commander, 'closedialogbox')
            self.wait_custom(self.commander, 'clickresult')
            self.wait_custom(self.commander, 'clickresult')
            self.refresh_ = 0

        if not self.init:
            self.init = not self.init
            return
        if self.status == 'Signal_closed':
            self.correction(self.direction)
            return

        if self.status == 'Correction':
            self.protection(self.direction)
            return

        if self.status == 'protection2':
            self.protection2(self.direction)
            return

        self.direction = self.strategy_player.strategy()
        self.SendSinal(self.direction)
        return

    def correction(self, direction: str) -> None:
        if direction == 'PatternBanker':
            if FilterBacBo().result()[0] == 'b':
                result = self.browser.results_number[-1]
                self._state.winner_one(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                result = self.browser.results_number[-1]
                self._state.winner_tie(result)
                self.status = 'Signal_open'
                return

            self.number_gale = 1
            self.message_id = self.message.SendMessageProtection(
                self.number_gale
            ).message_id
            self.status = 'Correction'
            try:
                self.commander._execute('clickchips10')
                sleep(2)
                self.commander._execute('click_banker')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return

        if direction == 'PatternPlayer':
            if FilterBacBo().result()[0] == 'p':
                result = self.browser.results_number[-1]
                self._state.winner_one(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                result = self.browser.results_number[-1]
                self._state.winner_tie(result)
                self.status = 'Signal_open'
                return

            self.number_gale = 1
            self.message_id = self.message.SendMessageProtection(
                self.number_gale
            ).message_id
            self.status = 'Correction'
            try:
                self.commander._execute('clickchips10')
                sleep(2)
                self.commander._execute('click_player')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return
        return

    def protection(self, direction: str) -> None:

        if self.message_id not in self.list_ids:
            self.list_ids.append(self.message_id)
            self.message.DeleteMessage(self.message_id)

        if direction == 'PatternBanker':
            if FilterBacBo().result()[0] == 'b':
                result = self.browser.results_number[-1]
                self._state.winner_protection(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                result = self.browser.results_number[-1]
                self._state.winner_protection_tie(result)
                self.status = 'Signal_open'
                return

            self.number_gale = 2
            self.message_id = self.message.SendMessageProtection(
                self.number_gale
            ).message_id
            self.status = 'protection2'
            try:
                self.commander._execute('clickchips25')
                sleep(2)
                self.commander._execute('click_player')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return

        if direction == 'PatternPlayer':
            if FilterBacBo().result()[0] == 'p':
                result = self.browser.results_number[-1]
                self._state.winner_protection(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                self.status = 'Signal_open'
                result = self.browser.results_number[-1]
                self._state.winner_protection_tie(result)
                return

            self.number_gale = 2
            self.message_id = self.message.SendMessageProtection(
                self.number_gale
            ).message_id
            self.status = 'protection2'
            try:
                self.commander._execute('clickchips25')
                sleep(2)
                self.commander._execute('click_player')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return
        return

    def protection2(self, direction: str) -> None:
        if self.message_id not in self.list_ids:
            self.list_ids.append(self.message_id)
            self.message.DeleteMessage(self.message_id)

        if direction == 'PatternBanker':
            if FilterBacBo().result()[0] == 'b':
                result = self.browser.results_number[-1]
                self._state.winner_protection(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                result = self.browser.results_number[-1]
                self._state.winner_protection_tie(result)
                self.status = 'Signal_open'
                return

            result = self.browser.results_number[-1]
            self._state.loss(result)
            self.status = 'Signal_open'
            return

        if direction == 'PatternPlayer':
            if FilterBacBo().result()[0] == 'p':
                result = self.browser.results_number[-1]
                self._state.winner_protection(result)
                self.status = 'Signal_open'
                return

            if FilterBacBo().result()[0] == 't':
                self.status = 'Signal_open'
                result = self.browser.results_number[-1]
                self._state.winner_protection_tie(result)
                return

            result = self.browser.results_number[-1]
            self._state.loss(result)
            self.status = 'Signal_open'
            return
        return

    def SendSinal(self, direction: str) -> None:
        if direction == 'PatternBanker':
            self.message.SendMessageSignal('🔴')
            self.status = 'Signal_closed'
            try:
                self.commander._execute('clickchips5')
                sleep(2)
                self.commander._execute('click_banker')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return

        if direction == 'PatternPlayer':
            self.message.SendMessageSignal('🔵')
            self.status = 'Signal_closed'
            try:
                self.commander._execute('clickchips5')
                sleep(2)
                self.commander._execute('click_player')
                self.commander._execute('click_draw')
            except Exception:
                pass
            return
        return


if __name__ == "__main__":
    bac_bo = BacBoAutomaticPlayer()
    time = ResultsCassino()
    results = FilterBacBo()
    control = RoboBacBo(time, bac_bo.check_pattern)
    time.addObserver(control)

    while True:
        time.state = results.get_result()
