 #include <stdio.h>
 #include <string.h>
 #define SIZE 100
 main(void)
 {
  char s[SIZE][SIZE];
  char *line[SIZE]; 
  char *p;
  int  i,j,k;
  for (i=0;i<SIZE;i++)
     {
      printf("%d:",i+1);
      fgets(s[i],SIZE,stdin);
      if (strcmp(s[i],"q\n")==0)
           break;
      line[i]=s[i];
     }
  for (j=0; j<i-1; j++)
     for (k=j+1; k<i; k++)
         if (strcmp(line[j],line[k]) >0)
            {
             p = line[k];
             line[k] = line[j];
             line[j] = p;
            }
  printf("\nSorting...\n");
  for (j=0; j<i; j++)
     printf("%d: %s",j+1,line[j]);
 }
