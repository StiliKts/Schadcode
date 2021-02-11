#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    int pass = 0;

    printf("\n Bitte geben Sie das Passwort ein: \n");
    gets(buff);

    if(strcmp(buff, "AltenGmbH"))
    {
        printf ("\n Falsches Passwort \n");
    }
    else
    {
        printf ("\n Richtiges Passwort \n");
        pass = 1;
    }

    if(pass)
    {
       
        printf ("\n Root privilegien wurden an den user uebertragen \n");
    }

    return 0;
}