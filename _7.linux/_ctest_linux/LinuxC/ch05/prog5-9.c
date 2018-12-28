 #include <stdio.h>
 main(void)
 {
   int i=0,j=1;
   printf("Please input first number:");
   scanf("%d",&i);
   printf("Please input second number:");
   scanf("%d",&j);
   printf("%s",(i+j<10?"OK\n":"Wrong\n"));
 }
