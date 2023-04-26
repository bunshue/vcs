#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ofstream fout("test0.txt");
   if(!fout){
      cout << "無法開啟檔案。\n";
      return 1;
   }
   else
      cout  << "檔案已開啟。\n";

   fout.close();
   cout  << "檔案已關閉。\n";

   return 0;
}
