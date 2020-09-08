def verify_valid_input(input_text,input_choices):
	while input_text not in input_choices:
		print("Invalid category: Please enter either of the following choices:")
		for choice in input_choices:
			print(choice)
		continue		

root_word=input('Enter the root word: ')
category=input("Enter the category of the word: 'n' for noun and 'v' for verb: ")
verify_valid_input(category,['n','v'])

if category=='n':
	count=input("Should the word to be generated be singular or plural? Enter 'sg' for singular and 'pr' for plural.")
	verify_valid_input(count,['sg','pr'])
	if count=='sg':
		print(root_word)
	else:
		print(root_word+'s')
else:
	count=input("Enter the tense of the word. Enter 'pr' for present,'pa' and 'f' for future.")
	verify_valid_input(count,['pr','pa','f'])
	if count=='pr':
		print(root_word+'ing')
	elif count=='pa':
		print(root_word+'ed')
	else:
		print('Will '+root_word)