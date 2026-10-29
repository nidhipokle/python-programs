
from nltk.stem import PorterStemmer

ps = PorterStemmer()

print(ps.stem("eating"))
print(ps.stem("running"))
print(ps.stem("agreed"))
print(ps.stem("agreeing"))
