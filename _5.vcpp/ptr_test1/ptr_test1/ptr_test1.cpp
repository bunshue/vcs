// ptr_test1.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
//#include <iostream>

int _tmain(int argc, _TCHAR* argv[])
{
	char Li;
	char Chen;
	char Huang;
	char Wang;
	char Ma;
	char Lin;
	char Xie;
	char Song;
	char Zhu;

	Li = 15;
	Chen = 18;
	Huang = 7;
	Wang = 9;
	Ma = 16;
	Lin = 23;
	Xie = 11;
	Song = 2;
	Zhu = 33;

	getchar();//或system("pause");

	return 0;
}


/*
int _tmain(int argc, _TCHAR* argv[])
{
	int i;
	int* p;
	int aaa[10];

	p = &aaa[0];
	printf("p1 = %p\n", p);
	p = aaa;
	printf("p2 = %p\n", p);

	for(i = 0; i < 10; i++)
	{
		aaa[i] = i * i;
		printf("i = %d, aaa[%d] = %d, addr of aaa[%d] is %p\n", i, i, aaa[i], i, &aaa[i]);
	}
	for(i = 0; i < 10; i++)
	{
		printf("index %d, addr is %p, value is %d\n", i, p+i, *(p+i));
	}
	getchar();//或system("pause");

	return 0;
}
*/
