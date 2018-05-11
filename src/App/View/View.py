class View:
    """This is where the view is 'rendered'"""
    def __init__(self, intergalactic_numerals: str, value: int, from_currency: str = None, to_currency : str = None):
        """Constructor"""
        self.__intergalactic_numerals = intergalactic_numerals.title()
        self.__value = value
        self.__from_currency = from_currency.capitalize() if from_currency else from_currency
        self.__to_currency = to_currency.capitalize() if to_currency else to_currency

    def __str__(self):
        """Returns stringified view data"""
        if self.__from_currency and self.__to_currency:
            result = "{} {} is {} {}".format(self.__intergalactic_numerals, self.__from_currency, self.__value, self.__to_currency)
        else:
            result = "{} is {}".format(self.__intergalactic_numerals, self.__value)
        return result
