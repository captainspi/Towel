from unittest import TestCase
from src.Bank.Bank import Bank
from src.Bank.Exception import ExchangeRateNotFoundException
from src.Bank.Money.Money import Money


class TestBank(TestCase):
    """"Tests the Bank"""

    def test_convert_money(self):
        """Tests the method that converts monetary values from Type A to type B"""
        # Set up
        """ We are using a real object here even though its not the SUT. Defying the mockist approach ;) """
        fake_base_amount = 5
        fake_intergalactic_money = Money(fake_base_amount, 'Silver')
        fake_exchange_rate = 50
        fake_exchange_rate_2 = 100
        bank = Bank()
        bank.add_rate('Silver', 'Credit', fake_exchange_rate)
        bank.add_rate('Silver', 'Euros', fake_exchange_rate_2)

        # Exercise
        converted_money = bank.convert_to('Credit', fake_intergalactic_money)
        converted_money_2 = bank.convert_to('Euros', fake_intergalactic_money)

        # Verify
        self.assertEqual(converted_money.get_amount(), fake_exchange_rate * fake_base_amount)
        self.assertEqual(converted_money.get_currency().capitalize(), 'Credit')

        self.assertEqual(converted_money_2.get_currency().capitalize(), 'Euros')
        self.assertEqual(converted_money_2.get_amount(), fake_exchange_rate_2 * fake_base_amount)

    def test_exception_invalid_conversion(self):
        """Tests the bank for invalid exchange rate"""
        with self.assertRaises(ExchangeRateNotFoundException) as context:
            stubbed_amount = 5
            fake_intergalactic_money = Money(stubbed_amount, 'Silver')
            bank = Bank()
            bank.convert_to('Credit', fake_intergalactic_money)