 #include<stdio.h>
 typedef struct person {
                 char *name;
                 char *addr;
                 int  age;
	       } prn;

 prn changeit(struct person);

 main(void)
 {
  prn wu;
  static prn student={"liu","Tainan",20};
  printf("Before calling...\n");
  printf("Ms. %s lived at %s when she was %d years old."
	 ,student.name,student.addr,student.age);

  wu=changeit(student);
  printf("\nAfter calling...\n");
  printf("Ms. %s lived at %s when she was %d years old.\n"
         ,wu.name,wu.addr,wu.age);
 }

 prn changeit(prn p)
 {
        p.addr = "Taipei";
        p.age =100;
        return(p);  /* return a structure */
 }
