#different form of words have same meaning, use stemmer to save memory in database
#can make your own stemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for w in example:
    print(ps.stem(w))





new_example = "it is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"

word = word_tokenize(new_example)

for w in word:
    print(ps.stem(w))
