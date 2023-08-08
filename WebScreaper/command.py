"""
Description...
"""
from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    """
    Descriptions...
    """
    @property
    @abstractmethod
    def commands(self) -> Dict[str, str]: pass


class CommandsBacBoBlaze(Command):
    def __name__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return self.__name__()

    def commands(self) -> Dict[str, str]:
        return {
            'GAME_NAME': 'div.header--1b29e div.tableInfo--e93ee',
            'SUBMIT_BUTTON': 'button.submit',
            'PLAYER_BUTTON': 'div.player--82e25 div.svgResult--d94ae',
            'BANKER_BUTTON': 'div.banker--cc9e5 div.svgResult--d94ae',
            'DRAW_BUTTON': 'div.container--5f978 div.'
            'tie--b0a3f div.svgResult--d94ae',
            'LIST_CHIPS': 'div.chipItem--07039',
            'PLAYER_PERCENT': 'div.statistics--4e1d7 div.playerPart--e3dee',
            'BANKER_PERCENT': 'div.statistics--4e1d7 div.bankerPart--18b1a',
            'DRAW_PERCENT': 'div.statistics--4e1d7 div.tiePart--2e4b1',
            'CLOSE_DIALOG_BOX_BUTTON': 'div.popup--11329 span.label--290ba',
            'AMMONT_BANK': 'span.amount--bb99f',
            'AMMONT_BET': 'div.totalBet--e866e span.amount--56eca',
            'IFRAME 1': 'div#game_wrapper iframe',
            'IFRAME 2': 'div.loader-frame-container iframe',
            'BALANCE_VALUE': 'div.textContainer--8e37d',
            'LIST_NUMBERS': 'svg.beadRoad--1913c'
        }


class CommandsBacBoPokerStars(Command):
    def __name__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return self.__name__()

    def commands(self) -> Dict[str, str]:
        return {
            'GAME_NAME': 'div.header--1b29e div.tableInfo--e93ee',
            'SUBMIT_BUTTON': 'button.submit',
            'PLAYER_BUTTON': 'div.player--82e25 div.svgResult--d94ae',
            'BANKER_BUTTON': 'div.banker--cc9e5 div.svgResult--d94ae',
            'DRAW_BUTTON': 'div.container--5f978 div.'
            'tie--b0a3f div.svgResult--d94ae',
            'LIST_CHIPS': 'div.chipItem--07039',
            'PLAYER_PERCENT': 'div.statistics--4e1d7 div.playerPart--e3dee',
            'BANKER_PERCENT': 'div.statistics--4e1d7 div.bankerPart--18b1a',
            'DRAW_PERCENT': 'div.statistics--4e1d7 div.tiePart--2e4b1',
            'CLOSE_DIALOG_BOX_BUTTON': 'div.restrictedMinWidth--c8d97 button',
            'AMMONT_BANK': 'span.amount--bb99f',
            'AMMONT_BET': 'div.totalBet--e866e span.amount--56eca',
            'IFRAME 1': 'iframe#GameClient',
            'IFRAME 2': 'div.loader-frame-container iframe',
            'BALANCE_VALUE': 'ugc-text#asc_bb_balanceVal',
            'LIST_NUMBERS': 'svg.beadRoad--1913c',
            'BUTTON_ENTRY': 'div._3aae362  button._18f4de1',
        }


class CommandsBrazilianRoulletBlaze(Command):
    def __name__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return self.__name__()

    def commands(self) -> Dict[str, str]:
        return {
            'SUBMIT_BUTTON': 'button.submit',
            'LIST_INDEX_NUMBER_BUTTONS': [
                13, 14, 17, 20, 21, 22, 23, 25, 26, 27, 28, 31,
                32, 35, 36, 38, 42, 43, 44, 45, 47, 48
            ],
            'LIST_OF_BUTTONS': 'div.roulette-game-area'
            '__col_left div.roulette-game-area_'
            '_main-table-wrapper svg.roulette-digital-table-'
            '-pIoRZ g g.table-cell--Wz6uJ',
            'CHIPS': 'div.arrow-slider__scrollable-content svg',
            'IFRAME': 'div#game_wrapper iframe',
            'RESULTS': 'div.roulette-game-area__history-line',
        }


class CommandsCassino(ABC):
    @staticmethod
    @abstractmethod
    def get_commands_bac_bo_blaze() -> CommandsBacBoBlaze: pass

    @staticmethod
    @abstractmethod
    def get_commands_brazilian_roullet_blaze(
    ) -> CommandsBrazilianRoulletBlaze: pass

    @staticmethod
    @abstractmethod
    def get_commands_bac_bo_poker_stars(
    ) -> CommandsBacBoPokerStars: pass


class Cassino(CommandsCassino):
    @staticmethod
    def get_commands_bac_bo_blaze() -> CommandsBacBoBlaze:
        return CommandsBacBoBlaze()

    @staticmethod
    def get_commands_brazilian_roullet_blaze(
    ) -> CommandsBrazilianRoulletBlaze:
        return CommandsBrazilianRoulletBlaze()

    @staticmethod
    def get_commands_bac_bo_poker_stars(
    ) -> CommandsBacBoPokerStars:
        return CommandsBacBoPokerStars()


# if __name__ == "__main__":
#     a = Cassino()
#     b = Cassino()
#     print(a.get_Commands_bac_bo().__repr__())
#     print(b.get_Commands_Brazilian_roullet().__repr__())
