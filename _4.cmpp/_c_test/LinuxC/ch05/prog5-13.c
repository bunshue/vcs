 #include<stdio.h>
 main(void)
 {
     int ii;
     double dd;

     dd=(float) 400/3;   /* �N 400 �ন float ���O */
     printf("dd=400/3=%f\n",dd);

     ii=-3-6;
     printf("ii=%d\n",ii);
     ii=(unsigned char) -3 -6;
     printf("ii=%d\n",ii);
 }
