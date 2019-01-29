#include <stdio.h>

int main(void) {
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	
	if(num1 % 2 == 0) {
		if(num2 % 2 == 0) {
			printf("Â¦¼ö+Â¦¼ö=Â¦¼ö");
		} else {
			printf("Â¦¼ö+È¦¼ö=È¦¼ö");
		}
	} else {
		if(num2 % 2 == 0) {
			printf("È¦¼ö+Â¦¼ö=È¦¼ö");
		} else {
			printf("È¦¼ö+È¦¼ö=Â¦¼ö");
		}
	}
	
	return 0;
}
