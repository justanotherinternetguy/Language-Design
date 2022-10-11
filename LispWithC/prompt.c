#include <stdio.h>

// Buffer for userinput of size 2048
static char input[2048];

int main(int argc, char** argv) {
    while (1) {
        // print prompt
        fputs("LispCy >> ", stdout);

        // Readline into input buffer
        fgets(input, 2048, stdin);

        // print input back to user
        printf("you said %s", input);
    }
    return 0;
}
