#include <iostream>
using namespace std;

int main()
{
   const int num = 5;
   int test[num];

   cout << num <<"請輸入5個學生的分數。\n";
   for(int i=0; i<num; i++){
      cin >> test[i];
   }

   for(int j=0; j<num; j++){
      cout << j+1 << "號的學生分數為" << test[j] << "。\n";
   }

   return 0;
}
