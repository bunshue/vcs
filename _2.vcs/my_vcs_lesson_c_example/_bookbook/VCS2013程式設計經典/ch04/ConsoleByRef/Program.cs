using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleByRef
{
    class Program
    {
        private static void CallRef(ref int x, ref int y)
        {
            int z;
            x = 20;
            y = 30;
            Console.WriteLine("\n方法內 交換前\t\t：x= {0}   y={1} ", x, y);
            z = x;  //透過第三個變數來做x,y值作互換
            x = y;
            y = z;
            Console.WriteLine("\n方法內 交換後\t\t：x= {0}   y={1} ", x, y);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("\n  **** Call By Reference 參考呼叫 **** \n");
            int a = 10;
            int b = 12;
            Console.WriteLine("\n呼叫敘述 未進入方法前\t：a= {0}  b={1}", a, b);
            CallRef(ref a, ref b);
            Console.WriteLine("\n呼叫敘述 離開方法回原處\t：a= {0}  b={1}", a, b);
            Console.Read();
        }
    }
}
