using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0412
{
    class Program
    {
        static void Main(string[] args)
        {
            ushort count = 1, total = 0;
            //計數數count, 條件式count <= 10
            while (count <= 10)
            {
                total += count;//儲存累加值
                count += 2;//控制運算式
            }
            WriteLine($"1~10累加結果 {total}");
            ReadKey();//螢幕暫停
        }
    }
}
