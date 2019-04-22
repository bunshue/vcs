 #include <stdio.h>
 struct person  {
                 char name[32];
                 char addr[20];
                 int  age;
                 };
 main(void)
 {
  struct person student;

  printf("name = :");
  scanf("%s",student.name);
  printf("addr = :");
  scanf("%s",student.addr);
  printf("age  = :");
  scanf("%d",&student.age);
  /* input 3 data then display */

  printf("%-32s %-20s %3d\n",student.name,
            student.addr,student.age);
 }
