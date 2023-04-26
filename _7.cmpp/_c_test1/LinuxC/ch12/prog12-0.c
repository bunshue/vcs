 #include <stdio.h>
 #include <sys/utsname.h>
 main(void)
 {
  struct utsname myname;
  uname(&myname);

  //printf ("SYS_NMLN = %d\n", SYS_NMLN); 
  printf ("The OS name is %s\n", myname.sysname);
  printf ("The name of machine is %s\n", myname.nodename);
  printf ("The OS version is %s, %s\n", myname.release, myname.version);
  printf ("The hardware type is %s\n", myname.machine);
 }
