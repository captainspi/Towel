from src.Numerals.Mapper.Exception import InvalidNumeralMappingException


class Mapper:
    map = {}

    def get_mapped_numeral(self, numeral: str) -> str:
        """Maps a Roman Numeral to its Arabic Value"""
        if numeral in self.map:
            return self.map[numeral.upper()]

        raise InvalidNumeralMappingException(numeral)

    def map_numeral(self, from_numeral: str, to_numeral: str):
        """Maps numerals"""
        self.map.update({from_numeral.upper(): to_numeral.upper()})