#include <iostream>
using namespace std;

int main()
{
   int res;
   char ans;

   cout << "請問要選哪條路線？\n";
   cout << "請輸入整數。\n";

   cin >> res;

   ans = (res==1) ? 'A' : 'B'; 

   cout << ans << "路線已選擇。\n";

   return 0;
}
