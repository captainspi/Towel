from src.Numerals.Bag.Exception import RomanNumeralsBagException
from typing import Optional


class RomanNumeralsBag:
    """A bag that holds RomanNumerals"""

    def __init__(self):
        """ constructor """
        self.__numerals_list = []

    def append_numeral(self, numeral: str) -> None:
        """Appends a numeral to the end of the internal collection"""
        if not self.__is_valid_numeral(numeral.capitalize()):
            raise RomanNumeralsBagException("Numeral is invalid. Numeral: " + numeral)
        self.__numerals_list.append(numeral.capitalize())

    def get_last_numeral(self) -> Optional[str]:
        """Returns the last numeral or false"""
        if not self.__numerals_list:
            return None
        return self.__numerals_list.pop()

    def __is_valid_numeral(self, numeral: str) -> bool:
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return numeral in allowed_roman_numerals

    def __str__(self) -> str:
        """Returns the stringified version of the internal list of numerals"""
        return ''.join(self.__numerals_list)







