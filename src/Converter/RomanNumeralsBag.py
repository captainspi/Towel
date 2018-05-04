class RomanNumeralsBag:
    """A bag that holds RomanNumerals"""

    def __init__(self):
        """ constructor """
        self.numeralsList = []

    def append(self, numeral: str) -> None:
        """appends a numeral to the end of the internal collection"""
        self.numeralsList.append(numeral)

    def __str__(self) -> str:
        """Returns the stringified version of the internal list of numerals"""
        return ''.join(self.numeralsList)







