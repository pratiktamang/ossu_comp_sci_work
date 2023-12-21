/*
Write a program to copy its input to its output, replacing
each string of one or more blanks by a single blank
*/

#include <stdio.h>

int main()
{
    int c;
    int current_is_blank=0;

    while ((c = getchar()) != EOF){
        if (c == ' ' || c == '\t' || c == '\n'){
            if(!current_is_blank){
                putchar(c);
                current_is_blank=1;
            }
        } else {
            putchar(c);
            current_is_blank=0;
        }
    }

    return 0;
}