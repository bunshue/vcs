#include <iostream>
using namespace std;

//�@�P�Ŷ���ƫ��AYear���ŧi
union Year{
   int ad;
   int gengo; 
};

int main()
{
   Year myyear;

   cout << "�п�J�褸�~���C\n";
   cin >> myyear.ad;

   cout << "�褸��" << myyear.ad << "�C\n";
   cout << "�����]�O" << myyear.gengo << "�C\n";

   cout << "�п�J�����C\n";
   cin >> myyear.gengo;

   cout << "������" << myyear.gengo << "�C\n";
   cout << "�褸�]�O" << myyear.ad << "�C\n";

   return 0;
}
