 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>

 main(void)
 {
    unsigned char *get_block,*pointer;

    pointer="TEST!";

    get_block=(unsigned char*)malloc(sizeof(char)*strlen(pointer)+1);

    strcpy(get_block,pointer);

     *get_block='t';

     get_block[2]='s';
 
     puts(pointer);
 
     puts(get_block);

     free(get_block);
 }
