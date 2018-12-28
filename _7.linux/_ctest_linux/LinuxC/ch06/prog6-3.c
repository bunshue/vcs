 #include <stdio.h>
 main(void)
 {
  char func;
  printf("Command ? ");
  scanf("%c",&func);
  if      ( func=='a' || func=='A')
          printf("Append\n");
  else if ( func=='d' || func=='D')
          printf("Delete\n");
  else if ( func=='u' || func=='U')
          printf("Update\n");
  else
          printf("illegal command!\n");
 }
