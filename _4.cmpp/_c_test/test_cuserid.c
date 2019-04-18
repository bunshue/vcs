#include <stdio.h>
#include <unistd.h>
int main(int argc,char* argv[])
{
        printf("I am %s.\n", cuserid());
        return 0;
}

