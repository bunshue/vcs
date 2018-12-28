 #include <stdio.h>
 main(void)
 {
    char string[256];
    int count=0;

    printf("Input a string (max 256 characters) :");
    scanf("%s",string);

    while (string[count] != '\0')
      count=count+1;

    printf("The length of \"%s\" is %d\n",string,count);
 }
