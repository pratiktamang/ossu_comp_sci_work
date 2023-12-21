#include <stdio.h>

/* count characters in input; 1st version */

// int main() {
//     long nc;

//     nc = 0;
//     while(getchar() != EOF){
//         ++nc;
//         printf("%ld\n", nc);
//     }

//     return 0;
// }

/* count characters in input; 2nd version */

int main()
{
    double nc;
    
    for(nc=0; getchar() != EOF; ++nc)
    ;
    printf("%.0f\n", nc);
    return 0;
}

// the body of the for loop is empty, because all of the work
// in the test and increment parts. Grammatical rules of C 
// require that a for statement have a body.
// The isolated semicolon, called a null statement is there
// to satisfy that requirement.