f = open("number.txt","r") # файл с шифрованным номером

sfr = f.read().split('\n')

tab = []

for i in range(len(sfr)):
	tab.append([])

for i in range(len(sfr)):
	for k in range(0,len(sfr[i]),2):
		tab[i].append(sfr[i][k] + sfr[i][k+1]) # запись данных из файла по 2 символам в ячейку

end = []

for i in range(len(tab[0])):
	end.append(tab[0][i] +  tab[1][i] + tab[2][i] + tab[3][i])
	#запись данных по 4 символа в ячейку( выделение каждой зашифрованный цифры)

key  = [
	'********',
	' *** * *',
	'** ** **',
	'** * ***',
	'**** * *',
	'***  ***',
	' ** ****',
	'** ** * ',
	'**  ****',
	'**** ** '
] # ключи для поиска чисел в  шифрованном файле(записаны в одну строку)

for i in range(len(end)):
	for k in range(len(key)): #поиск ключей в файле
		if end[i] == key[k]:
			print(k, end = '') #расшифрованный номер