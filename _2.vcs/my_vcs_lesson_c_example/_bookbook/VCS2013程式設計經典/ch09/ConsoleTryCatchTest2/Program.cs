using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTryCatchTest2
{
    class Program
    {
        static void Main(string[] args)
        {
            int up, down, result;
            up = 10;
            down = 0;
            try
            {
                result = up / down;
            }
            //catch (System.DivideByZeroException ex)
            //{
            //    Console.WriteLine(" 除數不可為零...");
            //}
            catch (System.DivideByZeroException ex)
            {
                Console.WriteLine(ex.ToString());
            }
            finally
            {
                Console.WriteLine(" 已執行 finally區塊...");
            }
            Console.Read();
        }
    }
}
