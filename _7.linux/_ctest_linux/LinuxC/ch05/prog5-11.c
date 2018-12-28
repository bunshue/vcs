 #include <stdio.h>
 main(void)
 { 
     char s;  /* 若宣告成 signed char; 亦有相同的結果 */
     s='\x8c';
     printf("%d", s);
 }
