hardcode_code = 4321

while(1):
	input_code = input("Podaj kod do sejfu: ")
	try:
		input_code = int(input_code)
	except ValueError:
		print('Incorrect value')
		continue

	if input_code == hardcode_code:
		print("Correct Value")
		print('Sejf otwarty')
		break
	else:
		print('Incorect value')
