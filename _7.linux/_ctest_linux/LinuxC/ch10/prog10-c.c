 #include <stdio.h>
 enum grade {OK=60,Good=80,Excellent=90};

 main(void)
 {
  int score;

  printf("Please input your computer score:");
  scanf("%d",&score);

  if (score>=Excellent)
     printf("You are wonderful!\n");
  else if (score>=Good)
     printf("Nice, keep going\n");
  else if (score>=OK)
     printf("You can do more...\n");
  else
     printf("Don't play too much :P\n");
 }
