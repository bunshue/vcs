using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace 四則運算
{
    class Program
    {
        static void Main(string[] args)
        {
            bool result1;
            result1 = (98 + 21) - 18 / 2 >= 58 + 25 / 5;
            //顯示計算結果
            WriteLine("(98 + 21) - 18 / 2 >= 58 + 25 / 5的運算結果為：" + result1);
            Read(); //暫停
        }
    }
}
