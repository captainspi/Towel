import re
from src.Numerals.Validator.Error import Error
from src.Numerals.Validator.Exception import RomanNumeralsValidatorException


class RomanNumeralsValidator:
    """Validates Roman Numerals"""

    def __init__(self):
        """ constructor """
        self.__errors = []

    def validate(self, numeral_sequence: str) -> bool:
        """" Validates roman numerals """
        self.__validate_set(numeral_sequence)
        self.__validate_subtraction(numeral_sequence)
        if self.__errors:
            raise RomanNumeralsValidatorException(self.__errors)

        return True

    def __validate_subtraction(self, numeral_sequence: str):
        """"Verifies if the order of numerals for subtraction is correct"""
        vld_subtractions_pattern = 'V[X|L|C|D|M]|L[C|D|M]|DM'
        vld_subtraction_error = re.search(vld_subtractions_pattern, numeral_sequence)
        if vld_subtraction_error:
            self.__errors.append(Error(Error.INVALID_SUBTRACTION_VLD, numeral_sequence))

        ixc_subtractions_pattern = 'X[DM]|I[^VX]'
        ixc_subtractions_error = re.search(ixc_subtractions_pattern, numeral_sequence)
        if ixc_subtractions_error:
            self.__errors.append(Error(Error.INVALID_SUBTRACTION_IXC, numeral_sequence))

    def __validate_set(self, numeral_sequence: str):
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        allowed_roman_numerals_pattern = '[^IVXLCDM]'
        x = re.search(allowed_roman_numerals_pattern, numeral_sequence)
        if x:
            self.__errors.append(Error(Error.NUMERAL_SET, numeral_sequence))