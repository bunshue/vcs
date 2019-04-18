 #include<stdio.h>

 void main(void)
 {
  int i=100,j=1,*k;
  char *cp;
  long *lp;
  void *vp;

  cp= lp= &i;
  vp= &i;

  printf("Address of i: %x\nAddress of j: %x\n",
	&i,&j);
  printf("*cp=%c  *lp=%d  *(int *)vp=%d\n",
	  *cp,*lp,*(int *)vp);
 }
