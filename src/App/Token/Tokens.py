class Tokens:
    """"Contains a bunch of tokens"""
    def __init__(self, pattern_type: str, numerals: list = [], mapped_numeral: dict = {}, value: float = None, currency: str = ""):
        """"Constructor"""
        self.__pattern_type = pattern_type
        self.__currency = currency
        self.__numerals = numerals
        self.__mapped_numeral = mapped_numeral
        self.__value = value

    def get_pattern_type(self) -> str:
        """Returns value"""
        return self.__pattern_type

    def get_numerals(self) -> list:
        """Returns value"""
        return self.__numerals

    def get_mapped_numeral(self) -> {}:
        """Returns value"""
        return self.__mapped_numeral

    def get_value(self) -> float:
        """Returns value"""
        return self.__value

    def get_currency(self) -> str:
        return self.__currency
