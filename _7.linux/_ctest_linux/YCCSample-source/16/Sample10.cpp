#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ofstream fout("test0.txt");
   if(!fout){
      cout << "�L�k�}���ɮסC\n";
      return 1;
   }
   else
      cout  << "�ɮפw�}�ҡC\n";

   fout.close();
   cout  << "�ɮפw�����C\n";

   return 0;
}
