//program  to print whether the given number is palindrome or not
#include<stdio.h>
main()
{
int num,rev=0,rem,temp;
printf("enter a number");
scanf("%d",&num);
temp=num;
while(num!=0)
{
rem=num%10;
rev=rev*10+rem;
num=num/10;
}
if(temp==rev)
printf("it is a palindrome");
else
printf("it is not a palindrome");
}
