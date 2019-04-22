#include <stdio.h>
#include <string.h>
int main(int argc,char* argv[])
{
        int i;

	printf("Compiled time: %s %s\n\r", __DATE__, __TIME__);
	printf("%s:%s(%d)\n\r\n\r",__FILE__,__func__,__LINE__);

	char str[20];
	//const char * const txt1 = __DATE__;
	const char * const txt2 = __TIME__;

	memset(str, '\0', 20);

	printf("string is %s\n", str);
	for(i = 0; i < 20; i++)
	{
		printf("str[%2d] = %02x\n\r", i, str[i]);
	}

	sprintf(str, "%s", txt2);

	printf("string is %s\n", str);
	for(i = 0; i < 20; i++)
	{
		printf("str[%2d] = %02x\n\r", i, str[i]);
	}


        return 0;
}

