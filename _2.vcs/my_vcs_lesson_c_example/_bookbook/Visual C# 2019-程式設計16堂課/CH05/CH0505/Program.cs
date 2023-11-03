using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0505
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告陣列並初始化
            int[] number = { 124, 65, 3314, 81, 92, 65 };

            //foreach廻圈讀取陣列元素
            foreach (int item in number)
            {
                Write($"{item,4} ");
            }
            WriteLine();//換行

            int first = Array.IndexOf(number, 65);
            WriteLine($"從前方找65，索引值 {first}");

            int tail = Array.LastIndexOf(number, 65);
            WriteLine($"從末端找65，索引值 {tail}");

            int unknown = Array.IndexOf(number, 33);
            WriteLine($"從前方找33，索引值 {unknown}");

            ReadKey();//螢幕暫停
        }
    }
}
