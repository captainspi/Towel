import re
from typing import Optional
from src.Utils.Token.Tokens import Tokens
from src.Utils.Token.Tokenizer import Tokenizer


class RegexTokenizer(Tokenizer):
    """The Regex implementation of a Tokenizer"""

    def tokenize_for_map_to_roman_numeral_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for mapping to roman numeral pattern"""
        map_to_roman_numeral_pattern = "([^ ]+) is ([^ ]+)"
        match = re.match(map_to_roman_numeral_pattern, query)
        if match:
            from_numeral = match.group(1).strip().upper()
            to_numeral = match.group(2).strip().upper()
            return Tokens(self.MAP_TO_ROMAN_NUMERAL_PATTERN, mapped_numeral={"from_numeral": from_numeral, "to_numeral": to_numeral})

        return None

    def tokenize_for_initialize_currency_rate_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for initialize currency rate pattern"""
        initialize_currency_rate_pattern = "(.*) ([A-Z][a-z]+) is (\d+) Credits"
        match = re.match(initialize_currency_rate_pattern, query)
        if match:
            currency = match.group(2).strip().upper()
            value = float(match.group(3))

            numerals = match.group(1).strip().split(" ")
            for i in range(0, len(numerals)):
                numerals[i] = numerals[i].strip().upper()

            return Tokens(self.INITIALIZE_CURRENCY_RATE_PATTERN, currency=currency, value=value, numerals=numerals)

        return None

    def tokenize_for_convert_to_arabic_numeral_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for convert to arabic numeral pattern"""
        convert_to_arabic_numeral_pattern = "how much is (.*)\?"
        match = re.match(convert_to_arabic_numeral_pattern, query)
        if match:
            numerals = match.group(1).strip().split(" ")
            for i in range(0, len(numerals)):
                numerals[i] = numerals[i].strip().upper()

            return Tokens(self.CONVERT_TO_ARABIC_NUMERAL_PATTERN, numerals=numerals)

        return None

    def tokenize_for_convert_money_pattern(self, query: str) -> Optional[Tokens]:
        """Attempts to tokenize values for initialize currency rate commands"""
        convert_money_pattern = "how many Credits is (.*) ([A-Z].*) \?"
        match = re.match(convert_money_pattern, query)
        if match:
            currency = match.group(2).strip().upper()
            numerals = match.group(1).strip().split(" ")
            for i in range(0, len(numerals)):
                numerals[i] = numerals[i].strip().upper()

            return Tokens(self.CONVERT_MONEY_PATTERN, numerals=numerals, currency=currency)

    def tokenize_for_invalid_pattern(self, query: str) -> Tokens:
        """Attempts to tokenize values for initialize currency rate commands"""
        return Tokens(self.INVALID_PATTERN)
