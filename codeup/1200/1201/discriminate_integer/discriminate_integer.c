#include <stdio.h>

int main(void)
{
    int num;

    scanf("%d", &num);

    if (num > 0)
        printf("���\n");
    else if (num < 0)
        printf("����\n");
    else
        printf("0\n");
}