def keypad_sequence(string):
	keypad = ['skip','1',['skip','A','B','C'],['skip','D','E','F'],['skip','G','H','I'],['skip','J','K','L'],['skip','M','N','O'],['skip','P','Q','R','S'],['skip','T','U','V'],['skip','W','X','Y','Z'],'*','0','#']
	string_sequence = ''
	for letter in string:
		n = 0
		if letter == ' ':
			string_sequence+='0'
		for key in keypad:
			if letter in key:
				for i in range(key.index(letter)):
					string_sequence+=str(keypad.index(key))

	return string_sequence



keypad_sequence('GEEKS FOR GEEKS')