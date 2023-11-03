using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0602
{
    class Program
    {
        static void Main(string[] args)
        {
            //產生第一個物件並實體化
            Dog akita = new Dog();

            //呼叫方法，設欄位name的值
            Write($"{akita.show("Akita Inu")} 犬，");

            //呼叫方法，設dogColor欄位的值
            akita.display("black");
            //呼叫方法，取得dogColor欄位的值並回傳
            WriteLine($"毛色 {akita.displayInfo()}");

            //產生第二個物件並呼叫方法來設定相關欄位的值
            Dog bulldog = new Dog();
            Write(bulldog.show("Bulldog") + " 犬，");

            bulldog.display("brown");
            Write($"毛色 {bulldog.displayInfo()}");

            ReadKey();//暫停螢幕
        }
    }
}
