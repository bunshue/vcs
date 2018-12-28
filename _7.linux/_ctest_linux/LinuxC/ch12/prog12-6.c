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
  printf("The size of %s is %d\n", filename, filestat.st_size); 
 }
