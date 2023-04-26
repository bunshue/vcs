#include <stdio.h>
#include <stdlib.h>

#define ROW 3
#define COL 8

int main()
{
    int i, j;
    int gray[ROW][COL];

    printf("assign value\n");
    for(j = 0; j < ROW; j++)
    {
        for(i = 0; i < COL; i++)
        {
            gray[j][i] = i*10 + j;
        }
    }

    printf("print value\n");
    for(j = 0; j < ROW; j++)
    {
        for(i = 0; i < COL; i++)
        {
            printf("%02d  ", gray[j][i]);
        }
        printf("\n");
    }
    return 0;
}
