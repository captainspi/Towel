from optparse import OptionParser

from src.App.App import App
from src.Utils.Factory import UtilsFactory
from src.Utils.Factory import BankFactory
from src.Utils.Factory import NumeralsFactory

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="filename where the transaction logs are stored", metavar="FILE")
(options, args) = parser.parse_args()
filename = "sample_logs"
if options.filename:
    filename = options.filename

"""I really dislike passing the numerals factory like this. 
but short of changing the design of the RomanNumeralsBag and the RomanToArabicValueConverter/having a DI container, this is probably the simplest fix (okay is a hack)"""
app = App(NumeralsFactory().create_mapper(), BankFactory.create_bank(), NumeralsFactory())
tokenizer = UtilsFactory().create_regex_tokenizer()

with open('./assets/logs/' + filename) as fp:
    for line in fp:
        tokens = tokenizer.tokenize(line)
        app.execute(tokens)
