#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ofstream fout("test1.txt");
   if(!fout){
      cout << "�ɮ׵L�k�}�ҡC\n";
      return 1;
   }
   else
      cout  << "�g�J���ɮסC\n";

   fout << "Hello!\n";
   fout << "Goodbye!\n";

   fout.close();

   cout << "�ɮפw�����C\n";
   return 0;
}
