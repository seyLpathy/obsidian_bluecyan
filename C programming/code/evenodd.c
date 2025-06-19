#include<stdio.h>
#define YES 1
#define NO 0
int iseven(int number)
{
    int answer;
    if (number % 2 == 0)
        answer=YES;
    else
        answer=NO;
    return answer;
}
int main(void)
{
    int iseven(int number);
    if (iseven(17)==YES)
        printf("YES");
    else
    printf("NO");
    if (iseven(20)==YES)
        printf("yes\n");
    else 
        printf("no\n");
    return 0;
}