 #include <stdio.h>
 main(void)
 {
 char  oper;
 printf("A. format\n");
 printf("B. copy\n");
 printf("C. remove\n");
 printf("D. exit\n");
 printf("Please select one:");
 scanf("%c",&oper);

 switch (oper)
       {
       case 'A':printf("[format...]");
                break;
       case 'B':printf("[copy...]");
                break;
       case 'C':printf("[remove...]");
                break;
       case 'D':printf("bye-bye!");
                break;
       default: printf("\a");
                break;
       }
 }
