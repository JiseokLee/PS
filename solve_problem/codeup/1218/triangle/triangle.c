#include <stdio.h>

int main(void)
{
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    if (a + b > c)
    {
        if (a == b && b == c)
        {
            printf("Á¤»ï°¢Çü\n");
        }
        else if (a * a + b * b == c * c)
        {
            printf("Á÷°¢»ï°¢Çü\n");
        }
        else if (a == b || a == c || b == c)
        {
            printf("ÀÌµîº¯»ï°¢Çü\n");
        }
        else
        {
            printf("»ï°¢Çü\n");
        }
    }
    else
    {
        printf("»ï°¢Çü¾Æ´Ô\n");
    }

    return 0;
}