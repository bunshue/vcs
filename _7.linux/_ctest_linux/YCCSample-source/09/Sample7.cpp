#include <iostream>
using namespace std;

//avgㄧ计
double avg(int t[]);

//avgㄧ计ㄏノ
int main()
{

   int test[5];

   cout << "叫块5代喷だ计\n"; 

   for(int i=0; i<5; i++){
      cin >> test[i];
   }

   double ans = avg(test);

   cout << "5キАだ计" << ans << "\n";

   return 0;
}

//avgㄧ计﹚竡
double avg(int t[])
{
   double sum = 0;

   for(int i=0; i<5; i++){
      sum += t[i];
   }

   return sum/5;
}
