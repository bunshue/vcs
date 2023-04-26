#include<iostream>
using namespace std;

int main()
{
   int num;
   int* pT;

   cout << "請問要輸入幾個人的測驗成績？\n";

   cin >> num;

   pT = new int[num];

   cout << "請輸入所有人的成績。\n";

   for(int i=0; i<num; i++){
      cin >> pT[i];
   }

   for(int j=0; j<num; j++){
      cout << "第" << j+1 << "個人的成績是" << pT[j] << "。\n";
   }

   delete[] pT;

   return 0;
}
