#include <iostream>
#include <string>
using namespace std;

int main()
{
   char str0[20];
   char str1[10];
   char str2[10];

   strcpy(str1,"Hello");
   strcpy(str2,"Goodbye");
   strcpy(str0,str1);
   strcat(str0,str2);

   cout << "陣列str1是" << str1 << "。\n"; 
   cout << "陣列str2是" << str2 << "。\n"; 

   cout << "連結起來就變成了" << str0 << "。\n"; 

   return 0;
}
