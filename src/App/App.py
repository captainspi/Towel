from src.Bank.Bank import Bank
from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag
from src.Numerals.Mapper.Mapper import Mapper
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper
from src.Numerals.RomanToArabicValueConverter import RomanToArabicValueConverter
from src.Utils.Token.RegexTokenizer import RegexTokenizer
from src.Utils.Token.Tokens import Tokens
from src.Bank.Money.Money import Money


class App:
    """This is where all the magic happens!"""
    def __init__(self, mapper: Mapper, bank: Bank):
        """Constructor"""
        self.__mapper = mapper
        self.__bank = bank

    def execute(self, tokens: Tokens):
        """This is where all the magic is orchestrated!"""
        if tokens.get_pattern_type() == RegexTokenizer.MAP_TO_ROMAN_NUMERAL_PATTERN:
            self.__map_intergalactic_numerals_to_roman_numbers(tokens.get_mapped_from_numeral(), tokens.get_mapped_to_numeral())
        elif tokens.get_pattern_type() == RegexTokenizer.INITIALIZE_CURRENCY_RATE_PATTERN:
            self.__calculate_exchange_rate_for_alien_units(tokens.get_currency(), 'credits', tokens.get_numerals(), tokens.get_value())
        elif tokens.get_pattern_type() == RegexTokenizer.CONVERT_TO_ARABIC_NUMERAL_PATTERN:
            arabic_value = self.__calculate_arabic_value(tokens.get_numerals())
            print(int(arabic_value))
        elif tokens.get_pattern_type() == RegexTokenizer.CONVERT_MONEY_PATTERN:
            money = self.__calculate_monetary_value(tokens.get_numerals(), tokens.get_currency())
            print(int(money.get_amount()))

    def __map_intergalactic_numerals_to_roman_numbers(self, map_from: str, map_to: str) -> None:
        """This function maps intergalactic numerals to roman counterparts"""
        self.__mapper.map_numeral(map_from, map_to)

    def __calculate_exchange_rate_for_alien_units(self, from_currency: str, to_currency: str, intergalactic_numerals: list, rhs_value: float) -> None:
        """This functions is responsible for setting the exchange rate at the bank"""
        lhs_arabic_value = self.__calculate_arabic_value(intergalactic_numerals)
        exchange_rate = rhs_value / lhs_arabic_value
        self.__bank.add_rate(from_currency, to_currency, exchange_rate)

    def __calculate_arabic_value(self, intergalactic_numerals: list) -> int:
        """This function calculates the arabic value of intergalactic numerals"""
        roman_numeral_bag = RomanNumeralsBag()
        for intergalactic_numeral in intergalactic_numerals:
            roman_numeral_bag.append_numeral(self.__mapper.get_mapped_numeral(intergalactic_numeral))
        return RomanToArabicValueConverter(roman_numeral_bag, RomanToArabicValueMapper()).convert()

    def __calculate_monetary_value(self, intergalactic_numerals: list, from_currency: str, to_currency: str='credits') -> Money:
        """This function calculates the monetary value of intergalactic numerals"""
        arabic_value = self.__calculate_arabic_value(intergalactic_numerals)
        money = Money(arabic_value, from_currency)
        return self.__bank.convert_to(to_currency, money)
