 #include <stdio.h>
 main(void)
 {
    char c,l;
    char lower(char s);
    while ((c=getchar()) != '\x1a')
      {
        l = lower(c);
        putchar(l);
      }
 }

 char lower(char s)
 {
    if (s >= 'A' && s <= 'Z')
         s = s+('a'-'A');
    return s;
 }
