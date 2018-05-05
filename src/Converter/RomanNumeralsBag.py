from src.Converter.Exception import Exception as RomanNumeralException

class RomanNumeralsBag:
    """A bag that holds RomanNumerals"""

    def __init__(self):
        """ constructor """
        self.numeralsList = []

    def append_numeral(self, numeral: str) -> None:
        """Appends a numeral to the end of the internal collection"""
        if not self.__is_valid_numeral(numeral):
            raise RomanNumeralException("Numeral is invalid. Numeral: " + numeral)
        self.numeralsList.append(numeral)

    def __is_valid_numeral(self, numeral: str) -> bool:
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        return numeral in allowed_roman_numerals


    def __str__(self) -> str:
        """Returns the stringified version of the internal list of numerals"""
        return ''.join(self.numeralsList)







