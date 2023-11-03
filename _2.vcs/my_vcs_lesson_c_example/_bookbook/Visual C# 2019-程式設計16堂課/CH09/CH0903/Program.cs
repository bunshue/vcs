using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0903
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Testdiv();   //呼叫靜態方法Testdiv()
            }
            catch (Exception e)
            {
                WriteLine($"\ntoString()方法\n{e.ToString()}");
                Write($"\n屬性Message{e.Message}");
                WriteLine($"\n屬性StackTrace{e.StackTrace}");
            }
            ReadKey();
        }
        //靜態方法輸出數值
        public static void Testdiv()
        {
            for (int index = 5; index >= 0; index--)
            {
                int dob = 10;
                Write($"{dob / index} ");
            }
        }
    }
}
