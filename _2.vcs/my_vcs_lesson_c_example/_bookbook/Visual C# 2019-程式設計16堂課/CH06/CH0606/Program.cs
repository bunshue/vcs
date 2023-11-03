using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0606
{
    class Program
    {
        static void Main(string[] args)
        {
            Square rect = new Square();
            Write("請輸入邊長資訊：");
            rect.length = float.Parse(ReadLine());
            WriteLine($"面積：{rect.area}");

            ReadKey();
        }
    }
}
