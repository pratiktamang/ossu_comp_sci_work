/* Write a program that prints its input one word per line. */

#include <stdio.h>

int main()
{
    int c;
    int current_is_blank=0;

    while ((c = getchar()) != EOF){
        if (c == ' ' || c == '\t' || c == '\n'){
            if(!current_is_blank){
                putchar('\n');
                current_is_blank=1;
            }
        } else {
            putchar(c);
            current_is_blank=0;
        }
    }

    return 0;
}