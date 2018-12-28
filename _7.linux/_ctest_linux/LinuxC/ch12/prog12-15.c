 #include <unistd.h>
 #include <stdio.h>
 main(void)
 {
  char pathname[100];
  printf("Please input directory path:");
  scanf("%s", pathname); 
  chdir(pathname);

  printf("We will make a new directory in %s\n", pathname);
  mkdir("newdir", 00600);
  
  chdir("newdir");
  getcwd(pathname, 100);
  printf("Now we are in directory %s\n", pathname);  
 }
