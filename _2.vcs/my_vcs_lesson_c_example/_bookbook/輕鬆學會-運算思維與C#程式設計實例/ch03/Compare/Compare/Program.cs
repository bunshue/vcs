using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Compare
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2;
            bool compare;
            num1 = 999;
            num2 = 998;
            compare = (num1 == num2);  //判斷兩數是否相等
            WriteLine("第1個數字=999");
            WriteLine("第2個數字=998");
            WriteLine("兩數比較後是否相等=" + compare); //將result1顯示出來
            Read(); //暫停
        }
    }
}
