#include <stdio.h>

int main(void) {
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	
	if(num1 % 2 == 0) {
		if(num2 % 2 == 0) {
			printf("¦��+¦��=¦��");
		} else {
			printf("¦��+Ȧ��=Ȧ��");
		}
	} else {
		if(num2 % 2 == 0) {
			printf("Ȧ��+¦��=Ȧ��");
		} else {
			printf("Ȧ��+Ȧ��=¦��");
		}
	}
	
	return 0;
}
