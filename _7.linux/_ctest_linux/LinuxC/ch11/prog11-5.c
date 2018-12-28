 #include <stdio.h>
 main(void)
 {
  char s[255],name[20];
  int ret;
  FILE *fp,*fopen();
         
 printf("Input filename:");
 scanf("%s",name);
 fp=fopen(name,"r");

 while ((fgets(s,255,fp)) != NULL)
     fputs(s,stdout);
     fclose(fp);
 }
