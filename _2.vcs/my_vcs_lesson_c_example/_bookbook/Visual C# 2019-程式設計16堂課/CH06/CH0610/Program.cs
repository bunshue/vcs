using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//using static System.Console;

namespace CH0610
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("沒有物件，汽車 {Motor.Number} 輛");
            Motor sienta = new Motor("Sienta", 1.5F);
            Motor yaris = new Motor("Yaris", 1.8F);
            Motor hybrid = new Motor("Hybrid", 2.0F);
            Console.ReadKey();
        }
    }

    class Motor
    {
        //靜態類別欄位-記錄物件
        public static int Number { get; private set; }

        //自動實作屬性：Name, 排氣量Pde
        public string Name { get; set; }
        public float Pde { get; set; }

        //建構函式-含有兩個參數
        public Motor(string title, float engine)
        {
            Name = title;
            Pde = engine;
            Number++;   //建立物件就計數
            Console.WriteLine("第 {Number} 輛車-{Name,6}，排氣量{Pde:f1} L");
        }
        ~Motor() { }   //解構函式
    }
}
