 #include <stdio.h>
 struct person  {
                 char name[32];
                 char addr[20];
                 int  age;
                 };
 main(void)
 {
  struct person student[20];
  struct person *p;  /* pointer of structure */
  int i;

  p=student;
  for (i=0;i<5;i++,p++)
      printf("address of person[%d] = %x\n",i,p);
 }
