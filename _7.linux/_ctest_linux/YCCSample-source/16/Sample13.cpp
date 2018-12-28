#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ifstream fin("test1.txt");
   if(!fin){
      cout << "檔案無法開啟。\n";
      return 1;
   }

   char str1[16];
   char str2[16];
   fin >> str1 >> str2;
   cout << "寫入至檔案的2個字串為：\n";
   cout << str1 << "。\n";
   cout << str2 << "。\n";

   fin.close();

   return 0;
}
