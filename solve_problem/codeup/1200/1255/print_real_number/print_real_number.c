#include <stdio.h>

int main(void)
{
    double num1, num2;
    double i;

    scanf("%lf %lf", &num1, &num2);

    for (i = num1; i <= num2; i += 0.01)
        printf("%.2lf ", i);

    return 0;
}