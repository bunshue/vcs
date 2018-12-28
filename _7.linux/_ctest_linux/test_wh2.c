#include <stdio.h>

//#define LAYER1_WIDTH	1216
//#define LAYER1_HEIGHT	912
#define LAYER1_WIDTH	120
#define LAYER1_HEIGHT	40


int main(int argc,char* argv[])
{

	int i = 0;
	int j = 0;
	int W = LAYER1_WIDTH;
	int H = LAYER1_HEIGHT;

	printf("\n\rlayer1_add_corners W = %d H = %d\r\n", W, H);


	printf("tmp0 = %d\r\n", (int)((H / 8)*3/2));

	printf("tmp1 = %d tmp2 = %d\r\n", (int)((H / 8) * 3 / 2 - j), (int)((W - (H / 8) * 3 / 2) - 1 + j));
	printf("tmp3 = %d\r\n", (int)(1.5 * (H / 8 ) - 1));
	printf("tmp4 = %d tmp5 = %d\r\n", (int)(j + (H / 8) * 3 / 2 - H), (int)(W - ((H / 8 ) * 3 / 2-(H - j)) -1 ));


	// Draw transparency required on layer 1
	for(j = 0; j < H; j++)
	{
		printf("%2d\t", j);
		if(j < H / 8)
		{
			for(i = 0; i < W; i++)
			{
				if((i < W / 8) || (i > W * 7 / 8))
					printf("+");
				else
					printf(" ");
			}

		}
		else if(j > H * 7 / 8)
		{
			for(i = 0; i < W; i++)
			{
				if((i < W / 8) || (i > W * 7 / 8))
					printf("-");
				else
					printf(" ");
			}
		}
		else
		{
			for(i = 0; i < W; i++)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	printf("\n");



        return 0;
}

