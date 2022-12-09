//소수찾기
#include <stdio.h>

int main(void)
{
    int i, j, arr[1000] = {0, };
    int n, num, cnt = 0;
    
    arr[0] = 1, arr[1] = 1;
    
    for(j = 2; j < 1000; j++)
        for(i = j * 2; i < 1000; i++)
            if(i % j == 0) arr[i] = 1;
    
    scanf("%d", &n);
    
    for(i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if(arr[num] == 0) cnt++;
    }
    printf("%d", cnt);
    return 0;
}