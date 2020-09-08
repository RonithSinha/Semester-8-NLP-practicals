from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
sentence=input('Enter a sentence to be stemmed: ')
word_tokens=word_tokenize(sentence)
for word in word_tokens:
	print(word,': ',stemmer.stem(word))