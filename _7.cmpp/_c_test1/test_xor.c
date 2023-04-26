#include <stdio.h>
int main(int argc,char* argv[])
{
        int i;
	char name[] = "lion-mouse.";
	char xor1;
	char xor2;
	char key = 0x87;
	printf("size of name is %ld\n",sizeof(name));
	for(i = 0; i< sizeof(name); i++)
	{
		xor1 = name[i] ^ key;
		xor2 = xor1 ^ key;
		printf("%d\t%c\t0x%02x\t0x%02x\t0x%02x\n", i, name[i], name[i], xor1, xor2);
	}
        return 0;
}

