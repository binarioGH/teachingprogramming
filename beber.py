#-*-coding: utf-8-*-

edad = int(input("Cual es tu edad? "))

if edad >= 18 and edad < 100:
	print("Si puedes beber.")

elif edad >= 100:
	print("Ya deberias de estar muerto.")

elif edad < 10:
	print("Ni siquiera deberias de preguntar eso.")

else:
	print("No puedes beber.")