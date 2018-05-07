class Error:
    """Error class for representing basic validation errors of roman numerals"""
    
    NUMERAL_SET = 'each numeral must be one of the following: IVXLCDM'
    INVALID_SUBTRACTION_VLD = 'invalid numeral subtraction detected. V L and D can never be subtracted'
    INVALID_SUBTRACTION_IXC = 'invalid numeral subtraction detected. C can be extracted from D or M. X from L or C. I from V or X.'

    def __init__(self, message, value):
        """Create an Error object"""
        self.message = message
        self.value = value

    def __str__(self):
        return "{}. Provided value: {}".format(self.message, self.value)
