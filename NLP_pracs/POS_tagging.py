from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk

#nltk.download('averaged_perceptron_tagger') #one time code.

print('Word Tokenizer')
sentence=input('Enter a sentence: ')
word_tokens=word_tokenize(sentence)
POS_tokens=pos_tag(word_tokens)
print(POS_tokens)
print('\n')

print('Sentence Tokenizer')
text=input('Enter a list of sentences(paragraph):\n')
sentence_tokens=sent_tokenize(text)
for sentence in sentence_tokens:
	tokenized_text=word_tokenize(sentence)
	POS_tagged_list=pos_tag(tokenized_text)
	print('POS Tagged: ',POS_tagged_list)