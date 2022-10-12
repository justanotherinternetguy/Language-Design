#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#include <string.h>

static char bufer[2048];

// Fake readline func
char* readline(char* prompt) {
    fputs(prompt, stdout);
    fgets(buffer, 2048, stdin);
    char* cpy = malloc(strlen(buffer) + 1);
    strcpy(cpy, buffer);
    cpy[strlen(cpy) - 1] = '\0';
    return cpy
}

// Fake add_history func
void add_history(char* unused) {}

#else
#include <readline/readline.h>
#include <readline/history.h>
#endif

int main(int argc, char** argv) {
    while (1) {
        char* input = readline("LispCy >> ");
        add_history(input);
        
        printf("you typed %s\n", input);
        free(input);
    }
    return 0;
}
