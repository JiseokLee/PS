#include <stdio.h>

int main()
{
	int bmi;
	scanf("%d", &bmi);
	
	if(bmi <= 10)
		printf("정상\n");
	else if(bmi <= 20)
		printf("과체중\n");
	else
		printf("비만\n");
	
	return 0;
}
