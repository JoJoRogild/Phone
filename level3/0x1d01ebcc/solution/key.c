#include <stdio.h>


int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("usage: %s <username>\n", argv[0]);
		return 1;
	}

	int i;
	int sum = 0;

	for (i = 0; argv[1][i]; i++)
		sum += argv[1][i];
	
	sum &= 0x3f;

	sum += 11;

	/*
	 * Valid keys must have a cross sum equal to sum.
	 * Lets just generate a short and simple one.
	 */

	printf("key: ");
	
	for (i = 0; i + 9 <= sum; i += 9)
		printf("9");
	
	if (sum > i)
		printf("%i", sum-i);
	
	printf("\n");
	
	return 0;
}
