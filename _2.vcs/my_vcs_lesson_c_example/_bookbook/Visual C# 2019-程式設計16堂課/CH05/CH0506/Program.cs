using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0506
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num1 = { 1247, 64 };
            Array.Resize(ref num1, num1.Length + 2);
            num1[2] = 113;
            num1[3] = 54;
            WriteLine("將陣列加大");
            //foreach廻圈讀取陣列
            foreach (int item in num1)
            {
                Write($"{item,4:n0} ");
            }
            int[] num2 = { 11, 5, 9, 35, 116, 92 };
            Array.Resize(ref num2, num2.Length - 3);
            WriteLine("\n將陣列變小");
            foreach (int item in num2)
            {
                Write($"{item,3:n0} ");
            }
            ReadKey();//螢幕暫停
        }
    }
}
