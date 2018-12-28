 #include <stdio.h>
 struct person  {
                 char name[32];
                 char addr[20];
                 int  age;
                 };
 main(void)
 {
  struct person student;
  struct person *p; /* pointer of structure */

  p=&student;
  printf("Your name :");
  scanf("%s",p->name);
  printf("Your address :");
  scanf("%s",p->addr);
  printf("Your age :");
  scanf("%d",&p->age);

  printf("%-32s%-20s%3d\n",p->name,p->addr,p->age);
  printf("%-32s%-20s%3d\n",(*p).name,(*p).addr,(*p).age);
 }
