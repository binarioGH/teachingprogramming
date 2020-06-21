#-*-coding: utf-8-*-

myText = input("Write something: ")

counter = 0

for letter in myText:
	counter += 1

print("There are {} characters in '{}'".format(counter, myText))