#include <stdio.h>

int main(void)
{
    int is_flip[4];
    int is_flip_count = 0;
    int i;

    for (i = 0; i < 4; i++)
    {
        scanf("%d", &is_flip[i]);
    }

    for (i = 0; i < 4; i++)
    {
        if (is_flip[i] == 1)
        {
            is_flip_count++;
        }
    }

    if (is_flip_count == 1)
    {
        printf("��\n");
    }
    else if (is_flip_count == 2)
    {
        printf("��\n");
    }
    else if (is_flip_count == 3)
    {
        printf("��\n");
    }
    else if (is_flip_count == 4)
    {
        printf("��\n");
    }
    else
    {
        printf("��\n");
    }

    return 0;
}
