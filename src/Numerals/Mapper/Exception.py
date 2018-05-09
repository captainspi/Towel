class InvalidNumeralMappingException(Exception):
    """Validation exception class"""

    def __init__(self, value):
        """Create a ValidationError"""
        self.value = value

    def __str__(self):
        return "Undefined mapping attempted. Provided value: {}".format(self.value)
