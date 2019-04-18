 #include<stdio.h>
 main(void)
 {
  char s[3];
  FILE *stream;

  stream=fopen("file.txt","r+");
  fseek(stream,3,SEEK_SET);
  fgets(s,4,stdin);
  fputs(s,stream);
  fclose(stream);
 }
