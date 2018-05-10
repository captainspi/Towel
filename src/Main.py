from optparse import OptionParser
from src.App.App import App
from src.Bank.Bank import Bank
from src.Numerals.Mapper.Mapper import Mapper
from src.Utils.Token.RegexTokenizer import RegexTokenizer

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()
filename = "sample_logs"
if options.filename:
    filename = options.filename

app = App(Mapper(), Bank())
tokenizer = RegexTokenizer()

with open('./assets/logs/' + filename) as fp:
    for line in fp:
        tokens = tokenizer.tokenize(line)
        app.execute(tokens)
