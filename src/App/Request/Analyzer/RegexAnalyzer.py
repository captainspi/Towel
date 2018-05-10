import re
from typing import Match, Optional


class RegexAnalyzer:
    """The Regex implementation for an Analyzer"""

    MAP_TO_ROMAN_NUMERAL_PATTERN= "MapToRomanNumeralPattern"
    INITIALIZE_CURRENCY_RATE_PATTERN = "InitializeCurrencyRatePattern"
    CONVERT_TO_ARABIC_NUMERAL_PATTERN= "ConvertToArabicNumeralPattern"
    CONVERT_MONEY_PATTERN = "ConvertMoneyPattern"
    INVALID_PATTERN = "InvalidPattern"

    def resolve_pattern_type(self, query: str) -> str:
        """Method that resolves the query to a command type"""
        if self.tokenize_for_map_to_roman_numeral_pattern(query):
            return self.MAP_TO_ROMAN_NUMERAL_PATTERN
        elif self.tokenize_for_initialize_currency_rate_pattern(query):
            return self.INITIALIZE_CURRENCY_RATE_PATTERN
        elif self.tokenize_for_convert_to_arabic_numeral_pattern(query):
            return self.CONVERT_TO_ARABIC_NUMERAL_PATTERN
        elif self.tokenize_for_convert_money_pattern(query):
            return self.CONVERT_MONEY_PATTERN
        else:
            return self.INVALID_PATTERN


    def tokenize_for_map_to_roman_numeral_pattern(self, query: str) -> Optional[Match]:
        """Attempts to tokenize values for mapping to roman numeral pattern"""
        map_to_roman_numeral_pattern = "([^ ]+) is ([^ ]+)"
        return re.match(map_to_roman_numeral_pattern, query)

    def tokenize_for_initialize_currency_rate_pattern(self, query: str) -> Optional[Match]:
        """Attempts to tokenize values for initialize currency rate pattern"""
        initialize_currency_rate_pattern = "(.*) ([A-Z][a-z]+) is (\d+) Credits"
        return re.match(initialize_currency_rate_pattern, query)

    def tokenize_for_convert_to_arabic_numeral_pattern(self, query: str) -> Optional[Match]:
        """Attempts to tokenize values for convert to arabic numeral pattern"""
        convert_to_arabic_numeral_pattern = "how much is (.*)\?"
        return re.match(convert_to_arabic_numeral_pattern, query)

    def tokenize_for_convert_money_pattern(self, query: str) -> Optional[Match]:
        """Attempts to tokenize values for initialize currency rate commands"""
        convert_money_pattern = "how many Credits is (.*) ([A-Z].*) \?"
        return re.match(convert_money_pattern, query)
