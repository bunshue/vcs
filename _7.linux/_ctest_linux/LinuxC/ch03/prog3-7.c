 #define  FIRST 1    /* �}�l */
 #define  LAST  9    /* ���� */
 #define  STEP  1    /* ���j */
 main(void)  /* square from 1..9 */
 {
  int i,a;
  
  for (i=FIRST; i<=LAST; i=i+STEP)
  printf("i=%d  i*i=%d\n",i,i*i);
 }
