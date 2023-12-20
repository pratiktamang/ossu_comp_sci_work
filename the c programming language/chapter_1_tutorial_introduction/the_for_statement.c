#include <stdio.h>
/* print Fahrenheit-Celcius table*/

int main()
{
    // int fahr;
    // for(fahr = 0; fahr <=300; fahr = fahr + 20)
    //     printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    int i;
    for(i = 0; i <=300; i=i+20)
        printf("%3d %6.1f\n", i, (5.0/9.0)*(i-32));

    // in reverse order
    for(i = 300; i >= 0; i=i-20)
        printf("%3d %6.1f\n", i, (5.0/9.0)*(i-32));
}