 #include <stdio.h>
 #include <stdlib.h>
 main(void)
 {  int  number=0;
    char c='\0';
    number=rand();   /* ���ü� */
    printf("Even or Odd (E/O)?"); /* �Τj�g�� E �� O */
    c=getchar();
    if(c=='E' && number%2==0 || c=='O' && number%2==1)
       printf("\nRight! number=%d\n",number);
    else
       printf("\nWrong! number=%d\n",number);
 }
