class Error:
    """Error class for representing basic validation errors of roman numerals"""
    
    NUMERAL_SET = 'each numeral must be one of the following: IVXLCDM'

    def __init__(self, message, value):
        """Create an Error object"""
        self.message = message
        self.value = value

    def __str__(self):
        return "{}. Provided value: {}".format(self.message, self.value)
