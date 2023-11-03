using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0603
{
    class Program
    {
        static void Main(string[] args)
        {
            //產生第一個物件並實體化
            Dog akita = new Dog();
            //經由屬性，設dogColor欄位的值
            Write("請輸入犬類毛色：");
            akita.Tinct = ReadLine();
            akita.show("秋田");
            ReadKey();//暫停螢幕
        }
    }
}
