#include <stdio.h>

int main(void)
{
    int day1, day2, day3;
    int day = 1;

    scanf("%d %d %d", &day1, &day2, &day3);

    while(day%day1 != 0 || day%day2 != 0 || day%day3 != 0) {
        day++;
    }
    
    printf("%d\n", day);

    return 0;
}