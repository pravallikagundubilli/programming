//program to find whether the given year is a leap year
#include<stdio.h>
main()
{
int year;
printf("enter a year");
scanf("%d",&year);
if(year%400==0)
printf("%d is a leap year\n",year);
else if(year%100==0)
printf("%d is a not a leap year\n",year);
else if(year%4==0)
printf("the year is a leap year\n");
else
    printf("is not a leap  year");
}
