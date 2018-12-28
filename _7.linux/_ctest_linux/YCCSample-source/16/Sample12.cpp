#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
   ofstream fout("test2.txt");
   if(!fout){
      cout << "檔案無法開啟。\n";
      return 1;
   }

   const int num = 5;
   int test[num];
   cout << num <<"請輸入學生的成績。\n";
   for(int i=0; i<num; i++){
      cin >> test[i];
   }

   for(int j=0; j<num; j++){
      fout << "No." << j+1 << setw(5) << test[j] << '\n';
   }

   fout.close();

   return 0;
}
