from unittest import TestCase
from src.Numerals.Bank.Bank import Bank
from src.Numerals.Bank.Money.Money import Money


class TestBank(TestCase):
    """"Tests the Bank"""

    def test_convert_silver_to_credit(self):
        """Tests the method that converts monetary values from Type A to type B"""
        # Set up
        """ We are using a real object here even though its not the SUT. Defying the mockist approach ;) """
        stubbed_amount = 5
        stubbed_exchange_rate = 50
        fake_intergalactic_money = Money(stubbed_amount, 'Silver')
        bank = Bank()
        bank.add_rate('Silver', 'Credit', stubbed_exchange_rate)

        # Exercise
        converted_money = bank.convert_to('Credit', fake_intergalactic_money)

        # Verify
        # mock_money_map.map.assert_has_calls(expected_get_last_numeral_calls)
        self.assertEqual(converted_money.get_amount(), stubbed_exchange_rate * stubbed_amount)
        self.assertEqual(converted_money.get_currency(), 'CREDIT')
