using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace StringBuilderApp
{
    class Program
    {
        static void Main(string[] args)
        {
            //建立StringBuilder物件
            StringBuilder strb = new StringBuilder();
            WriteLine("預設容量：{0}", strb.Capacity);

            //使用 Append()方法附加字串
            strb.Append(
                "Never put off until tomorrow what you can do today.");
            WriteLine("字串長度：{0}，總容量：{1}",
                strb.Length, strb.Capacity);
            strb.AppendLine("\n");
            WriteLine("在字串尾端加入換行字元後");
            WriteLine("字串長度：{0}，總容量：{1}",
            strb.Length, strb.Capacity);

            strb.AppendLine(
                "It is a wonderful English proverb.");
            WriteLine("在字串尾端加入另一個字串後: ");
            WriteLine("字串長度：{0}，總容量：{1}",
            strb.Length, strb.Capacity);

            WriteLine("原來字串 -- {0}", strb);

            //Remove()方法
            string text = "English";//欲移除字串
                                    //取得欲刪除字串的索引編號
            int index = strb.ToString().IndexOf(text);
            if (index >= 0)
                strb.Remove(index, text.Length);
            WriteLine("變更後字串 -- {0}", strb);
            Read();
        }
    }
}
