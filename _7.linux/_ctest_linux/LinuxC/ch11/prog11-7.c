 #include <stdio.h>
 main(void)
 {
     int age;
     char file[15],name[20],addr[30];
     FILE *fp;

     printf("Input filename :");
     scanf("%s",file);
     fp=fopen(file,"r");
     if (fp==NULL) exit(1);

     while ((fscanf(fp,"%s %s %d",name,addr,&age))!= EOF)
         printf("%-20s%-30s%-d\n",name,addr,age);
     if (fclose(fp)==-1) exit(1);
 }
