#include <iostream>
using namespace std;

int main()
{
   int num;
   int sum = 0;

   cout << "�аݭn�D�q1�[����ӼƦr����M�O�H\n";

   cin >> num;

   for(int i=1; i<=num; i++){
      sum += i; 
   }

   cout << "�q1�[��" << num << "����M��" << sum << "�C\n";

   return 0;
}
