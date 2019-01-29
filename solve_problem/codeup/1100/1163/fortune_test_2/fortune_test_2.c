#include <stdio.h>

int main(void)
{
    int year, month, day;
    int num;

    scanf("%d %d %d", &year, &month, &day);

    num = (year + month + day) % 1000;
    num = num / 100;

    if (num % 2 == 0)
    {
        printf("대박");
    }
    else
    {
        printf("그럭저럭");
    }

    return 0;
}
