#include <iostream>
using namespace std;

int main()
{
   const int num = 5;
   int test[num];

   cout << num <<"�п�J�ǥͪ����ơC\n";
   for(int i=0; i<num; i++){
      cin >> test[i];
   }

   for(int s=0; s<num-1; s++){
      for(int t=s+1; t<num; t++){
         if(test[t] > test[s]){
            int tmp = test[t];
            test[t] = test[s];
            test[s] = tmp;
            
         }
      }
   }

   for(int j=0; j<num; j++){
      cout << j+1 << "���ǥͪ����Ƭ�" << test[j] << "�C\n";
   }

   return 0;
}
