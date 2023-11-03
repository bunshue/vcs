using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0905
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] index = new int[4] { 2, 4, 6, 8 };
            try
            {
                Write("輸入一個數字：");
                int x = Convert.ToInt32(ReadLine());

                for (int count = 0; count < index.Length; count++)
                {
                    Write($"{index[count] / x} ");
                }
                index[5] = x;
            }
            catch (ArithmeticException)
            {
                WriteLine("\n發生Arithmetic例外");
            }
            catch (IndexOutOfRangeException)
            {
                WriteLine("\n超出了陣列索引的例外");
            }
            finally
            {
                WriteLine("結束於主程式的finally區塊");
            }
            ReadKey();
        }
    }
}
