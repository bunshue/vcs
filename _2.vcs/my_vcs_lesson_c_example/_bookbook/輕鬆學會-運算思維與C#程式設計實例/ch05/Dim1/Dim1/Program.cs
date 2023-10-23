using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Dim1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] Test = new int[3];
            //列印陣列的預設初值
           WriteLine("===================");
           WriteLine("Test[{0}]= {1} ", 0, Test[0]);
           WriteLine("Test[{0}]= {1} ", 1, Test[1]);
           WriteLine("Test[{0}]= {1} ", 2, Test[2]);

            //宣告陣陣時一併指定初值
           WriteLine("===================");
            Test = new int[] { 52, 68, 77, 69, 23 };
           WriteLine("Test[{0}]= {1} ", 0, Test[0]);
           WriteLine("Test[{0}]= {1} ", 1, Test[1]);
           WriteLine("Test[{0}]= {1} ", 2, Test[2]);
           WriteLine("Test[{0}]= {1} ", 3, Test[3]);
           WriteLine("Test[{0}]= {1} ", 4, Test[4]);
           ReadLine();
        }
    }
}
