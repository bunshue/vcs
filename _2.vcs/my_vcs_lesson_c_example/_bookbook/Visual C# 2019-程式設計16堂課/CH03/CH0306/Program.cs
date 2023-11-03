using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0306
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告變數並設初始值
            ushort x = 15, y = 27;
            ushort a = 24, b = 92;

            //被除數b要轉成float型別
            float total = a / (float)b;
            float total2 = (float)a / b;
            float result = (x + y) / (float)(a * b / x);

            //變數直接運算再輸出結果
            WriteLine($"相加 = {x + y}, 相減 = {x - y}");
            WriteLine($"相乘 = {a * b:N0}");

            WriteLine($"相除 = {total:f6}");
            WriteLine($"相除 = {total2:f6}");

            WriteLine($"取餘數 = {b % a}");
            WriteLine($"運算式 = {result:f6}");

            ReadKey();
        }
    }
}
