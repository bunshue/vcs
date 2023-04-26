 #include <stdio.h>
 main(void)
 {
  int  i[5];

  printf("\nPlease input 5 integers:");
  scanf("%d %d %d %d %d", i, i+1, i+2, i+3, i+4);
  fwrite(i,sizeof(int),5,stdout);
 }
