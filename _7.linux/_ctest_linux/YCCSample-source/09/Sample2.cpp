#include <iostream>
using namespace std;

int main()
{
   const int num = 5;
   int test[num];

   cout << num <<"�п�J5�Ӿǥͪ����ơC\n";
   for(int i=0; i<num; i++){
      cin >> test[i];
   }

   for(int j=0; j<num; j++){
      cout << j+1 << "�����ǥͤ��Ƭ�" << test[j] << "�C\n";
   }

   return 0;
}
