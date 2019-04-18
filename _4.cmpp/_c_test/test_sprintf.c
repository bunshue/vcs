#include <stdio.h>
int main(int argc,char* argv[])
{
	char str[10];
	int num = 961406;

	sprintf(str, "%d", num);
	printf("str = %s\n", str);

	return 0;

}

