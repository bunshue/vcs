#include<iostream>
using namespace std;

int main()
{
   int num;
   int* pT;

   cout << "�аݭn��J�X�ӤH�����禨�Z�H\n";

   cin >> num;

   pT = new int[num];

   cout << "�п�J�Ҧ��H�����Z�C\n";

   for(int i=0; i<num; i++){
      cin >> pT[i];
   }

   for(int j=0; j<num; j++){
      cout << "��" << j+1 << "�ӤH�����Z�O" << pT[j] << "�C\n";
   }

   delete[] pT;

   return 0;
}
