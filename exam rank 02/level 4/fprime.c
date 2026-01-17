#include <stdlib.h>
#include <stdio.h>

int main(int ac, char **av)
{
	int i = 2;
	int num;

	if (ac != 2)
	{
		printf("\n");
		return (0);
	}
	num = atoi(av[1]);
	if (num == 1)
		printf("1");
	while (i <= num)
	{
		if (num % i == 0)
		{
			printf("%d", i);
			if (num != i)
				printf("*");
			num = num / i;
		}
		else
			i++;
	}
	printf("\n");
	return (0);
}