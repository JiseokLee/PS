#include <stdio.h>

int main(void)
{
    int n;
    int x, y;
    int matrix[19][19] = { 0, };

    scanf("%d", &n);

    for(int i=0; i<n; i++) {
        scanf("%d %d", &x, &y);
        matrix[x-1][y-1] = 1;
    }

    for(int i=0; i<19; i++) {
        for(int j=0; j<19; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}