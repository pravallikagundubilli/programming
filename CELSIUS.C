/*program to convert celsius to farenheit and vice versa*/
#include<stdio.h>
#include<conio.h>
main()
{
float c,f,faren,cel;
printf("enter the value of celsius");
scanf("%f",&c);
faren=(c*1.8)+32;
printf("the farenheit temp is %0.2f",faren);
printf("\n enter the farenheit value");
scanf("%f",&f);
cel=(f-32)/1.8;
printf(" the celsius temp is %0.2f",cel);
}
