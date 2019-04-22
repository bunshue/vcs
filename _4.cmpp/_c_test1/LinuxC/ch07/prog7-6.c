 #include<stdio.h>
 void hanoi(int,int,int,int);
 char tower[][4]={"1st","2nd","3rd"};

 main(void)
 {
  int i;
  printf("How many plate(s) to move?");
  scanf("%d",&i);
  hanoi(i,0,1,2);
 }

 void hanoi(int i,int begin,int mid,int dest)
 {
  if (i==1)
    printf("Move plate %d from %s tower to %s tower\n",
	i,tower[begin],tower[dest]);
  else
  {
    hanoi(i-1,begin, dest, mid);
    printf("Move plate %d from %s tower to %s tower\n",
	i,tower[begin],tower[dest]);
    hanoi(i-1,mid, begin, dest);
  }
  return;
 }
