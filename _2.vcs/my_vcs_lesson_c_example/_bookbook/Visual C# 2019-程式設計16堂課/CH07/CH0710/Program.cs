using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0710
{
    class Program
    {
        //產生委派物件-有兩個參數
        delegate int ExpressNum(int one, int two);

        //靜態方法-運算式主體定義
        static int CalcNumber(int n1, int n2) =>
           n1 * n2;
        static void Main(string[] args)
        {
            int total;
            Write("輸入第一個數值：");
            int num1 = int.Parse(ReadLine());
            Write("輸入第二個數值：");
            int num2 = int.Parse(ReadLine());

            //產生委派物件，呼叫Lamdba運算式         
            ExpressNum result = (a, b) => a + b;
            //傳遞引數給委派
            total = result(num1, num2);
            WriteLine($"{num1} + {num2} = {total}");

            result = (a, b) => a - b;
            total = result(num1, num2);
            WriteLine($"{num1} - {num2} = {total}");

            //呼叫靜態方法
            total = CalcNumber(num1, num2);
            WriteLine($"{num1} * {num2} = {total}");
            ReadKey();
        }
    }
}
