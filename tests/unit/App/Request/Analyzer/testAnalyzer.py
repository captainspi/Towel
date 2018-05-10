from unittest import TestCase
from src.App.Request.Analyzer.RegexAnalyzer import RegexAnalyzer


class TestAnalyzer(TestCase):
    """"Tests the Query Analyzer"""

    def test_resolve_command_type(self):
        """Tests the method that resolves the query to a command type"""
        data_provider = [
            {"sample_query": "glob is I", "resolved_command_type": "MapToRomanNumeralPattern"},
            {"sample_query": "prok is V", "resolved_command_type": "MapToRomanNumeralPattern"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRatePattern"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRatePattern"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRatePattern"},
            {"sample_query": "how much is pish tegj glob glob ?", "resolved_command_type": "ConvertToArabicNumeralPattern"},
            {"sample_query": "how many Credits is glob prok Iron ?", "resolved_command_type": "ConvertMoneyPattern"},
            {"sample_query": "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?", "resolved_command_type": "InvalidPattern"},
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                analyzer = RegexAnalyzer()

                # Exercise
                pattern_type = analyzer.resolve_pattern_type(data_provider[test_number]["sample_query"])

                # Verify
                self.assertEqual(pattern_type, data_provider[test_number]["resolved_command_type"])

