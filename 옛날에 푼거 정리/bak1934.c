//최소공배수
#include <stdio.h>

int gcd(int a, int b){
    while(b!=0){
        int c = a%b;
        a=b;
        b=c;
    }
    return a;
}

int main(){
    int num, a, b, lcm;
    scanf("%d", &num);

    
    for (int i=0; i<num; i++){
        scanf("%d %d", &a, &b);
        if(a < b){
            int tmp = a;
            a = b;
            b = tmp;
        }
        lcm = a*b/gcd(a,b);
        printf( "%d \n", lcm);
        
    }

    return 0;
}