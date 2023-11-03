using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0611
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 1;//計數用
            while (count <= 3)
            {
                Write("請輸入名稱：");
                string name = ReadLine();

                Write("輸入分數 -> ");
                Write("數學：");
                uint math = Convert.ToUInt32(ReadLine());
                Write("英文：");
                uint eng = Convert.ToUInt32(ReadLine());
                Write("國文：");
                uint chin = Convert.ToUInt32(ReadLine());

                //直接以類別來呼叫靜態方法Total()、Average()
                uint score = Student.Total(math, eng, chin);
                float avg = Student.Average("平均分數", score);

                WriteLine($"{name} " +
                   $"總分 {score}，平均 {avg:f3}");
                count++;
            }

            ReadKey();
        }
    }
}
