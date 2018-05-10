from unittest import TestCase
from src.Utils.Token.RegexTokenizer import RegexTokenizer


class TestRegexTokenizer(TestCase):
    """"Tests the Query Token"""

    def test_resolve_command_type(self):
        """Tests the method that resolves the query to a command type"""
        data_provider = [
            {"sample_query": "glob is I", "resolved_command_type": "MapToRomanNumeralPattern", "expected_mapped_numerals": {"from_numeral": "GLOB", "to_numeral": "I"},
             "expectedNumerals": [], "expectedCurrency": "", "expectedValue": None},
            {"sample_query": "prok is V", "resolved_command_type": "MapToRomanNumeralPattern", "expected_mapped_numerals": {"from_numeral": "PROK", "to_numeral": "V"},
             "expectedNumerals": [], "expectedCurrency": "", "expectedValue": None},
            {"sample_query": "glob prok Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRatePattern", "expected_mapped_numerals": {}, "expectedNumerals": ["GLOB", "PROK"],
             "expectedCurrency": "SILVER", "expectedValue": 34.00},
            {"sample_query": "how much is pish tegj glob glob ?", "resolved_command_type": "ConvertToArabicNumeralPattern", "expected_mapped_numerals": {}, "expectedNumerals": ["PISH", "TEGJ","GLOB", "GLOB"],
             "expectedCurrency": "", "expectedValue": None},
            {"sample_query": "how many Credits is glob prok Iron ?", "resolved_command_type": "ConvertMoneyPattern", "expected_mapped_numerals": {}, "expectedNumerals": ["GLOB", "PROK"],
             "expectedCurrency": "IRON", "expectedValue": None},
            {"sample_query": "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?", "resolved_command_type": "InvalidPattern", "expected_mapped_numerals": {}, "expectedNumerals": [],
             "expectedCurrency": "", "expectedValue": None},
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                tokenizer = RegexTokenizer()

                # Exercise
                tokens = tokenizer.tokenize(data_provider[test_number]["sample_query"])

                # Verify
                self.assertEqual(tokens.get_pattern_type(), data_provider[test_number]["resolved_command_type"])
                self.assertEqual(tokens.get_mapped_numeral(), data_provider[test_number]["expected_mapped_numerals"])
                self.assertEqual(tokens.get_numerals(), data_provider[test_number]["expectedNumerals"])
                self.assertEqual(tokens.get_currency(), data_provider[test_number]["expectedCurrency"])
                self.assertEqual(tokens.get_value(), data_provider[test_number]["expectedValue"])
