#include <iostream> 
using namespace std;

//ㄧ计絛セ
template <class T>
T maxt(T x, T y)
{
   if(x > y)
      return x;
   else
      return y;
}

//ㄧ计絛セㄏノ
int main()
{
   int a, b;
   double da, db;

   cout << "叫块2俱计\n";
   cin >> a >> b;

   cout << "叫块2计\n"; 
   cin >> da >> db;

   int ans1 = max(a, b);
   double ans2 = max(da, db);

   cout << "俱计程" << ans1 << "\n";
   cout << "计程" << ans2 << "\n";

   return 0;
}
