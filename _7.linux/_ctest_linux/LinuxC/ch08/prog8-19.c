 #include <stdio.h>
 void showerror();
 
 int main(int argc, char *argv[])
 {
 if (argc!=2 || argv[1][0]!='/')
   {
     showerror();
     return 1;
    }
 switch (argv[1][1])
      {
       case 'a':
       case 'A':
                printf("[format...]\n");
                break;
       case 'b':
       case 'B':
                printf("[copy...]\n");
                break;
       case 'c':
       case 'C':
                printf("[delete...]\n");
                break;
       case 'd':
       case 'D':
                printf("bye-bye!\n");
                break;
       default:
	        showerror();
                return 2;
      }
    return 0;
 }

 void showerror(void)
 {
   printf("Usage: Prog8-19 /[a][b][c][d]\n");
 }
