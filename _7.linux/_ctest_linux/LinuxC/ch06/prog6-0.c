 #include <stdio.h>
  main(void)
  {
    char c;
    c=getchar();
    if ('a'<=c && c<='z')
       printf("It is a lowercase letter\n");

    else
       printf("It is not a lowercase letter\n");
  }
