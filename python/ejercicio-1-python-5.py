import math

def triangulo(base, altura):
   area = (base * altura) / 2
   return(area)
    
def circulo(radio):
	area = round(math.pi * (radio ** 2), 2)
	return (area)

print(triangulo(2,3))
print(circulo(3))
