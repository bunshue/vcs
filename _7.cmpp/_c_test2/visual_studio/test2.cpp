#include <iostream>
using namespace std;
struct Car{
	int num;
	double gas;
};
void show1(Car c);		//�o�Ө�ƬO�Hstruct��ƫ��A�ӧ@���޼�
void show2(Car* pC);	//�o�Ө�ƬO����Vstruct��ƫ��A�����з�@�޼�

int main()
{
	int lion[5]={20,23,26,16,19};
	int i;
	printf("lion�}�C�����e��%d %d %d %d %d\n",lion[0],lion[1],lion[2],lion[3],lion[4]);
	for(i=0;i<5;i++)
		printf("lion[%d]���Ȭ� 0x%X\t��}�� 0x%X\n",i,lion[i],&lion[i]);

	for(i=0;i<5;i++)
		printf("lion+%d���Ȭ� 0x%X (�O�@�Ӧ�})\t���V�����e�Ȭ� %d	//(*(lion+%d))\n",i,lion+i,*(lion+i),i);

	//�r�����
	char str1[]="This is a lion-mouse";
	cout << str1 << "\n";
	//�Ϋ��гB�z�r��
	char* str2="This is a lion";	//�ϥ�""�H�r��N���Ъ�l��
	cout << str2 << "\n";			//��X�r��
	str2="This is a mouse";			//�ܧ���Щҫ��V���r��
	cout << str2 << "\n";			//��X�r��
	printf("���G�O%s\t//�G�i�H���ܦr�ꤺ�e\n\n",str2);		//��X�r��

	//��struct���޼ƨӥ�
	Car car1 = {0,0.0};
	car1.num=1234;
	car1.gas=20.5;
	show1(car1);	//�ǰestruct���Acar1����
	show2(&car1);	//�ǰestruct���Acar1����}


	return 0;
}

void show1(Car c)
{
	printf("�T�����P�O%d\t�T�o�e�q�O%f\n",c.num,c.gas);
}

void show2(Car* pC)
{
	printf("�T�����P�O%d\t�T�o�e�q�O%f\n",pC->num,pC->gas);
}
