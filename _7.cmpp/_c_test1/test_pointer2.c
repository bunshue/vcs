#include <stdio.h>
int main()
{
	int i;
	char a[3][6]={"hello", "world"};
	char *p;
	p = (char*)a;

	for(i = 0;i<5;i++)
	{
		printf("%c\n", *(p+i) ); //输出h
	}

	printf("%c\n", *p ); //输出h
	return 0;
}



