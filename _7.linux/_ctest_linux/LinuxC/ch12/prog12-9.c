 #include <sys/types.h>
 #include <sys/stat.h> 
 #include <unistd.h>
 #include <stdio.h>
 main(void)
 {
  char filename[100];
  struct stat filestat;

  printf ("Please input filename:");
  scanf("%s", filename);
  stat(filename, &filestat);
  
  chmod(filename, filestat.st_mode|00002);  
 }
