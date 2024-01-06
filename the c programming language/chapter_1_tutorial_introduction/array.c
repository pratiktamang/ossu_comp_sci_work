#include <stdio.h>
#define MAX_WORDS 0

/* count digits, white space, others */

int main()
{
    int c, i, nwhite, nother;
    int word_n[MAX_WORDS]; // declares ndigit to be an array of 10 integers


    nwhite = nother = 0;
    for (i = 0; i < MAX_WORDS; ++i)
        word_n[i] = 0;

    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9')
            ++word_n[c-'0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;

        printf("digits =");
        for (i = 0; i < MAX_WORDS; ++i)
            printf(" %d", word_n[i]);
        printf(", whitespace = %d, other = %d\n", nwhite, nother);
}