 #include<stdio.h>
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
       case 'a':
       case 'A':printf("[format...]");
                break;
       case 'b':
       case 'B':printf("[copy...]");
                break;
       case 'c':
       case 'C':printf("[remove...]");
                break;
       case 'd':
       case 'D':printf("bye-bye!");
                break;
       default: printf("\a");
                break;
       }
 }
