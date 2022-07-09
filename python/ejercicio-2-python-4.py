numero_inicial = 2
numero_final = 8
resultado = []
i = numero_inicial

while ( i <= numero_final ):
    if ( (i % 2) != 0 ):
        resultado.append(i)
    i += 1
if (len(resultado) != 0):
    print(resultado)
else:
    print("Nada que mostar")

