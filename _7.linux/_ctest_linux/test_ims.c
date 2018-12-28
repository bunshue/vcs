#include <stdio.h>
int main(int argc,char* argv[])
{
	int a;	//class_index
	int b;	//TUSB_CLASS_HUB
	int c;	//new_addr
	int d;	//hub_addr

	a = 3;
	b = 9;
	c = 3;
	d = 2;
      printf("david1228: %s:%s(%d) ST tmp1 = %d tmp2 = %d tmp3 = %d tmp4 = %d\r\n", __FILE__, __func__, __LINE__,
    		  (a == b),
		  (c != 0),
		  (a == b && d != 0),
		  !(a == b && d != 0)
      );
	a = 9;
	b = 9;
	c = 3;
	d = 2;
      printf("david1228: %s:%s(%d) ST tmp1 = %d tmp2 = %d tmp3 = %d tmp4 = %d\r\n", __FILE__, __func__, __LINE__,
    		  (a == b),
		  (c != 0),
		  (a == b && d != 0),
		  !(a == b && d != 0)
      );


        return 0;
}

