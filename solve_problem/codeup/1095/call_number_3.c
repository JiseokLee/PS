#include <stdio.h>
 
int main(void)
{
    int n;
    int num_list[10000];
    int fastest_num = 24;
 
    scanf("%d", &n);
 
    for(int i=0; i<n; i++) {
        scanf("%d", &num_list[i]);
        if(num_list[i] < fastest_num) {
            fastest_num = num_list[i];
        }
    }
 
    printf("%d\n", fastest_num);
 
    return 0;
}