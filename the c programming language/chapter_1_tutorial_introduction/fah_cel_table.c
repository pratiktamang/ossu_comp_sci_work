#include <stdio.h>

/* print Fahrenhiet-Celcius table
    for fahr = 0, 20, ..., 300 */

// #v1, uses integers not quite qccurate
// int main()
// {
//     int fahr, celcius;
//     int lower, upper, step;

//     lower = 0;
//     upper = 300;
//     step  = 20;

//     fahr = lower;
//     while(fahr <= upper) {
//         celcius = 5 * (fahr-32) / 9;
//         printf("%d\t%d\n", fahr, celcius);
//         // printf("%3d %6d\n", fahr, celcius); // right aligned
//         fahr = fahr + step;
//     }
// }

// #v2, uses floating point
#include <stdio.h>
/* print Fahrenhiet-Celcius table
    for fahr = 0, 20, ..., 300 */

void fah_to_cel();
void cel_to_fah();

int main(){
    fah_to_cel();
    cel_to_fah();
}

void cel_to_fah(){
    float fahr, celcius;
    int lower, upper, step;

    lower = 0;
    upper = 100;
    step = 20;

    celcius = lower;
    printf("Celcius to Fahrenheit\n");
    while (celcius <= upper){
        fahr = celcius * (9.0/5.0) + 32.0;
        printf("%3.0f %6.1f\n", celcius, fahr);
        celcius = celcius + step;
    }
}

void fah_to_cel(){
    float fahr, celcius;
    int lower, upper, step;

    lower = 0;
    upper = 100;
    step = 20;

    fahr = lower;
    printf("Fahrenheit to Celcius\n");
    while(fahr<=upper){
        celcius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celcius);
        fahr = fahr + step;
    }
}
/*
    %d      print as decimal integer
    %6d     print as decimal integer, at least 6 characters wide
    %f      print as floating point
    %6f     print as floating point, at least 6 characters wide
    %.2f    print as floating point, 2 characters after decimal point
    %6.2f   print as floating point, at least 6 wide and 2 after decimal point
*/