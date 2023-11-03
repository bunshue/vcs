using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0609
{
    class Dinner
    {
        //自動實作屬性並設初值
        public uint price { get; set; } = 0;
        public uint foodprice { get; set; } = 350;
        public uint tea { get; set; } = 125;
        public uint savoury { get; set; } = 50;

        public string mainfood { get; set; }
        public string teadrink { get; set; }
        public string appetizing { get; set; }

        //建構函式只有一個參數
        public Dinner(string food)
        {
            mainfood = food;
            price = foodprice;
        }

        //建構函式只有二個參數
        public Dinner(string food, string drink)
        {
            mainfood = food;
            teadrink = drink;
            price = foodprice + tea;
        }

        //建構函式只有三個參數
        public Dinner(string food,
              string drink, string salad)
        {
            mainfood = food;
            teadrink = drink;
            appetizing = salad;
            price = foodprice + tea + savoury;
        }

        //定義方法輸出費用
        public void showInfo()
        {
            Write($"{mainfood,-5} " +
               $"{teadrink,-2} {appetizing,4}");
            WriteLine($" 費用 {price,4:c0}");
        }
    }
}
