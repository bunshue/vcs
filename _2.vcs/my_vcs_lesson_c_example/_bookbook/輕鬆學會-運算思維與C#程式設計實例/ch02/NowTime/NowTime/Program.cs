using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace NowTime
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime current_time = DateTime.Now;
            WriteLine("目前執行本程式的電腦時間為： " + current_time);
            Read(); //暫停
        }
    }
}
