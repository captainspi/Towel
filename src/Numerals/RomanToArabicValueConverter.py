from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper


class RomanToArabicValueConverter:
    """Converts Roman Numerals to Arabic Values"""

    def __init__(self, roman_numerals_bag: RomanNumeralsBag, roman_to_arabic_mapper: RomanToArabicValueMapper):
        """ constructor """
        self.__roman_numerals_bag = roman_numerals_bag
        self.__roman_to_arabic_mapper = roman_to_arabic_mapper

    def convert(self) -> int:
        """" Converts the Roman Numerals sequence to its Arabic equivalent """
        total_arabic_value = 0

        roman_numeral = self.__roman_numerals_bag.get_last_numeral()
        while roman_numeral:
            current_arabic_value = self.__map_to_arabic_value(roman_numeral)
            total_arabic_value = self.__sum(current_arabic_value, total_arabic_value)

            roman_numeral = self.__roman_numerals_bag.get_last_numeral()

        return total_arabic_value

    def __map_to_arabic_value(self, roman_numeral: str) -> int:
        """"Reutrns the Arabic value of a roman numeral"""
        return int(self.__roman_to_arabic_mapper.map_numeral(roman_numeral))

    def __sum(self, lhs_value: int, rhs_value: int) -> int:
        """Returns the sum of the lhs and rhs values based on roman calculations"""
        if lhs_value < rhs_value:
            return rhs_value - lhs_value
        else:
            return rhs_value + lhs_value







