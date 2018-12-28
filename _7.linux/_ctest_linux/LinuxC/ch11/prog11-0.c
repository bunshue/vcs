 #include <stdio.h>
 main(void)
 {
   FILE *fp1;
   char c;

   fp1=fopen("text.txt","w");
   while ((c=getchar())!='\n')
       putc(c,fp1);
   fclose(fp1);
 }
