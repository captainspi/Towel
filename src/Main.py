from optparse import OptionParser

from src.App.App import App
from src.Utils.Factory import UtilsFactory
from src.Utils.Factory import BankFactory
from src.Utils.Factory import NumeralsFactory

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()
filename = "sample_logs"
if options.filename:
    filename = options.filename

"""I really dislike this, 
but short of changing the design of the RomanNumeralsBag and the RomanToArabicValueConverter/having a DI container, 
I don't see how else I can do this."""
app = App(NumeralsFactory().create_mapper(), BankFactory.create_bank(), NumeralsFactory())
tokenizer = UtilsFactory().create_regex_tokenizer()

with open('./assets/logs/' + filename) as fp:
    for line in fp:
        tokens = tokenizer.tokenize(line)
        app.execute(tokens)
