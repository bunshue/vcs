using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0712
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime LoginTime, LogoffTime;
            //StayTime取得停留時間
            TimeSpan StayTime = new TimeSpan();
            string YesNo;
            int Loop1, Loop2;
            //取得目前登入的時間
            LoginTime = DateTime.Now;
            WriteLine($"登入時間：{LoginTime}");
            //模擬檔案下載
            do
            {
                WriteLine("檔案下載中...請稍待...");

                for (Loop1 = 0; Loop1 <= 200000; Loop1++)
                {
                    if (Loop1 % 8000 == 0)
                    {
                        for (Loop2 = 0; Loop2 <= 6000000; Loop2++) ;
                        Write(char.ConvertFromUtf32((int)16));
                    }
                }

                /*呼叫Char結構ConvertFromUtf32()方法
                  將指定Unicode字碼指標轉換成UTF-16編碼的字串*/
                Write(char.ConvertFromUtf32((int)10) +
                   "下載完成！是否繼續？(Y/N)");

                YesNo = ReadLine(); //取得所輸入的值

                //輸入「n」時，則顯示登出及停留時間
                if (YesNo.ToLower() == "n")
                {
                    LogoffTime = DateTime.Now;
                    WriteLine($"登出時間：{LogoffTime}");

                    /* DateTime結構的Subtract()方法計算時間差
                       時間差(StayTime) = 登出時間 - 登入時間
                       再以所得結果，換算時、分、秒   */
                    StayTime = LogoffTime.Subtract(LoginTime);
                    WriteLine($"您在此停留{StayTime.Hours,2}"
                       + $" 小時，{StayTime.Minutes} 分鐘 " +
                       $"{StayTime.Seconds} 秒");
                }
            } while (YesNo.ToLower() == "y");

            ReadKey();
        }
    }
}
