#! /bin/python3.6
a = int(input('Qual a tabuada que você quer: '))
for i in range(1, 11):
	print(f'{a} X {i} = \033[31m {a*i}\033[m')

