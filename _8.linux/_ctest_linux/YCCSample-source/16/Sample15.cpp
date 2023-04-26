#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
   if(argc!=2){
      cout << "參數的數值不同。\n";
      return 1;
}

   ifstream fin(argv[1]);
   if(!fin){
      cout << "無法開啟檔案。\n";
      return 1;
   }

   char ch;
   while(!fin.eof()){
      fin.get(ch);
      cout.put(ch);
}

   fin.close();

   return 0;
}
