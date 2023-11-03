using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0305
{
    class Program
    {
        static void Main(string[] args)
        {
            //將指定ASCII數值以型別char轉為字元
            int num1 = 69;
            //呼叫Convert類別的ToChar()轉為字元
            char chE = Convert.ToChar(69);
            WriteLine($"ASCII {num1} 是字元 {chE}");

            //將字元以型別int轉為ASCII值
            char chX = 'X';
            //直接以int將字元轉為整數
            int num2 = (int)chX;
            WriteLine($"字元 {chX} 的ASCII = {num2}");

            //直接以unicode做設定
            char key = '\u0308';
            WriteLine($"字元 {key}");

            ReadKey();//螢幕暫停
        }
    }
}