 #include <unistd.h>
 #include <string.h>
 #include <stdio.h>
 main(void)
 {
  char name[]="mylinux.flag.com.tw";
  int len,r;
  len=strlen(name);
  r=sethostname(name,len);
  
  if (r !=0)
     printf("Setup failure!\n");
  else
     printf("Setup success!\n");
 }
