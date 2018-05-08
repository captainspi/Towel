from unittest import TestCase

class TestBank(TestCase):
    """"Tests the Bank"""

    def testConvert(self):
        """Tests the method that converts monetary values from Type A to type B"""
        # Set up
        """ We are using a real object here even though its not the SUT. Defying the mockist approach ;) """
        fake_intergalactic_money = Money(5, 'Silver')
        bank = SimpletonBank()
        bank.addRate('Silver', 'Credit', 50)

        # Exercise
        converted_money = bank.convertTo('Credit', fake_intergalactic_money)

        # Verify
        # mock_money_map.map.assert_has_calls(expected_get_last_numeral_calls)
        self.assertEqual(converted_money, 50)
