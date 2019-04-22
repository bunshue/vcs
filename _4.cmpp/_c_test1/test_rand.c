#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	int a,b;
	//srand(time(NULL));
	srand(100);
	for(a=1;a<=5;a++)
	{
		b= rand();
		printf("%d\n",b);
	}

	printf("%ld\n",time(NULL));

	return 0;
}



