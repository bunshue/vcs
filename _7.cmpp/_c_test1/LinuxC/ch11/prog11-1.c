 #include <stdio.h>
 main(void)
 {
   FILE *fp1;
   char c;

   fp1=fopen("test.txt","r");
   while ((c=getc(fp1))!=EOF)
       printf("%c",c);
   fclose(fp1);
 }
