using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace StrAdd
{
    class Program
    {
        static void Main(string[] args)
        {
            string A, B, C, D;
            A = "I";
            B = " Love";
            C = " My";
            D = " Family";

            A = A + B + C + D;  //將所有字串變數內容結合在一起
            WriteLine(A); //變數顯示出來
            Read(); //暫停
        }
    }
}
