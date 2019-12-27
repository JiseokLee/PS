#include <stdio.h>

int main(void)
{
	int i;
	int size;
	int input;
	int result[24] = { 0, };

	scanf("%d", &size);

	for(i=0; i<size; i++) {
		scanf("%d", &input);
		result[input]++;
	}

	for(i=1; i<=23; i++) {
		printf("%d ", result[i]);
	}

	printf("\n");

	return 0;
}
