#include <iostream>
using namespace std;

//avg��ƪ��ŧi
double avg(int t[]);

//avg��ƪ��ϥ�
int main()
{

   int test[5];

   cout << "�п�J5�H��������ơC\n"; 

   for(int i=0; i<5; i++){
      cin >> test[i];
   }

   double ans = avg(test);

   cout << "5�H���������Ƭ�" << ans << "�C\n";

   return 0;
}

//avg��ƪ��w�q
double avg(int t[])
{
   double sum = 0;

   for(int i=0; i<5; i++){
      sum += t[i];
   }

   return sum/5;
}
