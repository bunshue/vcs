 #include<stdio.h>
 main(void)
  {
   int  i;
   void inc(),dec(),display();
   puts("Increasing...");
   for (i=0; i<5; i++)
     {
        inc();
        display();
     }
   puts("Decreasing...");
   for (i=0; i<5; i++)
     {
        display();
        dec();
     }
  }

  int counter=0;

  void inc()
  {
       counter++;
  }

  void dec()
  {
       counter--;
  }

  void display()
  {
       printf("Counter= %d\n",counter);
  }
