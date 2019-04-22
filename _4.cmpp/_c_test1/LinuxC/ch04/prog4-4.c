 #include<stdio.h>
 main()
 {
  float f;
  double d;
  f=5/3.0;	/* 注意, 若寫成 "5/3" 則會變成整數運算, 結果是 1 */
  d=5/3.0;
  printf("f equal to %20.18f\n",f);
  printf("d equal to %20.18f\n",d);
 }
