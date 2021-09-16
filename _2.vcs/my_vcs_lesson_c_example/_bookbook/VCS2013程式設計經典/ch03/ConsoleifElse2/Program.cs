using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleifElse2
{
    class Program
    {
        static void Main(string[] args)
        {
            int age ;
            Console.Write("請輸入年齡 : ");
            age = int.Parse (Console.ReadLine());
            if (age<10 || age >20) 
                Console.WriteLine ("你的年齡是 {0} , 不是青少年仔! ",age);
            else
                Console.WriteLine("你的年齡是 {0} , 是青少年仔 !", age);
            Console.Read ();
        }
    }
}
