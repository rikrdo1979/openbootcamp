def bisiesto(anio):
	if ((anio % 4 == 0 ) and ( not anio % 100 == 0 or anio % 400 == 0)):
		return ("*** Año Bisiesto ***")
	else:
		return ("| ¯\_(ツ)_/¯ |")

for i in range(1999, 2401):
	print(i, " : " , bisiesto(i))
