using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0709
{
    class Store
    {
        public string Size { get; set; } //空量
        public ushort Cups { get; set; } //杯數     
        public string Drink { get; set; }//飲料
        public uint Total { get; set; }  //合計金額
                                         //方法多載，無任何參數
        public void Beverage()
        {
            WriteLine("沒有選取任何飲料");
        }
        //方法多載，3個參數
        public void Beverage(string name, ushort teacup,
              uint price)
        {
            Drink = name;
            Cups = teacup;
            Total = teacup * price;
            WriteLine($"{Drink} {Cups}杯，計 {Total:c0}");
        }
        //方法多載，4個參數
        public void Beverage(string name, ushort teacup,
              string volume, uint price)
        {
            Drink = name;
            Cups = teacup;
            //判斷容量
            if (volume == "大杯")
                Total = teacup * price;
            else
                Total = teacup * price;
            WriteLine($"{Drink} {volume} {Cups}，" +
               $"計 {Total:c0}");
        }
    }
}
