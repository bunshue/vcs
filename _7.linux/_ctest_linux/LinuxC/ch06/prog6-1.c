 #include <stdio.h>
 #include <stdlib.h>
 main(void)
 {  int  number=0;
    char c='\0';
    number=rand();   /* 取亂數 */
    printf("Even or Odd (E/O)?"); /* 用大寫的 E 或 O */
    c=getchar();
    if(c=='E' && number%2==0 || c=='O' && number%2==1)
       printf("\nRight! number=%d\n",number);
    else
       printf("\nWrong! number=%d\n",number);
 }
