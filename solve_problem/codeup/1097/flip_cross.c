#include <stdio.h>

int main()
{
    int i, j;
    int matrix[19][19] = {};
    int n;
    int x, y;

    for(i=0; i<19; i++) {
        for(j=0; j<19; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    scanf("%d", &n);

    for(i=0; i<n; i++) {
        scanf("%d %d", &x, &y);
        x--;
        y--;

        for(j=0; j<19; j++) {
            if(matrix[x][j] == 0) {
                matrix[x][j] = 1;
            } else {
                matrix[x][j] = 0;
            }
        }

        for(j=0; j<19; j++) {
            if(matrix[j][y] == 0) {
                matrix[j][y] = 1;
            } else {
                matrix[j][y] = 0;
            }
        }
    }

    for(i=0; i<19; i++) {
        for(j=0; j<19; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
