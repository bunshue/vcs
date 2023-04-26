 #include<stdio.h>

 main(void)
 {
  int feet;
  float tall,inch;

  printf ("How tall are you (cm):");
  scanf ("%f",&tall);
  feet= tall / 30.48;
  inch= (tall-feet*30.48)/2.54;
  printf ("Your are %d feet %.2f inch(es) tall.\n",feet,inch);
 }
