using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0601
{
    //定義Dog類別
    class Dog
    {
        //定義欄位-對外公開
        public string name;
        public string dogColor;
    }

    class Program
    {
        static void Main(string[] args)
        {
            //產生第一個物件並實體化
            Dog akita = new Dog();
            akita.name = "Akita Inu";
            akita.dogColor = "black";

            Write($"{akita.name} 犬，");
            WriteLine($"毛色 {akita.dogColor}");

            //產生第二個物件
            Dog bulldog = new Dog();
            bulldog.name = "Bulldog";
            bulldog.dogColor = "brown";

            Write($"{bulldog.name,9} 犬，");
            Write($"毛色 {bulldog.dogColor}");

            ReadKey();//暫停螢幕
        }
    }
}
