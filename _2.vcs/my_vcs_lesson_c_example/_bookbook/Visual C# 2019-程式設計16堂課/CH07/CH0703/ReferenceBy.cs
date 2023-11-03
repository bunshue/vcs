using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0703
{
    class ReferenceBy
    {
        //定義不對外公開的靜態方法做傳值呼叫
        static int Num_power(int number) =>
           //呼叫Math類別的Pow()方法指定乘冪數
           number = (int)Math.Pow(number, 2);
        //使用傳址呼叫-使用「運算式主體定義」
        static int Power_ref(ref int figure) =>
           figure = (int)Math.Pow(figure, 2);

        static void Main(string[] args)
        {
            //建立rand物件，呼叫Next()方法指定隨機數10~50之間
            Random rand = new Random();
            int num_any = rand.Next(10, 50);
            WriteLine($"隨機數 {num_any}");
            if (num_any < 10 || num_any > 50)
                Write("超出範圍，不做計算");
            else
            {
                //Passing By Value
                int result = Num_power(num_any);
                Write("Passing By Value: ");
                WriteLine($"隨機值 {num_any} 結果 {result}\n");
                //Passing By Reference
                int outcome = Power_ref(ref num_any);
                WriteLine("Passing By Reference: ");
                WriteLine($"隨機值 {num_any} 結果 {outcome}");
            }

            ReadKey();
        }
    }
}
