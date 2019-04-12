#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 10

int main()
{
	int i;
	int j;
	int A[N] = {0};
	int temp;

	//srand(time(NULL));
	srand(100);
	for(i=0; i < N; i++)
	{
		A[i] = rand() % 100;
	}


	printf("Before Bubble sort, A = \t");
	for(i=0; i < N; i++)
	{
		printf("%02d ", A[i]);
	}
	printf("\n");

	for(i=0; i < (N - 1); i++)
	{
		for(j = (i + 1); j < N; j++)
		{
			if(A[i] > A[j])
			{
				temp = A[i];
				A[i] = A[j];
				A[j] = temp;
			}

		}
	}


	printf("After  Bubble sort, A = \t");
	for(i=0; i < 10; i++)
	{
		printf("%02d ", A[i]);
	}
	printf("\n");

	return 0;
}



