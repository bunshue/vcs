 #include <stdio.h>
 struct person {
                 char name[10];
                 char addr[10];
                 int  age;
	       };
 void readdata (struct person*);
 
 main(void)
 {
  struct person student;
        
  readdata(&student);
  printf("\n");
  printf("Name = %s\n",student.name);
  printf("Addr = %s\n",student.addr);
  printf("Age  = %d\n",student.age);
 }

 void readdata(struct person *p)
 {
  printf("Your name ? ");
  scanf("%s",p->name);
  printf("Your addr ? ");
  scanf("%s",p->addr);
  printf("Your age  ? ");
  scanf("%d",&p->age);
 }
