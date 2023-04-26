 #include<stdio.h>
 main(void)
 {
     int i=1;
     while(i != 0) {
           scanf("%d", &i);
           if ((i % 2) == 0)
              printf("even!\n");
           else
              printf("odd!\n");
     }
 }
