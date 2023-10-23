using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace Blessings
{
    class Hello
    {
        public void GoodWord(string[] s1)
        {
            for (int j=0;j<=3;j++)
                WriteLine(s1[j]);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            string[] phrase = new string[4] {
                    "天作良緣月老定", "相敬如賓夫妻健",
                    "百子千孫有孝行", "行儀天下世人鏡" };
            Hello obj = new Hello();
            obj.GoodWord(phrase);
            Read(); //暫停
        }
    }
}