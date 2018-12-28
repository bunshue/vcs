#include <stdio.h>
int main(int argc,char* argv[])
{
        int i;
        printf("david: This is a c template.\n");
        for(i=0;argv[i]!=NULL;i++)
                printf("argument %d : %s\n",i,argv[i]);
        for(i=0;i<argc;i++)
                printf("argument %d : %s\n",i,argv[i]);
        return 0;
}

