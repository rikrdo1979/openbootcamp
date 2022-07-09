#include <stdio.h>

int sum(int a, int b, int c)
{
	int d;
	
	d = a + b + c;
	
	return(d);
}

void main()
{
	int suma;
	int x = 3;
	int y = 2;
	int z = 1;
	
	suma = sum(x, y, z);
	
	/* suma debe ser igual 3 + 2 + 1 = 6 */ 
	printf("La Suma es: %d \n", suma);
} 
