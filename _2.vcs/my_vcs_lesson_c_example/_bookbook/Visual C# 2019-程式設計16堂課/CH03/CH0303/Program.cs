using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0303
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告浮點數值，以float型別處理
            float a = 1f, b = 0f, c = -1f, d = -0f, f = 3.0f;
            float e = 99999999999999f, g = 1e5f;
            //使用WriteLine()方法配合字串插補
            WriteLine($"a = {a:f3}, b = {b}");
            WriteLine($"c = {c}, d = {d}");
            WriteLine($"e = {e}, f = {f}, g = {g}");
            //將數值做簡單運算
            WriteLine($"a/b = {a / b}, c/b = {c / b}");
            WriteLine($"c/d = {c / d}");
            WriteLine($"e*e = {e * e}, e*e*e*e = {e * e * e * e}");
            WriteLine($"a/e = {a / e:N}");
            WriteLine($"c/f = {c / f:N8}");
            //讓螢幕暫停
            ReadKey();
        }
    }
}
