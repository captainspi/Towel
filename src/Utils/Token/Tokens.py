class Tokens:
    """"Contains a bunch of tokens"""
    def __init__(self, pattern_type: str, numerals: list = [], mapped_from_numeral: str = "", mapped_to_numeral: str = "", value: float = None, currency: str = ""):
        """"Constructor"""
        self.__pattern_type = pattern_type
        self.__currency = currency
        self.__numerals = numerals
        self.__mapped_from_numeral = mapped_from_numeral
        self.__mapped_to_numeral = mapped_to_numeral
        self.__value = value

    def get_pattern_type(self) -> str:
        """Returns value"""
        return self.__pattern_type

    def get_numerals(self) -> list:
        """Returns value"""
        return self.__numerals

    def get_mapped_from_numeral(self) -> str:
        """Returns value"""
        return self.__mapped_from_numeral

    def get_mapped_to_numeral(self) -> str:
        """Returns value"""
        return self.__mapped_to_numeral

    def get_value(self) -> float:
        """Returns value"""
        return self.__value

    def get_currency(self) -> str:
        return self.__currency
