using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleOutput
{
    class Program
    {
        private static void CallOut(out int x, out int y)
        {
            int z;
            x = 20;
            y = 30;
            Console.WriteLine("\n方法內 交換前\t\t\t: x= {0}  y={1} ", x, y);
            z = x;
            x = y;
            y = z;
            Console.WriteLine("\n方法內 交換後\t\t\t: x= {0}  y={1} ", x, y);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("\n  **** Call Out 傳出參數 **** \n");
            int a, b;
            Console.WriteLine("\n呼叫敘述 未進入方法前  a 和 b 未設定初值 ");
            CallOut(out a, out b);
            Console.WriteLine("\n呼叫敘述 離開方法回主程式\t: a= {0}  b={1}", a, b);
            Console.Read();
        }
    }
}
