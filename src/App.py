from optparse import OptionParser

from src.Bank.Bank import Bank
from src.Bank.Money.Money import Money
from src.Numerals.Bag.RomanNumeralsBag import RomanNumeralsBag
from src.Numerals.Mapper.Mapper import Mapper
from src.Numerals.Mapper.RomanToArabicValueMapper import RomanToArabicValueMapper
from src.Numerals.RomanToArabicValueConverter import RomanToArabicValueConverter
from src.Utils.Token.RegexTokenizer import RegexTokenizer

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()

filename = "sample_logs"
if options.filename:
    filename = options.filename

with open('./assets/logs/' + filename) as fp:
    tokenizer = RegexTokenizer()
    mapper = Mapper()
    bank = Bank()
    for line in fp:
        tokens = tokenizer.tokenize(line)
        if tokens.get_pattern_type() == RegexTokenizer.MAP_TO_ROMAN_NUMERAL_PATTERN:
            mapper.map_numeral(tokens.get_mapped_from_numeral(), tokens.get_mapped_to_numeral())
        elif tokens.get_pattern_type() == RegexTokenizer.INITIALIZE_CURRENCY_RATE_PATTERN:
            to_currency = 'credits'
            from_currency = tokens.get_currency()
            rhs_arabic_value = tokens.get_value()
            roman_numeral_bag = RomanNumeralsBag()
            for integalactic_numerals in tokens.get_numerals():
                roman_numeral_bag.append_numeral(mapper.get_mapped_numeral(integalactic_numerals))
            lhs_arabic_value = RomanToArabicValueConverter(roman_numeral_bag, RomanToArabicValueMapper()).convert()
            exchange_rate = rhs_arabic_value / lhs_arabic_value
            bank.add_rate(from_currency, to_currency, exchange_rate)
        elif tokens.get_pattern_type() == RegexTokenizer.CONVERT_TO_ARABIC_NUMERAL_PATTERN:
            roman_numeral_bag = RomanNumeralsBag()
            for integalactic_numerals in tokens.get_numerals():
                roman_numeral_bag.append_numeral(mapper.get_mapped_numeral(integalactic_numerals))
            arabic_value = RomanToArabicValueConverter(roman_numeral_bag, RomanToArabicValueMapper()).convert()
            print(int(arabic_value))
        elif tokens.get_pattern_type() == RegexTokenizer.CONVERT_MONEY_PATTERN:
            roman_numeral_bag = RomanNumeralsBag()
            for integalactic_numerals in tokens.get_numerals():
                roman_numeral_bag.append_numeral(mapper.get_mapped_numeral(integalactic_numerals))
            arabic_value = RomanToArabicValueConverter(roman_numeral_bag, RomanToArabicValueMapper()).convert()
            money = Money(arabic_value, tokens.get_currency())
            money = bank.convert_to("credits", money)
            print(int(money.get_amount()))
