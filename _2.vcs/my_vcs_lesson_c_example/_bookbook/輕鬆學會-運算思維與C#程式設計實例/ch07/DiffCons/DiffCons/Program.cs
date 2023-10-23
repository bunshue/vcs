using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace DiffCons
{
    class Data
    {
        //資料成員
        protected int field1;
        protected float field2;
        protected string field3;

        //多載建構函式
        public Data() { }

        public Data(int i) : this(i, 0, "") { }

        public Data(int i, float f) : this(i, f, "") { }

        public Data(int i, float f, string s)
        {
            this.field1 = i;
            this.field2 = f;
            this.field3 = s;
        }

        //將資料成員輸出到螢幕上
        public void dump()
        {
            Console.WriteLine("成員1 ={0}\n成員2 ={1}\n成員3 ={2}\n",
                              field1, field2, field3);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //各種不同的建構函式
            Data memberX = new Data();
            Data memberY = new Data(158);
            Data memberZ = new Data(25, 28.7f, "股價的最低點與最高點");

            //列印資料成員
            memberX.dump();
            memberY.dump();
            memberZ.dump();
            Console.Read();
        }
    }
}
