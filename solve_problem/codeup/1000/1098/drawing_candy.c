#include <stdio.h>

int main(void)
{
    int i, j;
    int matrix[101][101] = { 0, };
    int h, w;
    int n;
    int l, d, x, y;

    scanf("%d %d", &h, &w);
    scanf("%d", &n);

    for(i=0; i<n; i++) {
        scanf("%d %d %d %d", &l, &d, &x, &y);

        if(d == 0) {
            for(j=y; j<y+l; j++) {
                matrix[x][j] = 1;
            }
        } else {
            for(j=x; j<x+l; j++) {
                matrix[j][y] = 1;
            }
        }
    }

    for(i=1; i<=h; i++) {
        for(j=1; j<=w; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}