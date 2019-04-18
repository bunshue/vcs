 #include<stdio.h>
 int counter=0;
 main(void)
 {
  int  i;
  void inc();
  for (i=0; i<5; i++)
     {
      inc();
      counter++;
      printf("In main() counter= %d\n",counter);
     }
 }

 void inc(void)
 {
  counter++;
  printf("In inc() counter= %d  ",counter);
 }
