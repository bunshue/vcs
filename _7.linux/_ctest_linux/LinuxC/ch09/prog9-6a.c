 #include <stdio.h>
 #define BUFSIZE 255
 static char stack[BUFSIZE];
 static int sp=0;
 void push(char s)
 {
     if (sp<BUFSIZE)
        stack[sp++]=s;
     else
        printf("ERROR: stack full\n");
 }

 int pop(void)
 {
     if (sp>0)
        return(stack[--sp]);
     else
        printf("ERROR: stack empty\n");
 }

 void dump(void)
 {
    int i;
    printf("Contant of stack:");
    if  (sp>0)
        for (i=sp-1;i>=0;i--)
            printf("%c ",stack[i]);
    else
        printf("EMPTY!");
    printf("\n");
 }
