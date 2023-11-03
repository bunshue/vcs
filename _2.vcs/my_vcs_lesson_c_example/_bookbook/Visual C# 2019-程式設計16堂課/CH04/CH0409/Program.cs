using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0409
{
    class Program
    {
        //以for廻圈將數值加總
        static void Main(string[] args)
        {
            int k, total = 0, number = 10;
            //for迴圈每執行一次自動加1
            for (k = 1; k <= number; k++)
            {
                total += k;//儲存累加值
                WriteLine($"{k,2}, total = {total,3}");
            }

            ReadKey();//螢幕暫停
        }
    }
}
