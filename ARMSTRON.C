//program to find whether a given number is armstrong or not
#include<stdio.h>
#include<math.h>
main()
{
int num,r,sum=0,temp,digits=0;
printf("enter a number:");
scanf("%d",&num);
temp=num;
while(temp!=0)
{
digits++;
temp=temp/10;
}
temp=num;
while(num!=0)
{
r=num%10;
sum=sum+pow(r,digits);
num=num/10;
}
if(temp==sum)
printf("it is an armstrong number");
else
printf("it is not an armstrong number");
}



