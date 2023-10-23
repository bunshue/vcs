using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace 電腦時間
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            WriteLine("現在時間為：" + now);
            Read(); //暫停
        }
    }
}