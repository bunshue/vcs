 #include <stdio.h>
 main(void)
 {
  char a[80];
  char b[] = "What is your name?";
  char c[] = "Hi!";

  puts(b);
  fgets(a,80,stdin);
  puts(c);
  puts(a);
 }
