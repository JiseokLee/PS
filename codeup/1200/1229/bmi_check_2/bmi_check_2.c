#include <stdio.h>

int main(void)
{
    double height, weight;
    double stdWeight = 0;
    double bmi = 0;

    scanf("%lf %lf", &height, &weight);

    if (height < 150)
    {
        stdWeight = height - 100;
    }
    else if (height < 160)
    {
        stdWeight = (height - 150) / 2 + 50;
    }
    else
    {
        stdWeight = (height - 100) * 0.9;
    }

    bmi = (weight - stdWeight) * 100 / stdWeight;

    if (bmi <= 10)
    {
        printf("����\n");
    }
    else if (bmi <= 20)
    {
        printf("��ü��\n");
    }
    else
    {
        printf("��\n");
    }

    return 0;
}