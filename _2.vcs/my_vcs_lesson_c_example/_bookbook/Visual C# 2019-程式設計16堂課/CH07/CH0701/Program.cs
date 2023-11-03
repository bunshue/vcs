using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0701
{
    class Program
    {
        static void Main(string[] args)
        {
            float math, chin, eng;
            Write("輸入名稱：");
            string student = ReadLine();
            Write("數學--> ");
            math = Convert.ToSingle(ReadLine());
            Write("國文--> ");
            chin = Convert.ToSingle(ReadLine());
            Write("英文--> ");
            eng = Convert.ToSingle(ReadLine());

            //呼叫靜態方法--同一類別直接呼叫名稱
            float score = Score_total(math, chin, eng);
            WriteLine($"Hi! {student}, 成績 {score:f4}");
            ReadKey();
        }

        //定義靜態方法
        public static float Score_total(
              float a, float b, float c)
        {
            float outcome = a * 0.4F + b * 0.3F + c * 0.3F;
            return outcome;
        }
    }
}
