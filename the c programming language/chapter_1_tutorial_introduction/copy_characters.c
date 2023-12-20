/*
    read a character
    while (character is not end-of-file indicator)
        output the character just read
        read a character
*/
#include <stdio.h>
void v1();
void v2();
void v3();
void v4();

/* copy input to output; 1st version */
int main()
{
    // v1();
    // v2();
    // v3();
    v4();
}

void v1()
{
    int c;

    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}

/* copy input to output; 2nd version */
void v2()
{
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);

}

// Exercise 1-6. Verify that the expression getchar ( ) I= EOF is 0 or 1. 0

void v3(){
    int c;
    while(1) {
        c = getchar() != EOF;
        printf("%d\n", c);
        if(c==0) break;
    }
}
// Exercise 1-7. Write a program to print the value of EOF. 0

void v4(){
    printf("EOF = %d\n", EOF);
}