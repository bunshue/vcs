 #include <stdio.h>
 #include <stdlib.h>
 #include <ctype.h>
 main(void)
 {
  int m,n,count,c;
  unsigned static char data[10000];
  char name[20];
  FILE *fp;

  printf("Input the filename to dispay:");
  scanf("%s",name);
  fp=fopen(name,"rb");
  if (fp==NULL) exit(1);
  for (m=0;m<10000;m++)
  {
   c=fgetc(fp);
   if (c==EOF) break;
   data[m]=c;
  }

  for (count=0,c=0;count<m;count+=16,c++)
  {
   printf("%04x ",count);
   for (n=0;n<16;n++)
	printf("%02x ",data[count+n]);
   for (n=0;n<16;n++)
   { if ( isprint(data[count+n]) )
       printf("%c",data[count+n]);
     else
       printf(".");
   }
	   
   if ((c%24)==23)
   {
    printf("\nPress any key to continue..");
    getchar();
   }

   printf("\n");
   }
   
  fclose(fp);
 }
