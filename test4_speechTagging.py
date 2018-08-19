import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#state_union get the speech text of president in different years
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

#use the 2005 to train the tokenizer, note the tokenizer is pretrained already
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
#then, use trained tokenizer to tokenize sample text
tokenized = custom_sent_tokenizer.tokenize(sample_text)

##for x in range(0,5):
##    print()
##    print(tokenized[x])

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))

process_content()
