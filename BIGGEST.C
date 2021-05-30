/*program to find the largest number using ternary operators*/
#include<stdio.h>
main()
{
int a,b,c,big;
printf("enter the values of a,b,c");
scanf("%d%d%d",&a,&b,&c);
big=a>b?(a>c?a:c):(b>c?b:c);
printf("the biggest among the three numbers is %d",big);
}

