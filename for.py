#-*-coding: utf-8-*-

name = input("Escriba su nombre: ")
vocales = ["a","e","i","o","u"]
contador_de_vocales = 0
for letra in name:
	if letra.lower() in vocales:
		contador_de_vocales += 1

print("En tu nombre hay {} vocales.".format(contador_de_vocales))

