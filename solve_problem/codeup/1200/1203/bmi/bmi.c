#include <stdio.h>

int main()
{
	int bmi;
	scanf("%d", &bmi);
	
	if(bmi <= 10)
		printf("����\n");
	else if(bmi <= 20)
		printf("��ü��\n");
	else
		printf("��\n");
	
	return 0;
}
