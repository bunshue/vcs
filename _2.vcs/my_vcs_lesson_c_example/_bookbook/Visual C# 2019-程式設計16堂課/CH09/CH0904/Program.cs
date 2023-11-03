using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0904
{
    class Program
    {
        static void Main(string[] args)
        {
            Testdiv();   //呼叫靜態方法Testdiv()
        }
        //宣告靜態方法
        public static void Testdiv()
        {
            try
            {
                for (int index = 5; index >= 0; index--)
                {
                    int dob = 10;
                    Console.Write($"{dob / index} ");
                }
            }
            finally
            {
                Console.WriteLine("在finally區塊");
            }
        }

    }
}
