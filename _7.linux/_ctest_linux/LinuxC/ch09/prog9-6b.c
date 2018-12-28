 #include<stdio.h>
 main(void)
 {
  int i,c;
  char pop(void);
  void push(char),dump(void);

       puts("Pushing...");
       for (i=0; i<5; i++)
           {
           push('a'+i);
           dump();
           }
       puts("\nPoping...");
       for (i=0; i<5; i++)
           {
           c= pop();
           dump();
           }
 }

