#filter out unnecessary words in english to speed up possessing, 
#remove stop word won't change the meaninng of sentence
#can make your own stopword list
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing stop word filtration."
stop_words = set(stopwords.words("english"))
print(stop_words);

words = word_tokenize(example_sentence);
filtered_sentence = [];

for w in words:
        if w not in stop_words:
            filtered_sentence.append(w);

print(filtered_sentence)

filtered_sent2 = [w for w in words if not w in stop_words]
print(filtered_sentence)
