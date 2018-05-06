class RomanNumeralsValidatorException(Exception):
    """Validation error class"""

    def __init__(self, errors):
        """Create a ValidationError"""
        self.errors = errors

    def __str__(self):
        result = "Validation errors:\n"
        for error in self.errors:
            result += str(error) + "\n"
        return result
