#include <stdio.h>
#define LOWER 0
#define UPPER 300
#define STEP 300

/* print Fahrenheit-Celcius table*/

int main()
{
    // int fahr;
    // for(fahr = 0; fahr <=300; fahr = fahr + 20)
    //     printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    int fahr;
    for(fahr = LOWER; fahr <=UPPER; fahr=fahr+20)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}