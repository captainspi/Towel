from optparse import OptionParser
from src.Utils.Token.RegexTokenizer import RegexTokenizer

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()

filename = "sample_logs"
if options.filename:
    filename = options.filename

with open('./assets/logs/' + filename) as fp:
    tokenizer = RegexTokenizer()
    for line in fp:
        tokens = tokenizer.tokenize(line)
        print(tokens.get_pattern_type())
