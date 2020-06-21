#-*-coding: utf-8-*-

operation = ""


while operation != "exit":
	print("Choose from the following operations: addition, subtraction, multiplication, division.")
	operation = input("What operation will you use?")
	operations = ("addition", "subtraction", "multiplication", "division")

	if operation in operations:

		num_1 = int(input("What is your first number?"))
		num_2 = int(input("What is your second number?"))
		
		if operation == "addition":
			result = num_1 + num_2


		elif operation == "subtraction":
			result = num_1 - num_2
		

		elif operation == "multiplication":
			result = num_1 * num_2


		elif operation == "division":
			result = num_1 / num_2	



		print(result)

	else:
		print("That operation is not in the list.")


