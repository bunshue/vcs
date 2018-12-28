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
		for(i = 0; i < W; i++)
		{
			if(j < 1.5*(H / 8))	 // Top lines	//tmp0
			{
				//          tmp1
				if ((i < (1.5 * (H / 8) - j)) || (i > ((W - 1.5 * (H / 8)) - 1 + j)))
				{
					//xil_printf("+");
					//surface_1[j * W + i] = ABGR2COLOR(0x7f, 0x33, 0x33, 0x33);		//OSD 100% black
					//surface_1[j * W + i] = 0xff000000;
					//surface_1[j * W + i] = 0x6789abcd;
					printf("X");
				}
				else
				{
					printf(" ");
				}
			}
			else if(j > (1.5 * (H / 8 ) - 1))	 // Bottom lines	//tmp3
			{	// Bottom lines
				if((i < (j + 1.5 * (H >> 3) - H) ) || i > ((W - (1.5 * (H >> 3)-(H - j))) -1 ))
				{
					//xil_printf("-");
					//surface_1[j * W + i] = ABGR2COLOR(0x7f, 0x44, 0x44, 0x44);	//OSD 100% black
					//surface_1[j * W + i] = 0xff000000;
					//surface_1[j * W + i] = 0x6789abcd;
					printf("x");
				}
				else
				{
					printf(" ");
				}
			}
		}
		printf("\n");
	}
	printf("\n");



        return 0;
}

