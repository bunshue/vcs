 #include <stdio.h>
 main(void)
 {
   void func(void);

        func();
 }

 void  func(void)
 {
  printf("This is a non_stop program\n");
  func();
 }
