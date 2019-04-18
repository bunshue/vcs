 #include <stdio.h>
 main(void)
 {
  int i,j,k;
  int a[7]={25,45,23,49,17,78,93};
  int b[9]={23,55,42,77,41,56,17,90,78};
  int c[5]={65,33,17,42,44};
    
  for (i=0;i<7;i++)
     {
     for (j=0;j<9;j++)
        {
        for (k=0;k<5;k++)
           {
           if ((a[i]==b[j]) && (a[i]==c[k]))
              {
              printf("You got it!\n");
              printf("i=%d, j=%d, k=%d, value=%d\n",i,j,k,a[i]);       
              goto prg_end;
              }
           }
        }
     }
  printf("There is no match");

  prg_end:
 }
