using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Grade
{
    class Program
    {
        static void Main(string[] args)
        {
            int score = 88;
            int level = 0;
            //巢狀if..else敘述
            WriteLine("利用if..else控制敘述判斷");
            if (score >= 60)
            {
                if (score >= 75)
                {
                    if (score >= 90)
                    {
                        WriteLine("成績" + score + " 是甲等!!");
                        level = 1;
                    }
                    else
                    {
                        WriteLine("成績" + score + " 是乙等!!");
                        level = 2;
                    }
                }
                else
                {
                    WriteLine("成績" + score + " 是丙等!!");
                    level = 3;
                }
            }
            else
                WriteLine("成績" + score + " 不及格!!");
            // switch..case敘述
            WriteLine("利用switch..case控制敘述判斷");
            switch (level)
            {
                case 1: WriteLine("成績" + score + " 是甲等!!"); break;
                case 2: WriteLine("成績" + score + " 是乙等!!"); break;
                case 3: WriteLine("成績" + score + " 是丙等!!"); break;
                default: WriteLine("成績" + score + " 是丁等!!"); break;
            }
            Read();
        }
    }
}