#include <iostream>
using namespace std;

//maxㄧ计
int max(int x, int y);
double max(double x, double y);

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

//maxint篈ㄧ计﹚竡
int max(int x, int y)
{
   if (x > y)
      return x;
   else 
      return y;
}

//maxdouble篈ㄧ计﹚竡
double max(double x, double y)
{
   if (x > y)
      return x;
   else 
      return y;
}
