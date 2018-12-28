 #include <stdio.h>
 main(void)
 {
  static char s[3][20]={ "This is a book",
                         "talking about",
                         "C language" };
  printf("%s %s %s.\n",s[0],s[1],s[2]);
 }
