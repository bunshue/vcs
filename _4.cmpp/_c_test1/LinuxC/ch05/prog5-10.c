 #include<stdio.h>
 main(void)
 {
     char   cc;
     int    ii;
     float  ff;
     double dd;
     long   ll;

     dd=400/3;
     printf("dd=400/3  =%f\n",dd);
     cc=ii=ff=dd=400/3.0;
     printf("dd=400/3.0=%f\n",dd);
     printf("ff=400/3.0=%f\n",ff);
     printf("ii=400/3.0=%d\n",ii);
     printf("cc=400/3.0=%d\n",cc);
 }
