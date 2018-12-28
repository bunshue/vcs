#include <iostream>
using namespace std;

//共同空間資料型態Year的宣告
union Year{
   int ad;
   int gengo; 
};

int main()
{
   Year myyear;

   cout << "請輸入西元年份。\n";
   cin >> myyear.ad;

   cout << "西元為" << myyear.ad << "。\n";
   cout << "元號也是" << myyear.gengo << "。\n";

   cout << "請輸入元號。\n";
   cin >> myyear.gengo;

   cout << "元號為" << myyear.gengo << "。\n";
   cout << "西元也是" << myyear.ad << "。\n";

   return 0;
}
