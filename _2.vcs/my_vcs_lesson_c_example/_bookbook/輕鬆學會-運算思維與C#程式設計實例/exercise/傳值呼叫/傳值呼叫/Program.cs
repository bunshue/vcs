using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace 傳值呼叫
{
    class Program
    {
        static int Area(int intL, int intW, int intH)
        {
            return intL * intW * intH;
        }

        static void Main(string[] args)
        {
            int volume;
            int length, width, height;
            Write("請輸入長方體的長度：");
            length = int.Parse(ReadLine());
            Write("請輸入長方體的寬度：");
            width = int.Parse(ReadLine());
            Write("請輸入長方體的高度：");
            height = int.Parse(ReadLine());
            volume = Area(length, width, height);
            Write("物體的體積為：{0}", volume);
            Read();
        }
    }
}