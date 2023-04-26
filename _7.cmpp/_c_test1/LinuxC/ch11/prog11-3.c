 #include <stdio.h>
 #include <stdlib.h>
 main (void)
 {
  int c,ret;
  char name1[20],name2[20];
  FILE *stream1, *stream2;

  printf("Input source filename :");
  scanf("%s",name1);
  printf("Input destination filename :");
  scanf("%s",name2);
  stream1=fopen(name1,"r");

  if (stream1==NULL)
  {
     puts("Cannot open read_file\n");
     exit(1);
  }
  stream2=fopen(name2,"w");

  if (stream2==NULL)
  {
     puts("Cannot open write_file\n");
     exit(1);
  }
  while ( (c=fgetc(stream1)) != EOF)
           fputc(c,stream2);
  fclose(stream1);
  fclose(stream2);
  printf("Copy complete!\n");
 }
