 #include <stdio.h>
 struct person {
                 char *name;
                 char *addr;
                 int  age;
               };
 struct person changeit(struct person);

 main(void)
 {
  struct person wu;
  static struct person student={"liu","Tainan",20};
  printf("Before calling...\n");
  printf("Ms. %s lived at %s when she was %d years old."
         ,student.name,student.addr,student.age);
  wu=changeit(student);
  printf("\nAfter calling...\n");
  printf("Ms. %s lived at %s when she was %d years old.\n"
         ,wu.name,wu.addr,wu.age);
 }
 struct person changeit(p)
 struct person p; /* pass structure*/
 {
        p.addr = "Taipei";
        p.age =100;
        return(p);  /* return a structure */
 }
