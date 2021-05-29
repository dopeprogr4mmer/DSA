def word_break(word_list, word):
	if word == '':
		return 1
	else:
		wordLen = len(word)
		for i in range(wordLen+1):
			if word[:i] in word_list:
				return word_break(word_list, word[i:])
		return 0



if __name__ == '__main__':
	try:
		word_list = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 
					'cream', 'icecream', 'man', 'go', 'mango']
		#print(word_list)
		word = 'samilikesammango'
		#print(word)
		output = word_break(word_list, word)
		if output:
			print("True")
		else:
			print("False")
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")
