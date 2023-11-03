using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0316
{
    class Program
    {
        //定義結構
        struct Circle
        {
            public float cRadius;
            public string cColor;
        }
        //定義結構並呼叫另一個結構為其型別
        struct Wheel
        {
            //呼叫Circl結構
            public Circle round;
            public string usage;
        };

        static void Main(string[] args)
        {
            Wheel tyre;   //產生結構成員
                          //產生欄位值
            tyre.round.cRadius = 50;
            tyre.round.cColor = "黑色";
            tyre.usage = "汽車";
            WriteLine($"輪胎半徑：{tyre.round.cRadius}");
            WriteLine($"輪胎顏色：{tyre.round.cColor}");
            WriteLine($"輪胎用途：{tyre.usage}");
            ReadKey();
        }
    }

}
