#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   ifstream fin("test1.txt");
   if(!fin){
      cout << "�ɮ׵L�k�}�ҡC\n";
      return 1;
   }

   char str1[16];
   char str2[16];
   fin >> str1 >> str2;
   cout << "�g�J���ɮת�2�Ӧr�ꬰ�G\n";
   cout << str1 << "�C\n";
   cout << str2 << "�C\n";

   fin.close();

   return 0;
}
