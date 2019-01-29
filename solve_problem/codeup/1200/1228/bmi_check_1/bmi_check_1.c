#include <stdio.h>

int main(void)
{
    double height;
    double weight;
    double stdWeight = 0;
    double bmi = 0;

    scanf("%lf %lf", &height, &weight);

    stdWeight = (height - 100) * 0.9;
    bmi = (weight - stdWeight) * 100 / stdWeight;

    if (bmi <= 10)
    {
        printf("정상\n");
    }
    else if (bmi <= 20)
    {
        printf("과체중\n");
    }
    else
    {
        printf("비만\n");
    }

    return 0;
}