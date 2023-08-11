from __future__ import annotations
import requests as api
from settings.urls import UrlsBlaze
from abc import ABC, abstractmethod
from typing import Dict, List


class FilterResults(ABC):
    """CORPO PARA O OBJECT"""
    @abstractmethod
    def get_result(self, url: str) -> Dict[str, str]: None

    @abstractmethod
    def result(self) -> List[str]: None


class FilterBacBo(FilterResults):
    def __init__(self) -> None:
        self.url = UrlsBlaze()

    def get_result(self) -> Dict[str, str]:
        try:
            dict_result = api.get(self.url.URL_BAC_BO_API).json()
            return dict_result
        except Exception:
            print('API indidisponivel tentando reconectar...')
            return {'results': 'error,'}

    def result(self, index: int) -> List[str]:
        try:
            return [x.replace(
                'Player,', 'p'
            ).replace(
                'Banker,', 'b'
            ).replace('Tie,', 't') for x in self.get_result()['results'].split(
            )[0:index]]
        except Exception:
            return ['null', 'null', 'null', 'null']


a = FilterBacBo()
