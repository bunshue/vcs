 #include <stdio.h>
 #include <sys/sysinfo.h> 
 main(void)
 {
  struct sysinfo buf;
  sysinfo(&buf); 
  printf("Total ram = %d\n", buf.totalram);
  printf("Free ram = %d\n", buf.freeram); 
 }
