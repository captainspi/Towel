from src.Bank.Exception import ExchangeRateNotFoundException
from src.Bank.Money.Money import Money


class Bank:
    """Converts Roman Numerals to Arabic Values"""

    def __init__(self):
        """ Bank """
        self.__rates = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: float) -> None:
        """" Adds a rate for a given currency."""
        to_rates = {}
        if from_currency.upper() in self.__rates:
            to_rates = self.__rates[from_currency.upper()]

        to_rates.update({to_currency.upper(): rate})
        self.__rates.update({from_currency.upper(): to_rates})

    def convert_to(self, to_currency: str, money: Money) -> Money:
        """Converts the money to the assigned currency"""
        converted_money = Money(money.get_amount(), to_currency)
        converted_money.multiply(self.__get_exchange_rate(money.get_currency(), to_currency))
        return converted_money

    def __get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        """Returns the exchange rate if available"""
        if from_currency.upper() in self.__rates and to_currency.upper() in self.__rates[from_currency]:
            return self.__rates[from_currency.upper()][to_currency.upper()]

        raise ExchangeRateNotFoundException
