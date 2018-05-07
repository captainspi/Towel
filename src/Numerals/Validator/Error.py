class Error:
    """Error class for representing basic validation errors of roman numerals"""

    INVALID_NUMERAL = 'invalid numeral detected. numerals must be one of the following: I V X L C D M'
    INVALID_SUBTRACTION_VLD = 'invalid  subtraction detected. V L and D can never be subtracted'
    INVALID_SUBTRACTION_IX = 'invalid  subtraction detected. X can be subtracted from L or C. I from V or X.'
    INVALID_REPETITION_D_L_V = 'invalid repetition detected. D L V can never be repeated'
    INVALID_REPETITION_FOUR_IN_A_ROW_I_X_C_M = 'invalid repetition detected. Four in a row not allowed for I X C M'
    INVALID_REPETITION_INCONSECUTIVE_IN_A_ROW_X_C_M = 'invalid repetition detected. Four in a row not allowed for I X C M unless separated by a valid smaller number'

    def __init__(self, message, value):
        """Create an Error object"""
        self.message = message
        self.value = value

    def __str__(self):
        return "{}. Provided value: {}".format(self.message, self.value)
