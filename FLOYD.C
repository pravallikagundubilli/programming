//program to print floyd triangle
#include<stdio.h>
#include<conio.h>
main()
{
int i,j,n,sum=1;
printf("enter number of rows");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
for(j=1;j<=i;j++)
{
printf("%d   ",sum);
sum++;
}
printf("\n");
}
}