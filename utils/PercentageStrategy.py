from __future__ import annotations
from abc import ABC, abstractmethod


class ValuePersentage:
    def __init__(self, total: float, percentage: CalculatePercentage):
        self._total = total
        self._percentage = percentage

    @property
    def total(self):
        return self._total

    @property
    def total_value_percent(self):
        return self._percentage.value_percent(self.total)

    @property
    def total_acreditate_percent(self):
        return self._percentage.value_percent_acreditate(self.total)

    @property
    def total_percent_value(self):
        return self._percentage.percent_value(self.total)


class CalculatePercentage(ABC):
    @abstractmethod
    def value_percent(self, total: float) -> float: pass

    @abstractmethod
    def value_percent_acreditate(self, total: float) -> float: pass

    @abstractmethod
    def percent_value(self, total: float) -> float: pass


class FivePercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 5 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 5 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 5 * 100 / total
        except ZeroDivisionError:
            return 0


class TenPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 10 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 10 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 10 * 100 / total
        except ZeroDivisionError:
            return 0


class FifteenPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 15 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 15 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 15 * 100 / total
        except ZeroDivisionError:
            return 0


class TwentyPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 20 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 20 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 20 * 100 / total
        except ZeroDivisionError:
            return 0


class TwentyFivePercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 25 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 25 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 25 * 100 / total
        except ZeroDivisionError:
            return 0


class ThirtyPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 30 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 30 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 30 * 100 / total
        except ZeroDivisionError:
            return 0


class ThirtyFivePercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 35 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 35 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 35 * 100 / total
        except ZeroDivisionError:
            return 0


class FortyPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 40 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 40 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 40 * 100 / total
        except ZeroDivisionError:
            return 0


class FortyFivePercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 45 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(self, total: float) -> float:
        try:
            return 45 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 45 * 100 / total
        except ZeroDivisionError:
            return 0


class FiftyPercent(CalculatePercentage):

    def value_percent(self, total: float) -> float:
        try:
            return 50 * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(
            self, total: float) -> float:
        try:
            return 50 * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return 50 * 100 / total
        except ZeroDivisionError:
            return 0


class CustomPercent(CalculatePercentage):
    def __init__(self, value) -> None:
        self.value = value

    def value_percent(self, total: float) -> float:
        try:
            return self.value * total / 100
        except ZeroDivisionError:
            return 0

    def value_percent_acreditate(
            self, total: float) -> float:
        try:
            return self.value * total / 100 + total
        except ZeroDivisionError:
            return 0

    def percent_value(self, total: float) -> float:
        try:
            return self.value * 100 / total
        except ZeroDivisionError:
            return 0

# if __name__ == "__main__":
#     cinco_porcento = FivePercent()
#     dez_porcento = TenPercent()
#     quinze_porcento = FifteenPercent()
#     vinte_porcento = TwentyPercent()
#     vinte_e_cinco_porcento = TwentyFivePercent()
#     trinta_porcento = ThirtyPercent()
#     trinta_e_cinco_porcento = ThirtyFivePercent()
#     quarenta_porcento = FortyPercent()
#     quarenta_e_cinco_porcento = FortyFivePercent()
#     cinquenta_porcento = FiftyPercent()

#     parar = ValuePersentage(total=500, percentage=cinco_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=dez_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=quinze_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=vinte_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=vinte_e_cinco_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=trinta_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=trinta_e_cinco_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=quarenta_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=quarenta_e_cinco_porcento)
#     print(parar.total, parar.total_acreditate_percent)

#     parar = ValuePersentage(total=500, percentage=cinquenta_porcento)
#     print(parar.total, parar.total_acreditate_percent)

    # parar = ValuePersentage(total=500, percentage=CustomPercent(16))
    # print(parar.total, parar.total_acreditate_percent)
