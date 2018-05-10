from unittest import TestCase

class TestAnalyzer(TestCase):
    """"Tests the Query Analyzer"""

    def test_resolve_command_type(self):
        """Tests the method that resolves the query to a command type"""
        data_provider = [
            {"sample_query": "glob is I", "resolved_command_type": "MapToRomanNumeral"},
            {"sample_query": "prok is V", "resolved_command_type": "MapToRomanNumeral"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRate"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRate"},
            {"sample_query": "glob glob Silver is 34 Credits", "resolved_command_type": "InitializeCurrencyRate"},
            {"sample_query": "how much is pish tegj glob glob ?", "resolved_command_type": "ConvertToArabicNumeral"},
            {"sample_query": "how many Credits is glob prok Iron ?", "resolved_command_type": "ConvertMoney"},
            {"sample_query": "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?", "resolved_command_type": "InvalidCommand"},
        ]
        for test_number in range(data_provider.__len__()):
            with self.subTest(i=test_number):
                # Set up
                analyzer = new RegexAnalyzer()

                # Exercise
                converted_value = analyzer.resolve_command_type(data_provider[test_number]["sample_query"])

                # Verify
                self.assertEqual(converted_value, data_provider[test_number]["resolved_command_type"])

