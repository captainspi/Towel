from src.Numerals.Mapper.Exception import InvalidNumeralMappingException


class RomanToArabicValueMapper:
    """Maps a Roman Numeral to its Arabic Value"""

    def __init__(self):
        """Constructor"""
        self.__map = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

    def map_numeral(self, numeral: str) -> str:
        """Maps a Roman Numeral to its Arabic Value"""
        if numeral in self.__map:
            return self.__map[numeral]

        raise InvalidNumeralMappingException(numeral)
