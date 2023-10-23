using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Constructor
{
    class SuperClass : Object //System.Object為所有類別之父類別
    {
        public SuperClass() //建構函式,預設是使用base()初始函式
        {
            WriteLine("這是在 SuperClass 內的建構函式所輸出文字");
        }
    }

    class ChildClass1 : SuperClass
    {
        //不顯性定義,使用預設的建構函式    
    }

    class ChildClass2 : ChildClass1
    {
        public ChildClass2()
          : base()
        {
            WriteLine("這是由在 ChildClass2 內的建構函式所輸出文字");
        }

        //this()等於ChildClass2.ChildClass2()
        public ChildClass2(string s)
          : this()
        {
            WriteLine("輸出字串: " + s);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("===================================");
            WriteLine("new ChildClass1() 的輸出結果：");
            new ChildClass1();

            WriteLine("===================================");
            WriteLine("new ChildClass2() 的輸出結果：");
            new ChildClass2();

            WriteLine("===================================");
            WriteLine("new ChildClass2(一個參數) 的輸出結果");
            new ChildClass2("傳入一個參數的建構函式");
            Read();
        }
    }
}
