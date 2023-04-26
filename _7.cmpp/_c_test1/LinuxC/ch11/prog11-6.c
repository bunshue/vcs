 #include <stdio.h>
 main(void)
 {
     int m,age;
     char file[15],name[20],addr[30];
     FILE *fp;

     printf("Input filename:");
     scanf("%s",file);
     fp=fopen(file,"w");

     for (m=0;m<3;m++){
         printf("Name=");
         scanf("%s",name);
         printf("Addr=");
         scanf("%s",addr);
         printf("Age =");
         scanf("%d",&age);
         fprintf(fp,"%-20s%-30s%-d\n",name,addr,age);
      }
 }
