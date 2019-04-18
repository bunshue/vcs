#include <stdio.h>

int gcd(int m, int n);

int main(int argc,char* argv[])
{
	int a;
	int b;
        int ret;
	a = 1234;
	b = 5678;
	ret = gcd(a, b);
	printf("gcd(%d, %d) = %d\n", a, b, ret);
	a = 18;
	b = 150;
	ret = gcd(a, b);
	printf("gcd(%d, %d) = %d\n", a, b, ret);
	a = 256;
	b = 72;
	ret = gcd(a, b);
	printf("gcd(%d, %d) = %d\n", a, b, ret);
	a = 1234;
	b = 1234;
	ret = gcd(a, b);
	printf("gcd(%d, %d) = %d\n", a, b, ret);
	
        return 0;
}

int gcd(int a, int b)
{
	int temp = 1;
	while(temp != 0)
	{
		temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}



