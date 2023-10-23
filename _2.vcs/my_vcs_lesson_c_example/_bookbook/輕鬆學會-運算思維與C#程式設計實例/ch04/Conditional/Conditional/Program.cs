using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Conditional
{
    class Program
    {
        static void Main(string[] args)
        {
            //變數宣告
            char math_score = 'A';
            WriteLine("Michael數學成績：");
            math_score = char.Parse(ReadLine());

            switch (math_score)
            {
                case 'A':
                    WriteLine("師長評語：非常好！真是優秀\n");
                    break;  // break的用意是跳出switch條件判斷式
                case 'B':
                    WriteLine("師長評語：也不錯，但還可以更好\n");
                    break;  // break的用意是跳出switch條件判斷式
                case 'C':
                    WriteLine("師長評語：真的要多用功\n");
                    break;  // break的用意是跳出switch條件判斷式
                default:
                    WriteLine("師長評語：不要貪玩，為自己多讀書\n");
                    break;
            }

            math_score = 'C';
            WriteLine("Jane數學成績：");
            math_score = char.Parse(ReadLine());

            switch (math_score)
            {
                case 'A':
                    WriteLine("師長評語：非常好！真是優秀\n");
                    break;  // break的用意是跳出switch條件判斷式
                case 'B':
                    WriteLine("師長評語：也不錯，但還可以更好\n");
                    break;  // break的用意是跳出switch條件判斷式
                case 'C':
                    WriteLine("師長評語：真的要多用功\n");
                    break;  // break的用意是跳出switch條件判斷式
                default:
                    WriteLine("師長評語：不要貪玩，為自己多讀書\n ");
                    break;
            }
            Read();
        }
    }
}
