import math
def binary_strings(string, count, output=[]):
		#return output
	if '?' in string:
		x = string.replace('?','1',1)
		y = string.replace('?','0',1)
		binary_strings(x, count, output)
		binary_strings(y, count, output)
	else:
		#print(string)
		output.append(string)
		
	if len(output) == count:
		return output

def binary_strings_alternative(string, i, output =[]):
	if i == len(string):
		#print('d')
		output.append("".join(string)) 
		#print(output)
		return output
	if string[i] == '?':
		string[i] = '1'
		binary_strings_alternative(string, i+1, output)
		string[i] = '0'
		binary_strings_alternative(string, i+1, output)
		string[i]='?'
	else:
		binary_strings_alternative(string, i+1, output)
		
	return output
	


if __name__ == '__main__':
	try:
		string = "1??0?101"
		#count = int(math.pow(2,string.count('?')))
		#print(count)
		#output = binary_strings(string, count, [])
		string = list(string)
		output = binary_strings_alternative(string, 0, [])
		if output!=[]:
			for bstring in output:
				print(bstring)
		else:
			print("No such string found!")
	except Exception:
		errorno = 50159747054
		print(f"Hey Phantom, there's a {errorno: #x} error")
