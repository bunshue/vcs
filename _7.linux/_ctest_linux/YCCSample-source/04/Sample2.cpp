#include <iostream>
using namespace std;

int main()
{
   int num1 = 2;
   int num2 = 3;
   int sum = num1+num2;

   cout << "�ܼ�num1���ȬO" << num1 << "�C\n";
   cout << "�ܼ�num2���ȬO" << num2 << "�C\n";
   cout << "num1+num2���ȬO" << sum << "�C\n";

   num1 = num1+1;

   cout << "�ܼ�num1���ȥ[1��O" << num1 << "�C\n";

   return 0;
}
