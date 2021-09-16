using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmptyClass
{
    class MyFirstClass     //定義類別，名稱為MyFirstClass
    {

    }

    class Program
    {
        static void Main(string[] args)
        {
           Console.WriteLine("建立一個 MyFirstClass 物件 A ...");
           MyFirstClass A = new MyFirstClass();
           /* 
           上述一行敘述也可以改成如下兩行
           MyFirstClass A ;     // 宣告A物件為MyFirstClass類別
           A=new MyFirstClass();// 使用new敘述建立A物件為MyFirstClass類別
           */
            Console.WriteLine("A 物件建立完成 !!");
            Console.WriteLine("請按 Enter 結束 ...");
            Console.Read();
        }
    }
}
