#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc,char* argv[])
{
	printf("Math function test\n");
	float input;
	char filename[]="math_test_result.txt";
	FILE *fp;
	printf("%s\n",filename);
	if ((fp = fopen(filename,"w")) < 0)
	{
		printf("File %s opened fails... exit\n",filename);
		return 0;
	}
	else
	{
		printf("File %s opened OK...\n",filename);
	}
	fprintf(fp,"%%Math test, saving sin wave data.\n");
	
	for(input=0;input<3.5;input+=0.01)
	{
		//fprintf(fp,"sin(%f)=%f\n",input,sin(input));
		fprintf(fp,"%f\t%f\n",input,sin(input));
		//printf("cos(%f)=%f\n",input,cos(input));
		//printf("tan(%f)=%f\n",input,tan(input));
	}
	fclose(fp);
	
	return 0;
}


