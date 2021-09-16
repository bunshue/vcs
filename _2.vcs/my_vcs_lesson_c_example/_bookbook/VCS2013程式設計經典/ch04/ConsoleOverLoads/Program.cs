using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleOverLoads
{
    class Program
    {
        static int sum(int x, int y)		// 傳回兩數相加
        {
            return (x + y);
        }
        static int sum(int x, int y, int z) 	// 傳回三數相加
        {
            return (x + y + z);
        }
        static string sum(string x, string y)  // 傳回兩個字串合併結果
        {
            return (x + y);
        }
        // 傳回三個字串合併結果
        static string sum(string x, string y, string z)
        {
            return (x + y + z);
        }
        static void Main(string[] args)
        {
            Console.WriteLine("sum(1,2)={0}", sum(1, 2));
            Console.WriteLine("sum(1,2,3)={0}", sum(1, 2, 3));
            Console.WriteLine("sum(\"a\", \"b\")={0}", sum("a", "b"));
            Console.WriteLine
             ("sum(\"a\", \"b\", \"c\")={0}", sum("a", "b", "c"));
            Console.Read();
        }
    }

}
