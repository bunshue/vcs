#include <iostream> 
using namespace std;

//��ƽd��
template <class T>
T maxt(T x, T y)
{
   if(x > y)
      return x;
   else
      return y;
}

//��ƽd�����ϥ�
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
