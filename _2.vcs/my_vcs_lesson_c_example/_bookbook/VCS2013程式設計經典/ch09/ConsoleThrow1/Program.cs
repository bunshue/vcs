using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleThrow1
{
    class Program
    {
        private static void KeyinScore(out int score)
        {
            Console.Write("輸入成績( 0 - 100 ) :  ");
            score = int.Parse(Console.ReadLine());
            if (score <= 0 || score >= 100)
            {
                throw new ArgumentOutOfRangeException();
            }
            else
                Console.WriteLine("\n輸入的成績合於限定範圍! 進入系統 ...");
        }

        static void Main(string[] args)
        {
            int score;
            while (true)
            {
                try
                {
                    KeyinScore(out score);
                    break;
                }
                catch (ArgumentOutOfRangeException ex)
                {
                    Console.WriteLine("不合理成績\n");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("其他種錯誤\n");
                }
            }
            Console.Read();
        }
    }
}
