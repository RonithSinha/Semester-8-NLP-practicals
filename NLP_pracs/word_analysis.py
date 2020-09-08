list_of_words=[
{'word':'boys','root_word':'boy','category':'noun','gender':'male','count':'plural','tense':'none','aspect':'none'},
{'word':'boy','root_word':'boy','category':'noun','gender':'male','count':'singular','tense':'none','aspect':'none'},
{'word':'pens','root_word':'pen','category':'noun','gender':'none','count':'plural','tense':'none','aspect':'none'},
{'word':'saw','root_word':'see','category':'verb','gender':'none','count':'none','tense':'past','aspect':'simple'},
{'word':'watching','root_word':'watch','category':'verb','gender':'none','count':'none','tense':'present','aspect':'present continuous'}
]

input_word=input('Enter the word to be searched: ')
word_found=False
for word_info in list_of_words:
	if word_info['word']==input_word:
		for key,value in word_info.items():
			print(key,': ',value)
		word_found=True
if not word_found:
	print('Word not found.')