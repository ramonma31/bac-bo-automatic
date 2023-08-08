from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from WebScreaper.command import Cassino
from WebScreaper.Generathor import Click

from time import sleep


class BrowseThePage:
    """ Receiver - Navegar-no-site """

    def __init__(
            self,
            url: str,
            user_name: str,
            password: str,
            cassino: str,
    ) -> None:
        if cassino == 'Bac_Bo':
            self.cassino = Cassino().get_commands_bac_bo_blaze()
        elif cassino == 'Brazilian_roullet':
            self.cassino = Cassino().get_commands_brazilian_roullet_blaze()
        elif cassino == 'poker_stars':
            self.cassino = Cassino().get_commands_bac_bo_poker_stars()
        self.url = url
        self.css_selectors = self.cassino
        self.user_name = user_name
        self.password = password
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = Chrome(options=options)
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=3)
        self.condition = EC

    @property
    def ammont_bank(self) -> str:
        return self.driver.find_element(
            "css selector", self.css_selectors.commands()['AMMONT_BANK']
        ).text

    @property
    def results_number(self) -> list[str]:
        locator_numbers = (
            'css selector', self.css_selectors.commands()['LIST_NUMBERS']
        )
        return self.driver.find_element(*locator_numbers).text.split()

    def refresh(self):
        self.driver.refresh()
        return

    def login_play_blaze(self) -> None:
        locator_username = ('name', 'username')
        self.driver.find_element(*locator_username).send_keys(self.user_name)
        locator_password = ('name', 'password')
        self.driver.find_element(*locator_password).send_keys(self.password)
        locator_button = (
            'css selector', self.css_selectors.commands()['SUBMIT_BUTTON']
        )
        self.driver.find_element(*locator_button).click()
        return

    def login_play_poker_stars(self) -> None:
        sleep(2)
        coockie_btn = ('css selector', 'button#onetrust-accept-btn-handler')
        self.driver.find_element(*coockie_btn).click()
        sleep(5)
        locator_play_game = ('css selector', 'div._3aae362  button._18f4de1')
        self.wait.until(EC.visibility_of_element_located(locator_play_game))
        self.driver.find_element(*locator_play_game).click()
        locator_username = ('css selector', 'input#userId')
        self.wait.until(EC.visibility_of_element_located(locator_username))
        self.driver.find_element(*locator_username).send_keys(self.user_name)
        locator_password = ('css selector', 'input#password')
        self.driver.find_element(*locator_password).send_keys(self.password)
        locator_bt = ('css selector', 'div._38fea9f>button._19a2eb7')
        self.wait.until_not(EC.element_attribute_to_include(locator_bt, 'css'))
        self.driver.find_element(
            'css selector', 'div._38fea9f>button._18f4de1'
        ).click()
        sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return

    def change_frame_game(self) -> None:
        if self.css_selectors.__repr__() == 'CommandsBacBoBlaze':
            iframe1 = self.driver.find_element(
                'css selector',
                self.css_selectors.commands()['IFRAME 1']
            )
            self.driver.switch_to.frame(iframe1)
            iframe2 = self.driver.find_element(
                'css selector',
                self.css_selectors.commands()['IFRAME 2']
            )
            self.driver.switch_to.frame(iframe2)
            self.driver.current_window_handle

        elif self.css_selectors.__repr__() == 'CommandsBacBoPokerStars':
            iframe1 = self.driver.find_element(
                'css selector',
                self.css_selectors.commands()['IFRAME 1']
            )
            self.driver.switch_to.frame(iframe1)
            iframe2 = self.driver.find_element(
                'css selector',
                self.css_selectors.commands()['IFRAME 2']
            )
            self.driver.switch_to.frame(iframe2)

        else:
            self.driver.switch_to.frame(
                self.driver.find_element(
                    "css selector",
                    self.css_selectors.commands()['IFRAME']
                )
            )

        return

    def close_dialog_box(self):
        locator_box_dialog = (
            'css selector', 'div.buttonContainer--dc29a  button'
        )
        self.driver.find_element(*locator_box_dialog).click()
        return
        # self.driver.find_elements(
        #     'css selector',
        #     'div.buttonContainer--dc29a  button'
        # )[0].click()

    def change_results_format(self) -> list[str]:
        locator_button = (
            'css selector', self.css_selectors.commands()['LIST_NUMBERS']
        )
        self.driver.find_element(*locator_button).click()
        # self.driver.find_element(
        #     'css selector',
        #     self.css_selectors.commands()['LIST_NUMBERS']
        # ).click()

    def click_button_player(self) -> None:
        self.driver.find_element(
            "css selector",
            self.css_selectors.commands()['PLAYER_BUTTON']
        ).click()

    def click_button_baker(self) -> None:
        self.driver.find_element(
            "css selector",
            self.css_selectors.commands()['BANKER_BUTTON']
        ).click()

    def click_button_draw(self) -> None:
        self.driver.find_element(
            "css selector",
            self.css_selectors.commands()['DRAW_BUTTON']
        ).click()

    def click_chips_5(self) -> None:
        locator = ('css selector', 'div.collapsed--ac77a')
        self.wait.until_not(EC.element_attribute_to_include(locator, 'class'))
        self.driver.find_elements(
            "css selector",
            self.css_selectors.commands()['LIST_CHIPS']
        )[0].click()

    def click_chips_10(self) -> None:
        self.driver.find_elements(
            "css selector",
            self.css_selectors.commands()['LIST_CHIPS']
        )[1].click()

    def click_chips_25(self) -> None:
        self.driver.find_elements(
            "css selector",
            self.css_selectors.commands()['LIST_CHIPS']
        )[2].click()

    def click_buttons_numbers(self) -> None:
        list_of_buttons: List[WebElement] = self.driver.find_elements(
            "css selector",
            self.css_selectors.commands()['LIST_OF_BUTTONS']
        )

        for click in Click.click_event(
            self.css_selectors.commands()['LIST_INDEX_NUMBER_BUTTONS']
        ):
            try:
                list_of_buttons[click].click()
            except Exception:
                print('your balance is insufficient to play')


class ICommand(ABC):
    """ Interface de comando """

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class Refresh(ICommand):
    def __init__(self, browser: BrowseThePage):
        self.browser = browser

    def execute(self) -> None:
        self.browser.refresh()

    def undo(self):
        pass


class LoginPlayBlaze(ICommand):
    def __init__(self, browser: BrowseThePage):
        self.browser = browser

    def execute(self) -> None:
        self.browser.login_play_blaze()

    def undo(self):
        pass


class LoginPlayPokerStars(ICommand):
    def __init__(self, browser: BrowseThePage):
        self.browser = browser

    def execute(self) -> None:
        self.browser.login_play_poker_stars()

    def undo(self):
        pass


class ChangeFrameGame(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.change_frame_game()

    def undo(self) -> None:
        pass


class ClickButtonPlayer(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_button_player()

    def undo(self) -> None:
        pass


class ClickButtonChips5(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_chips_5()

    def undo(self) -> None:
        pass


class ClickButtonChips10(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_chips_10()

    def undo(self) -> None:
        pass


class ClickButtonChips25(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_chips_25()

    def undo(self) -> None:
        pass


class ChangeResultsFormat(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.change_results_format()

    def undo(self):
        pass


class CloseDialogBox(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.close_dialog_box()

    def undo(self):
        pass


class ClickButtonBanker(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_button_baker()

    def undo(self):
        pass


class ClickButtonDraw(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_button_draw()

    def undo(self):
        pass


class ClickButtonNumbers(ICommand):
    def __init__(self, browser: BrowseThePage) -> None:
        self.browser = browser

    def execute(self) -> None:
        self.browser.click_buttons_numbers()

    def undo(self):
        pass


class CurrentCommander:
    """ Invoker """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def _execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def _undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('Nothing to undo')
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == "__main__":
    teste = BrowseThePage(
        'https://www.pokerstars.com/pt-BR/casino/game/live-bac-bo/1002/62',
        'ramonma312',
        'Manu.0512',
        'poker_stars'
    )

    teste.login_play_poker_stars()
