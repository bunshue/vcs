 #include <stdio.h>
 main(void)
 {
 static int a[2][3]= {{0,1,2}, {3,4,5} };
 int    m,n;
 for (m=0;m<2;m++)
   {
     for (n=0;n<3;n++)
       {
        printf("a[%d][%d] = %d\n",m,n,a[m][n]);
       }
   }
 }
