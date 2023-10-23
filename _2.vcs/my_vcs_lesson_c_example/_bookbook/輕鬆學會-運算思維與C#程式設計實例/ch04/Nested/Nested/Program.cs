using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Nested
{
    class Program
    {
        static void Main(string[] args)
        {
            //變數宣告
            int a = 0, b = 0;

            WriteLine("AND邏輯閘=(" + a + "," + b + ")");
            if (a == 1)
            {
                if (b == 1)
                {
                    WriteLine(a + "(AND)" + b + "=" + "1" + '\n');
                }
                else
                {
                    WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
                }
            }
            else
            {
                WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
            }

            a = 1;
            WriteLine("AND邏輯閘=(" + a + "," + b + ")");
            if (a == 1)
            {
                if (b == 1)
                {
                    WriteLine(a + "(AND)" + b + "=" + "1" + '\n');
                }
                else
                {
                    WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
                }
            }
            else
            {
                WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
            }

            a = 1;
            b = 1;
            WriteLine("AND邏輯閘=(" + a + "," + b + ")");
            if (a == 1)
            {
                if (b == 1)
                {
                    WriteLine(a + "(AND)" + b + "=" + "1" + '\n');
                }
                else
                {
                    WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
                }
            }
            else
            {
                WriteLine(a + "(AND)" + b + "=" + "0" + '\n');
            }
            Read();
        }
    }
}
