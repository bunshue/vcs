using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0302
{
    class Program
    {
        static void Main(string[] args)
        {
            //1坪 = 3.30579平方公尺，宣告為常數
            const float levelGrd = 3.30579F;

            //房子有27.5坪

            float square = 27.5F;

            //計算坪數並輸出
            double area = levelGrd * square;
            Console.WriteLine($"{square}坪 = {area:f4}平方公尺");

            //讓螢幕暫停
            Console.ReadKey();
        }
    }
}
