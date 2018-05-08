from src.Numerals.Bank.Money.Money import Money


class Bank:
    """Converts Roman Numerals to Arabic Values"""

    def __init__(self):
        """ Bank """
        self.__rates = {}

    def add_rate(self, from_currency: str, to_currency: str, rate: int) -> None:
        """" Adds a rate for a given currency. Rate can only be an int,
        we assume loose change was the weakness of humanity and aliens were too smart to ever want any. """
        self.__rates.update({from_currency.upper(): {to_currency.upper(): rate}})

    def convert_to(self, to_currency: str, money: Money) -> Money:
        converted_money = Money(money.get_amount(), to_currency)
        converted_money.multiply(self.__get_exchange_rate(money.get_currency(), to_currency))
        return converted_money

    def __get_exchange_rate(self, from_currency: str, to_currency: str) -> int:
        """Returns the exchange rate if available"""
        if from_currency.upper() in self.__rates and to_currency.upper() in self.__rates[from_currency]:
            return self.__rates[from_currency.upper()][to_currency.upper()]







