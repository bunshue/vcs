using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTenary
{
    class Program
    {
        static void Main(string[] args)
        {
            double netIncome;
            int taxRate;

            Console.Write("請輸入全年綜合所得淨額(單位:萬元) : ");
            netIncome = double.Parse(Console.ReadLine());

            if (netIncome > 0)
            {
                taxRate = (netIncome <= 50 ? 5 : (netIncome <= 113 ? 13 : (netIncome <= 226 ? 20 : (netIncome <= 423 ? 30 : 40))));
                Console.WriteLine("\n === {0} 萬元 的所得稅率為 {1}% .", netIncome.ToString ("#,#.0000"), taxRate);
            }
            else
                Console.WriteLine("\n === 全年所得淨額為負 ! 不用繳稅 ... ");

            Console.Read(); 
        }
    }
}
