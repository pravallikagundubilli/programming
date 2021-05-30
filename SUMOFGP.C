//program to print an arthematic progression
#include<stdio.h>
#include<math.h>
main()
{
int x,n,i,sum=0;
printf("\nenter the limit\n");
scanf("%d",&n);
printf("enter the value of x\n");
scanf("%d",&x);
if(x<0||n<0)
{
printf("illegal value");
}
else
{
for(i=0;i<=n;i++)
sum=sum+pow(x,i);
}
printf("sum=%d",sum);
}
