using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace 最小數
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a1 = new int[4];
            Write("輸入第1數：");
            a1[0] = int.Parse(ReadLine());
            Write("輸入第2數：");
            a1[1] = int.Parse(ReadLine());
            Write("輸入第2數：");
            a1[2] = int.Parse(ReadLine());
            Write("輸入第4數：");
            a1[3] = int.Parse(ReadLine());
            Array.Sort(a1);
            Write("最小值為：{0}", a1[0]);
            Read();
        }
    }
}
