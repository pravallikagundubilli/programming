//program to make a simple calculator to add,subtract,multiply ,divide using switch case
#include<stdio.h>
main()
{
char op;
int a,b;
printf("enter an arthematic operator(+,-,/,*)");
scanf("%c",&op);
printf("enter two numbers ");
scanf("%d %d",&a,&b);
switch(op)
{
case '+':printf("%d+%d=%d",a,b,a+b);
       break;
case '-':printf("%d-%d=%d",a,b,a-b);
       break;
case '*':printf("%d*%d=%d",a,b,a*b);
       break;
case '/':printf("%d/%d=%d",a,b,a/b);
       break;
case '%':printf("%d%%d=%d",a,b,a%b);

       break;
default:printf("invalid operation");
	break;
}
}
