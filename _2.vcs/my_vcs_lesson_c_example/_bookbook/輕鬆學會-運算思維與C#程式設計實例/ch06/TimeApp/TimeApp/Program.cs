using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace TimeApp
{
    class Program
    {
        static void Main(string[] args)
        {
            const int MAX1 = 3000000;
            const int MAX2 = 6000000;
            const int NUMBER = 8000;
            DateTime login;
            DateTime logout;
            TimeSpan period = new TimeSpan();
            int outer, inner;
            login = DateTime.Now; //登入時間
            WriteLine("登入時間：{0}", login);
            WriteLine("檔案開始下載！");
            for (outer = 0; outer <= MAX1; outer++)
            {
                if (outer % NUMBER == 0)
                {
                    for (inner = 0; inner <= MAX2; inner++) ;
                    Write("#");
                }
            }
            Write(char.ConvertFromUtf32((int)10));
            logout = DateTime.Now;
            WriteLine();
            WriteLine("登出時間：{0}", logout);
            period = logout.Subtract(login);
            WriteLine();
            WriteLine("檔案下載過程共花了 " + period.Hours
              + "小時" + period.Minutes + "分鐘"
              + period.Seconds + "秒");
            Read();
        }
    }
}