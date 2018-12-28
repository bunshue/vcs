 #include <stdio.h>

 struct  person {
                 char  name[32];
                 int   age;
                };
 struct  card {
               struct  person p;
               char    addr[20];
              } student, *stp;

 main(void)
 {
  stp=&student;
  printf("Your name :");
  scanf("%s",stp->p.name);
  printf("Your age :");
  scanf("%d",&student.p.age);
  printf("Your address :");
  scanf("%s",student.addr);

  printf("%-32s%3d %-20s\n",student.p.name,stp->p.age,stp->addr);
 }
