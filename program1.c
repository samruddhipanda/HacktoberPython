#include <studio.h>
int main ()
{
    printf ("Files in directory are:\n");
    execl ("/bin/ls", "ls", NULL);
    printf("Listing compleed\n");
    return 0;
}