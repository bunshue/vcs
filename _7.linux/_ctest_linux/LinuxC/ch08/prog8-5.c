 #include <stdio.h>
 main(void)
 {
  int a=23;
  int *pa;
  *pa=23;

  printf("Input a integer: ");
  scanf("%d",pa);
  printf("Value you input =%d \n",*pa);
  printf("Input a integer: ");
  scanf("%d",&a);
  printf("Value you input = %d \n",a);

  printf("Input a integer: ");   
  scanf("%d",a); 
  printf("Value you input =%d \n",a);
 }
