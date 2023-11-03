using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0503
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告陣列並初始化
            int[] eric = { 78, 91, 84, 65 };
            int len = eric.Length; //取得eric陣列長度

            Write("Eric分數：");

            //for廻圈配合陣列長度，讀其元素
            for (int index = 0; index < len; index++)
            {
                Write($"{eric[index],3}");//欄寬為3
            }

            ReadKey();//螢幕暫停
        }
    }
}