 #include <stdio.h>
 main(void)
 {
     struct person{
        char name[20];
        char addr[30];
        int age;
     } data;

     int number;
     FILE *fp;

     printf("Input record number (1-3):");
     scanf("%d",&number);

     fp=fopen("test3.dat","r+b");
     if (fp==NULL) exit(1);
     fseek(fp,(number-1)*sizeof(data),SEEK_SET);
     if (fread(&data,sizeof(data),1,fp)==1)
         printf("%-20s%-30s%-d\n",data.name,data.addr,data.age);
     if (fclose(fp)==-1) exit(1);
 }
