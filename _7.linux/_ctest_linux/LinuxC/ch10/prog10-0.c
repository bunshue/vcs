 #include <stdio.h>
 struct person  {
                 char name[32];
                 char addr[20];
                 int age;
                 };

 main(void)
 {
  struct person student;
  printf("size of struct person = %d byte\n",
          sizeof(struct person));
  printf("size of variable student = %d byte\n",
          sizeof(student));
 }
