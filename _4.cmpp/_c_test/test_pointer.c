#include <stdio.h>      /* puts, printf */

int main(int argc,char* argv[])
{
	int i;
	char *wday[]={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
	for(i = 0;i<7; i++)
	{
		printf("%d\t%s\n", i, wday[i]);
	
	}

	return 0;
}




