using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0310
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 12, y = 24, z = 37;
            WriteLine($"右移2位 {x} >> 2, {x >> 2}");
            WriteLine($"左移2位 {y} << 2, {y << 2}");
            WriteLine("---------------------");

            //^(XOR)運算子
            bool result = (x > y) ^ (y > z);
            WriteLine($"^運算子 數值 {x} ^ {y} = {x ^ y}");
            WriteLine($"^運算子 布林 {result}");
            WriteLine("---------------------");

            //&運算子
            result = (x > y) & (y < z);
            WriteLine($"&運算子 數值 {x} & {y} = {x & y}");
            WriteLine($"&運算子 布林 = {result}");
            WriteLine("---------------------");

            //|運算子
            result = (x != y) | (z < y);
            WriteLine($"|運算子 {x} | {y} = {x | y}");
            WriteLine($"|運算子 布林 = {result}");

            ReadKey();   //螢幕暫停
        }
    }
}
