 #include <unistd.h> 
 #include <stdio.h>
 main(void)
 {
  char oldfilename[100], newfilename[100];
  printf ("Please input source filename:");
  scanf("%s", oldfilename);
  printf ("Please input target filename:");
  scanf("%s", newfilename);

  link(oldfilename, newfilename);  
 }
