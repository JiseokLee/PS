#include <stdio.h>

int main(void) {
	int year, month, day;
	scanf("%d %d %d", &year, &month, &day);
	
	if((year-month+day) % 10 == 0) {
		printf("���");
	} else {
		printf("�׷�����");
	}
	
	return 0;
}