#include <stdio.h>

int main(void)
{
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    if (a + b > c)
    {
        if (a == b && b == c)
        {
            printf("���ﰢ��\n");
        }
        else if (a * a + b * b == c * c)
        {
            printf("�����ﰢ��\n");
        }
        else if (a == b || a == c || b == c)
        {
            printf("�̵�ﰢ��\n");
        }
        else
        {
            printf("�ﰢ��\n");
        }
    }
    else
    {
        printf("�ﰢ���ƴ�\n");
    }

    return 0;
}