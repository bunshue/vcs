 #include<stdio.h>
 int counter=0;

 main(void)
 {
  int  i;
  extern void inc(void);
  for (i=0; i<5; i++)
     {
      inc();
      counter++;
      printf("In main() counter= %d\n",counter);
     }
 }
