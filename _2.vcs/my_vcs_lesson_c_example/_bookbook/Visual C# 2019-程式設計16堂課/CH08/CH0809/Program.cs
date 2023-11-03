using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0809
{
    class Program
    {
        static void Main(string[] args)
        {
            Car[] cars = {   //初始化物件
            new Automobile("Hybrid", "裴冷藍", 2.0F),
            new Automobile("Vios", "亮麗白", 1.6F),
            new Automobile("Sunny", "魅力紅", 1.49F)
         };
            //foreach廻圈讀取物件並呼叫方法
            foreach (Car item in cars)
                item.Display();
            Console.ReadKey();
        }
    }
}
