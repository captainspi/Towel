from abc import ABC, abstractmethod
from typing import Optional
from src.Utils.Token.Tokens import Tokens


class Tokenizer(ABC):
    """The Tokenizer abstract class"""

    MAP_TO_ROMAN_NUMERAL_PATTERN = "MapToRomanNumeralPattern"
    INITIALIZE_CURRENCY_RATE_PATTERN = "InitializeCurrencyRatePattern"
    CONVERT_TO_ARABIC_NUMERAL_PATTERN = "ConvertToArabicNumeralPattern"
    CONVERT_MONEY_PATTERN = "ConvertMoneyPattern"
    INVALID_PATTERN = "InvalidPattern"

    def tokenize(self, query: str) -> Tokens:
        """Method that resolves the query to a command type"""
        token = self.tokenize_for_map_to_roman_numeral_pattern(query)
        if token:
            return token

        token = self.tokenize_for_initialize_currency_rate_pattern(query)
        if token:
            return token
        token = self.tokenize_for_convert_to_arabic_numeral_pattern(query)
        if token:
            return token
        token = self.tokenize_for_convert_money_pattern(query)
        if token:
            return token

        return self.tokenize_for_invalid_pattern(query)

    @abstractmethod
    def tokenize_for_map_to_roman_numeral_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for mapping to roman numeral pattern"""
        pass

    @abstractmethod
    def tokenize_for_initialize_currency_rate_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for initialize currency rate pattern"""
        pass

    @abstractmethod
    def tokenize_for_convert_to_arabic_numeral_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for convert to arabic numeral pattern"""
        pass

    @abstractmethod
    def tokenize_for_convert_money_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for initialize currency rate commands"""
        pass

    @abstractmethod
    def tokenize_for_invalid_pattern(self, query: str) -> Tokens:
        """Attempts to tokenize values for initialize currency rate commands"""
        pass
