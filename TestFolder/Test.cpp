#include<stdio.h>

int main() {
    int a;
    printf("Hello world!\n");
    
    printf("\n\n숫자를 입력하세요 : ");
    
    scanf("%d", &a);

    printf("입력된 숫자 : %d\n", a);

    scanf("%d", &a);
}