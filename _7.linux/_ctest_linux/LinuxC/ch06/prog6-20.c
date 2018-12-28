 #include <stdio.h>
 main(void)
 {
  goto label3;

  label1:
     printf ("printf in label1\n");
     goto label4;

  label2:
     printf ("printf in label2\n");
     goto label1;
     
  label3:
     printf ("printf in label3\n");
     goto label2;
     
  label4:
     printf ("printf in label4\n");
 }
     
