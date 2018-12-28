 #include <stdio.h>
 #include <stdlib.h>
 #define  quit1  printf("Cannot open file\n"); exit(1)
 #define  quit2  printf("Cannot close file\n"); exit(1)

 main(void)
 {
  int c,ret;
  char name[20];
  FILE *stream,*fopen();

  printf("Please input a filename :");
  scanf("%s",name);

  if((stream=fopen(name,"r"))==NULL)  { quit1; }
  printf("*** file open ***\n");

  while ( (c=fgetc(stream)) !=EOF)
           putchar(c);
  if ( (ret=fclose(stream))==-1)      {  quit2; }
  printf("\n*** file close ***\n");
 }
