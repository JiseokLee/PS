#include <stdio.h>

int main(void)
{
    int i;
    int n;
    int num_list[10000] = {};

    scanf("%d", &n);

    for(i=0; i<n; i++) {
        scanf("%d", &num_list[i]);
    }

    for(i=n-1; i>=0; i--) {
        printf("%d ", num_list[i]);
    }

    printf("\n");
    return 0;
}