#include <iostream>
using namespace std;
struct Car{
	int num;
	double gas;
};
void show1(Car c);		//這個函數是以struct資料型態來作為引數
void show2(Car* pC);	//這個函數是把指向struct資料型態的指標當作引數

int main()
{
	int lion[5]={20,23,26,16,19};
	int i;
	printf("lion陣列的內容為%d %d %d %d %d\n",lion[0],lion[1],lion[2],lion[3],lion[4]);
	for(i=0;i<5;i++)
		printf("lion[%d]的值為 0x%X\t位址為 0x%X\n",i,lion[i],&lion[i]);

	for(i=0;i<5;i++)
		printf("lion+%d的值為 0x%X (是一個位址)\t指向的內容值為 %d	//(*(lion+%d))\n",i,lion+i,*(lion+i),i);

	//字串測試
	char str1[]="This is a lion-mouse";
	cout << str1 << "\n";
	//用指標處理字串
	char* str2="This is a lion";	//使用""以字串將指標初始化
	cout << str2 << "\n";			//輸出字串
	str2="This is a mouse";			//變更指標所指向的字串
	cout << str2 << "\n";			//輸出字串
	printf("結果是%s\t//故可以改變字串內容\n\n",str2);		//輸出字串

	//把struct當做引數來用
	Car car1 = {0,0.0};
	car1.num=1234;
	car1.gas=20.5;
	show1(car1);	//傳送struct型態car1的值
	show2(&car1);	//傳送struct型態car1的位址


	return 0;
}

void show1(Car c)
{
	printf("汽車車牌是%d\t汽油容量是%f\n",c.num,c.gas);
}

void show2(Car* pC)
{
	printf("汽車車牌是%d\t汽油容量是%f\n",pC->num,pC->gas);
}
