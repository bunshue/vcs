 #include <stdio.h>
 main(void)
 {
    int key;
    printf("Are you sure (y/n) ?");
    do
    { key=getchar(); }
    while ( (key !='y') && (key !='n') );
    printf("Program end here.\n");
 }
