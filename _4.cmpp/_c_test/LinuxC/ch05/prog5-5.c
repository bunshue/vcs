 #include <stdio.h>
 main(void)
 {
    int  i=2, j=3;
    int  k,l,m,n,o,p;

    k = i > j;
    l = i < j;
    m = i >= j;
    n = i <= j;
    o = i == j;
    p = i != j;
    printf("i > j : %d   i < j : %d\n",k,l);
    printf("i >=j : %d   i <=j : %d\n",m,n);
    printf("i ==j : %d   i !=j : %d\n",o,p);
 }
