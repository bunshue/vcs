#include <stdio.h>
#include <stdlib.h>

//int* getRandom(int* r, int len)  //same
int* getRandom(int r[], int len)
{
    int i;

    //srand((unsigned)time(NULL));
    srand(123);

    for ( i = 0; i < len; i++)
    {
        r[i] = rand()%101;
        printf("%3d ",r[i]);
    }
    printf("\n");
    return r;
}


#define LEN 20

int main()
{
    int *p;
    int i;
    int arr[LEN];
    int len = LEN;

    p = &arr[0];

    for (i = 0; i < LEN; i++)
    {
        arr[i] = 13;
    }


    for (i = 0; i < LEN; i++)
    {
        printf("%3d ", *(p + i));
    }
    printf("\n");

    p = getRandom(arr, len);

    for (i = 0; i < LEN; i++)
    {
        printf("%3d ", *(p + i));
    }
    printf("\n");

    for (i = 0; i < LEN; i++)
    {
        printf("%3d ",arr[i]);
    }
    printf("\n");


    return 0;
}



