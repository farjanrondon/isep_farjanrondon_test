
while True:

	n = int(input('Número: '))
	sound = ''

	if (n % 3 == 0):
		sound += 'Plic'
		if (n % 5 == 0):
			sound += 'Plac'
			if (n % 7 == 0):
				sound +='Ploc'
		elif (n % 7 == 0):
			sound +='Ploc'

	elif (n % 5 == 0):
		sound += 'Plac'
		if (n % 7 == 0):
			sound +='Ploc'			
				
	elif (n % 7 == 0):
		sound += 'Ploc'

	else:
		print(n)

	print(sound)

	print(' ')
	aux = input("¿Salir? y/n: ")
	if aux == "y":
		break

	print(' ')
