 #include <stdio.h>
 main(void)
 {
     struct person{
	char name[20];
	char addr[30];
	int age;
     } data[3];

     int age,i;
     char name[20],addr[30];
     FILE *fp;

     fp=fopen("test3.txt","r+t");
     if (fp==NULL) exit(1);
     for (i=0;i<3;i++)
	 fscanf(fp,"%s %s %d",
	     &data[i].name,&data[i].addr,&data[i].age);
     if (fclose(fp)==-1) exit(1);

     if ((fp=fopen("test3.dat","w+a"))==NULL) exit(1);
     fwrite (data,sizeof(struct person),3,fp);
     if (fclose(fp)==-1) exit(1);
 }
