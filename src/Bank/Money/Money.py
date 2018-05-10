class Money:
    """Money object"""

    def __init__(self, amount: float, currency: str):
        """ Money."""
        self.__amount = amount
        self.__currency = currency.upper()

    def add(self, amount: float) -> None:
        """ Adds amount to the money """
        self.__amount = amount + amount

    def multiply(self, multiplier: float) -> None:
        """ Multiplies money by an amount"""
        self.__amount = self.__amount * multiplier

    def get_currency(self) -> str:
        """ Returns the currency """
        return self.__currency

    def get_amount(self) -> float:
        """Returns the amount"""
        return self.__amount







