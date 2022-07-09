def es_primo(numero):
	i = 1
	flag = 0
	if numero == 1:
		return (1)
	if numero == 0:
		return (0)
	while (i <= numero):
		if ((numero % i) == 0):
			flag += 1
		if flag > 2:
			return (0)
		i += 1
	return (1)

for i in range(0, 20):
	if es_primo(i) == 1:
		print('***', i, ': Es un Número Primo ***')
	else:
		print(i, ': No es un Número Primo')
  
