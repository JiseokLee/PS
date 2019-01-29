#include <stdio.h>

int main(void)
{
    int i, j;
    int maze[10][10] = { 0, };
    int x = 1;
    int y = 1;
    
    for(i=0; i<10; i++) {
        for(j=0; j<10; j++) {
            scanf("%d", &maze[i][j]);
        }
    }

    while(maze[x][y] != 2) {
        maze[x][y] = 9;
        if(maze[x][y+1] != 1) {
            y += 1;
        } else if (maze[x+1][y] != 1) {
            x += 1;
        } else {
            break;
        }
    }

    maze[x][y] = 9;

    for(i=0; i<10; i++) {
        for(j=0; j<10; j++) {
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }

    return 0;
}