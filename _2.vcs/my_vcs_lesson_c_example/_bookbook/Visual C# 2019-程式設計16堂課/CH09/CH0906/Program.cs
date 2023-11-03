using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH0906
{
    class Program
    {
        public static void Testdiv()
        {
            try
            {
                for (int index = 5; index >= 0; index--)
                {
                    int dob = 10;
                    Write($"{dob / index} ");
                }
            }
            catch (IOException)
            {
                WriteLine("抓到IO例外");
            }
            finally
            {
                WriteLine("\n位於Testdiv()方法的finally區塊");
            }
        }

        static void Main(string[] args)
        {
            try
            {
                Testdiv();
            }
            catch (ArithmeticException)
            {
                WriteLine("抓到Arithmetic例外");
            }
            finally
            {
                WriteLine("結束於主程式的finally區塊");
            }
            ReadLine();
        }
    }
}
