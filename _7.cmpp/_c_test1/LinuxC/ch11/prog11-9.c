 #include <stdio.h>
 main(void)
 {
     int age, number, os;
     char file[]={"test3.txt"},name[20],addr[30];
     FILE *stream;

     printf("Input record number (1-3):");
     scanf("%d",&number);
     stream=fopen(file,"r");

     if (stream==NULL) exit(1);
     fseek(stream,((number-1)*54),SEEK_SET);
     os=ftell(stream);

     if ((fscanf(stream,"%s %s %d",name,addr,&age))!= EOF)
         printf("Offset=%d\n",os);

     if (fclose(stream)==-1) exit(1);
 }
