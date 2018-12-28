 #define  FIRST 1    /* 開始 */
 #define  LAST  9    /* 結束 */
 #define  STEP  1    /* 間隔 */
 main(void)  /* square from 1..9 */
 {
  int i,a;
  
  for (i=FIRST; i<=LAST; i=i+STEP)
  printf("i=%d  i*i=%d\n",i,i*i);
 }
