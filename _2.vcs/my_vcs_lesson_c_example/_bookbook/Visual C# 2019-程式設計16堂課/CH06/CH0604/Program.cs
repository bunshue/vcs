using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0604
{
    class Program
    {
        static void Main(string[] args)
        {
            //new運算子實體化圓類別的物件round
            Circle round = new Circle();
            //輸入半徑計算圓面積
            Write("請輸入半徑值：");
            round.Radius = double.Parse(ReadLine());
            //輸出格式-F4，表示含有4位小數
            WriteLine($"面積：{round.Space:F4}");
            //輸入圓面積反推算半徑值
            Write("請輸入面積值：");
            round.Space = double.Parse(ReadLine());
            WriteLine($"半徑：{round.Radius:F4}");

            ReadKey();//暫停螢幕
        }
    }
}
