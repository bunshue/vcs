#include <iostream>
using namespace std;

//max��ƪ��ŧi
int max(int x, int y);
double max(double x, double y);

int main()
{
   int a, b;
   double da, db;

   cout << "�п�J2�Ӿ�ơG\n";
   cin >> a >> b;

   cout << "�п�J2�Ӥp�ơG\n";
   cin >> da >> db;

   int ans1 = max(a, b);
   double ans2 = max(da, db);

   cout << "��ƭȪ��̤j�Ȭ�" << ans1 << "�C\n";
   cout << "�p�ƭȪ��̤j�Ȭ�" << ans2 << "�C\n";

   return 0;
}

//max�]int���A�^��ƪ��w�q
int max(int x, int y)
{
   if (x > y)
      return x;
   else 
      return y;
}

//max�]double���A�^��ƪ��w�q
double max(double x, double y)
{
   if (x > y)
      return x;
   else 
      return y;
}
