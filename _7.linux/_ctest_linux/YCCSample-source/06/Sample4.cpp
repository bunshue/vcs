#include <iostream>
using namespace std;

int main()
{
   int num;
   int sum = 0;

   cout << "請問要求從1加到哪個數字為止的和呢？\n";

   cin >> num;

   for(int i=1; i<=num; i++){
      sum += i; 
   }

   cout << "從1加到" << num << "為止的和為" << sum << "。\n";

   return 0;
}
