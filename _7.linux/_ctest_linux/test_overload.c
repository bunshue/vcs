#include <stdio.h>


int print( char *s );                  // Print a string.  
int print( double dvalue );            // Print a double.  
int print( double dvalue, int prec );  // Print a double with a  


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

