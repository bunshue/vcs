#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ofstream fout("test1.txt");
   if(!fout){
      cout << "檔案無法開啟。\n";
      return 1;
   }
   else
      cout  << "寫入至檔案。\n";

   fout << "Hello!\n";
   fout << "Goodbye!\n";

   fout.close();

   cout << "檔案已關閉。\n";
   return 0;
}
