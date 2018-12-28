 #include<stdio.h>

 main(void)
 {
  int i,j=0,right=0;
  int guess[5]={3,2,8,6,5};
  do
  {
     printf ("Guess my magic number:");
     scanf("%d",&i);
     if (i==guess[j++])	   right++;
  }
  while (j<5);

  switch (right) {
  default:
	printf("You miss all, Hahaha...");
	break;
  case 1:
	printf("Sorry, bad luck...");
	break;
  case 2:
	printf("Try again!");
	break;
  case 3:
	printf("Not bad.");
	break;
  case 4:
	printf("Good!");
	break;
  case 5:
	printf("Oops! You are super!");
  }
 }

