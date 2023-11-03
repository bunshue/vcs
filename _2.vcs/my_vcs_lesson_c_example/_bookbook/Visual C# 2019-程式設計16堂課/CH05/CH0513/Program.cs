using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0513
{
    class Program
    {
        static void Main(string[] args)
        {
            //建立StringBuilder物件
            StringBuilder word = new StringBuilder();
            string source = "I made my song a blue coat.";
            string w2 = "Out of old mythologies.";
            string w3 = "Covered with embroideries.";
            WriteLine($"{source} 長度 {source.Length}");
            WriteLine($"{w2,27} 長度 {w2.Length}");
            WriteLine($"{w3,27} 長度 {w3.Length}");
            WriteLine($"預設容量：{word.Capacity}");
            //Append()方法加字串source
            word.Append(source);
            Write("加入字串1，");
            WriteLine($"長度：{word.Length}, " +
               $"容量：{word.Capacity}");
            word.AppendLine("\t");
            word.AppendLine(w2);
            Write("加入字串2，");
            WriteLine($"長度：{word.Length}, 容量：{word.Capacity}");

            //Remove()方法移除blue字串
            string text = "blue "; //欲移除字串

            //取得欲刪除字串的索引編號
            int index = word.ToString().IndexOf(text);
            if (index >= 0)
                word.Remove(index, text.Length);
            WriteLine($"字串 -> {word}");

            //取代部份內容: Replace()方法
            word.Replace("I", "We");
            int index2 = word.ToString().IndexOf("Out");
            word.Insert(index2, w3);
            WriteLine($"插入字串 -> {word}");
            Write($"長度：{word.Length}, 容量：{word.Capacity}");

            ReadKey(); //螢幕暫停
        }
    }
}
