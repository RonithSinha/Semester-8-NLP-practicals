#import nltk
#nltk.download('stopwords')
#nltk.download('punkt') 
#The above code needs to be run only once.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence=input('Enter the sentence from which stop words are to be removed: ')
stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(sentence)

filtered_sentence=[]
for word in word_tokens:
	if word not in stop_words:
		filtered_sentence.append(word+' ')
filtered_sentence=''.join(filtered_sentence)
print(filtered_sentence)