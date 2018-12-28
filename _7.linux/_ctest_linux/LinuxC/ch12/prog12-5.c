 #include <stdio.h>
 #include <sys/vfs.h>
 main(void)
 {
  char path[]="/";
  struct statfs myfsstat;
  statfs(path, &myfsstat);
  
  printf("total inodes = %d\n", myfsstat.f_files);
  printf("free inodes = %d\n", myfsstat.f_ffree);
 }
