 #include <stdio.h>
 main(void)
 {
  char s[30];
  char *test(char*),*t;

  printf("Please input a filename with extension:");
  scanf("%s",s);
  t=test(s);
  printf("EXT of filename %s is %s\n",s,t);
 }

 char *test(char* string)
 {
         while (* string ++ !='.');
         return(string);
 }
