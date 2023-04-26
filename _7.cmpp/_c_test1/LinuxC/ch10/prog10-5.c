 #include <stdio.h>
 struct data {
                 char *name;
                 int  age;
             } x,y;   /* x and y are structures */
 main(void)
 {
   x.name="Lin S.M";
   x.age=24;

   y=x;
   printf("y's name=%s, y's age=%d\n",y.name,y.age);
 }
