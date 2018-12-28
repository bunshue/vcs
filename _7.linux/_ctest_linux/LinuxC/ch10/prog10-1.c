  #include <stdio.h>
  struct person  {
                  char name[32];
                  char addr[20];
                  int  age;
                  };
  main(void)
  {
   struct person student[20];
   printf("size of student array = %d byte\n",
            sizeof(student));
  }
