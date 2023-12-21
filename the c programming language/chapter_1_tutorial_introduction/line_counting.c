/*
    Count lines in input
    Exercise 1-8. Write a program to count blanks, tabs, and newlines.
*/
#include <stdio.h>
int main()
{
    int c, nl = 0, t = 0, b = 0;

    while ((c = getchar()) != EOF){
        if (c == '\n')
            ++nl;
        else if (c == '\t')
            ++t;
        else if (c == ' ')
            ++b;
    }

    printf("New Lines: %d\n", nl);
    printf("Blanks: %d\n", b);
    printf("Tabs: %d\n", t);
}
