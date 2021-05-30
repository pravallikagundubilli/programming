//program to calculate the area of triangle using heron's formula
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
main()
{
float a,b,c,s,area;
printf("enter the values");
scanf("%d%d%d",&a,&b,&c);
s=(a+b+c)/2;
area=sqrt(s*(s-a)*(s-b)*(s-c));
printf("area of triangle is=%f",area);
}
