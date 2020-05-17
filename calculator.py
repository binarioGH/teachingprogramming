#-*-coding: utf-8-*-

'''
Cheat sheet

input -> ask the user for data

if -> ask the computer to compare values:
	== equal than
	!= different than
	> bigger than
	>= bigger or equal than
	< smaller than
	<= smaller or equal than

'''



#Ask the user for two numbers

do = ""

while do != "exit":
	number1 = int(input("Introduce a number: ")) 
	number2 = int(input("Introduce another number: "))

	do = input("What do you want to do? ")

	if do == "multiply":
		result = number1 * number2

	elif do == "divide":
		result = number1 / number2

	elif do == "add":
		result = number1 + number2

	elif do == "subtract":
		result = number1 - number2
	else:
		if do != "exit":
			print("That is not an option")
		else:
			print("Goodbye")
		exit()


	print("The result is {}".format(result))