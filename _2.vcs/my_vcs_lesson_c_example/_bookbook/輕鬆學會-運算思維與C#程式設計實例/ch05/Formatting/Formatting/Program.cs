using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Formatting
{
    class Program
    {
        static void Main(string[] args)
        {
            string str1, str2, str3;
            str1 = "四維";
            str2 = "八德";
            str3 = "五倫";
            WriteLine("校訓 1: {0} 校訓 2: {1} 校訓 3: {2}！", str1, str2, str3);
            Read(); //暫停
        }
    }
}
