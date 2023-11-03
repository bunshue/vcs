using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0709
{
    class Program
    {
        static void Main(string[] args)
        {
            //產生物件，呼叫成員方法並加入引數
            Store coffee = new Store();
            coffee.Beverage("珈琲", 5, 112);
            Store greentea = new Store();
            greentea.Beverage("綠茶", 15, "大杯", 75);
            Store blacktea = new Store();
            greentea.Beverage("紅茶", 7, "一般", 45);
            Console.ReadKey();
        }
    }
}
