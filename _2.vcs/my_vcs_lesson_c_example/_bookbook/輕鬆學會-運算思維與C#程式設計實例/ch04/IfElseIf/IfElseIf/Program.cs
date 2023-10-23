using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace IfElseIf
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("請輸入季節代號：");
            int season_no = int.Parse(ReadLine());

            if (season_no >= 1 && season_no <= 3)
                WriteLine("現在是第一季");
            else if (season_no > 3 && season_no <= 6)
                WriteLine("現在是第二季");
            else if (season_no > 6 && season_no <= 9)
                WriteLine("現在是第三季");
            else
                WriteLine("現在是第四季");
            Read();
        }
    }
}
