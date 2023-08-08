from typing import Any
from selenium.webdriver.remote.webdriver import WebDriver


class WaitCustom:
    def __init__(self, locator) -> None:
        self.locator = locator

    def __call__(self, webdriver: WebDriver):
        if webdriver.find_element(*self.locator):
            return True
        return False
