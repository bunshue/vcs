using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0315
{
    class Program
    {
        //定義結構
        struct Circle
        {
            //定義成員的資料型別
            public int cX, cY;
            public double cPeriph;
            public string cColor;
        };

        static void Main(string[] args)
        {
            //產生結構成員並初始化欄位值
            Circle round;
            round.cX = 100;
            round.cY = 100;
            round.cPeriph = (Math.PI) * 5;
            round.cColor = "紅色";
            WriteLine($"圓心 X 座標：{round.cX}");
            WriteLine($"圓心 Y 座標：{round.cY}");
            WriteLine($"圓周：{round.cPeriph:f4}");
            WriteLine($"填色：{round.cColor}");

            ReadKey();

        }
    }
}
