 #include <stdio.h>
 main(void)
 {
  int key;
        printf("key in a number between 0..999:");
        scanf("%d",&key);
        if ( key <1000 && key >=0 )
           if ( key <100)
              if ( key < 10 )
                printf("1 digit");
              else
                printf("2 digits");
           else
             printf("3 digits");
        else
          printf("Not allowed!");
 }
