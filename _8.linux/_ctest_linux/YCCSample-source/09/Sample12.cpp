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

   cout << "�}�Cstr1�O" << str1 << "�C\n"; 
   cout << "�}�Cstr2�O" << str2 << "�C\n"; 

   cout << "�s���_�ӴN�ܦ��F" << str0 << "�C\n"; 

   return 0;
}
