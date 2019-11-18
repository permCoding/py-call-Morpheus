f = open("number.txt","r")
lines = f.readlines()
f.close()

digits  = {
	'********': '0',
	' *** * *': '1',
	'** ** **': '2',
	'** * ***': '3',
	'**** * *': '4',
	'***  ***': '5',
	' ** ****': '6',
	'** ** * ': '7',
	'**  ****': '8',
	'**** ** ': '9'
}

result = ''
for pos in range(len(lines[0])//2):
	digit = ''
	for j in range(4):
		digit += lines[j][pos*2:pos*2+2]
	result += digits[digit]
print(result)
