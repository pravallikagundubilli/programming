//program to find whether the given number is prime number or not
#include<stdio.h>
main()
{
int i,n,count=0;
printf("enter a number");
scanf("%d",&n);
i=1;
while(i<=n/2)
{
if(n%i==0)
count++;
i++;
}
if(count==1)
 printf("it is a prime number");
else
 printf("it is not a prime number");
}
