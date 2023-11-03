using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別


namespace CH0416
{
    class Program
    {
        //雙層for廻圈的應用
        static void Main(string[] args)
        {
            byte k, j;//計數器
                      //外層for廻圈提供列數
            for (k = 1; k <= 10; k++)
            {
                //外層for廻圈提供欄位，依控制運算式輸出*字元
                for (j = 1; j <= k; j++)
                {
                    Write("*");
                }
                WriteLine();//換行
            }

            ReadKey();//螢幕暫停
        }
    }
}
