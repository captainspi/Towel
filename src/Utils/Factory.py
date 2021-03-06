from src.Bank.Bank import Bank
from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag
from src.Numerals.Mapper.Mapper import Mapper
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper
from src.Numerals.Validator.RomanNumeralsValidator import RomanNumeralsValidator
from src.Utils.Token.RegexTokenizer import RegexTokenizer


class NumeralsFactory:
    """Factory class for the Numerals"""
    @staticmethod
    def create_mapper() -> Mapper:
        """Factory method for the mapper"""
        return Mapper()

    @staticmethod
    def create_roman_to_arabic_numerals_mapper() -> RomanToArabicValueMapper:
        """Factory method for the roman numerals to arabic mapper"""
        return RomanToArabicValueMapper()

    @staticmethod
    def create_roman_numerals_bag() -> RomanNumeralsBag():
        """Factory method for the RomanNumeralsBag"""
        return RomanNumeralsBag()

    @staticmethod
    def create_roman_numerals_validator() -> RomanNumeralsValidator:
        """Factor method for the roman numerals validator"""
        return RomanNumeralsValidator()


class BankFactory:
    """"Factory class for the Bank"""
    @staticmethod
    def create_bank() -> Bank:
        """Creates the bank"""
        return Bank()


class UtilsFactory:
    """"Factory class for the Tokenizer"""
    @staticmethod
    def create_regex_tokenizer() -> RegexTokenizer:
        """Creates the Tokenizer"""
        return RegexTokenizer()
