 #include<stdio.h>
 main(void)
 {
     int ii;
     double dd;

     dd=(float) 400/3;   /* 將 400 轉成 float 型別 */
     printf("dd=400/3=%f\n",dd);

     ii=-3-6;
     printf("ii=%d\n",ii);
     ii=(unsigned char) -3 -6;
     printf("ii=%d\n",ii);
 }
