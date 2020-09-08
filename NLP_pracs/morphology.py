import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
#The above code needs to be run only once.

sentence=input('Enter a sentence: ')

stemmer=PorterStemmer()
lemmatizer=WordNetLemmatizer()

word_tokens=word_tokenize(sentence)
for word in word_tokens:
	print(f'Word: {word}; Lemmatized word: {lemmatizer.lemmatize(word)}; Stemmed word: {stemmer.stem(word)} ')