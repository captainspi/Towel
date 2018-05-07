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
        self.__validate_repetitions(numeral_sequence)
        if self.__errors:
            raise RomanNumeralsValidatorException(self.__errors)

        return True

    def __validate_set(self, numeral_sequence: str):
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        disallowed_roman_numerals_pattern = '[^IVXLCDM]'
        disallowed_roman_numerals_error = re.search(disallowed_roman_numerals_pattern, numeral_sequence)
        if disallowed_roman_numerals_error:
            self.__errors.append(Error(Error.INVALID_NUMERAL, numeral_sequence))

    def __validate_subtraction(self, numeral_sequence: str):
        """"Verifies if the order of numerals for subtraction is correct"""
        vld_disallowed_subtractions_pattern = 'V[X|L|C|D|M]|L[C|D|M]|DM'
        vld_subtraction_error = re.search(vld_disallowed_subtractions_pattern, numeral_sequence)
        if vld_subtraction_error:
            self.__errors.append(Error(Error.INVALID_SUBTRACTION_VLD, numeral_sequence))

        ix_disallowed_subtractions_pattern = 'X[DM]|I[^VX]'
        ix_subtractions_error = re.search(ix_disallowed_subtractions_pattern, numeral_sequence)
        if ix_subtractions_error:
            self.__errors.append(Error(Error.INVALID_SUBTRACTION_IX, numeral_sequence))

    def __validate_repetitions(self, numeral_sequence: str):
        """Verifies if the numeral belongs to a list of valid roman numeral types"""
        dlv_disallowed_repetitions_pattern = 'D{2,}|L{2,}|V{2,}'
        dlv_repetition_error = re.search(dlv_disallowed_repetitions_pattern, numeral_sequence)
        if dlv_repetition_error:
            self.__errors.append(Error(Error.INVALID_REPETITION_D_L_V, numeral_sequence))

        ixcm_disallowed_four_in_a_row_pattern = 'I{4,}|X{4,}|C{4,}|M{4,}'
        ixcm_disallowed_four_in_a_row_error = re.search(ixcm_disallowed_four_in_a_row_pattern, numeral_sequence)
        if ixcm_disallowed_four_in_a_row_error:
            self.__errors.append(Error(Error.INVALID_REPETITION_FOUR_IN_A_ROW_I_X_C_M, numeral_sequence))

        xcm_disallowed_four_inconsecutive_pattern = 'X{3}VX|C{3}[IVL]C|M{3}[IVXLD]M'
        xcm_disallowed_four_inconsecutive_error = re.search(xcm_disallowed_four_inconsecutive_pattern, numeral_sequence)
        if xcm_disallowed_four_inconsecutive_error:
            self.__errors.append(Error(Error.INVALID_REPETITION_INCONSECUTIVE_IN_A_ROW_X_C_M, numeral_sequence))