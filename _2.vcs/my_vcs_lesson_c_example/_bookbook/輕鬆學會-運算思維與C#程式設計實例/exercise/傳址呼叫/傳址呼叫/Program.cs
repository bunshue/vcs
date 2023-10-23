using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace 傳址呼叫
{
    class Program
    {
        static void test(ref int a1, ref int a2)
        {
            a1 *= 100;
            a2 *= 100;
        }
        static void Main(string[] args)
        {
            int num1, num2;
           Write("請輸入第一筆數字：");
            num1 = int.Parse(Console.ReadLine());
           Write("請輸入第二筆數字：");
            num2 = int.Parse(Console.ReadLine());
            test(ref num1, ref num2);
           WriteLine("第一個數字經傳址呼叫後，其100倍的值為{0}", num1);
           WriteLine("第二個數字經傳址呼叫後，其100倍的值為{0}", num2);
           Read();
        }
    }
}
