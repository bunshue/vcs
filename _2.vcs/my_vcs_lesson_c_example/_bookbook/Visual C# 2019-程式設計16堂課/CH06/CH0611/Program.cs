using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0611
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 1;//計數用
            while (count <= 3)
            {
                Console.Write("請輸入名稱：");
                string name = Console.ReadLine();

                Console.Write("輸入分數 -> ");
                Console.Write("數學：");
                uint math = Convert.ToUInt32(Console.ReadLine());
                Console.Write("英文：");
                uint eng = Convert.ToUInt32(Console.ReadLine());
                Console.Write("國文：");
                uint chin = Convert.ToUInt32(Console.ReadLine());

                //直接以類別來呼叫靜態方法Total()、Average()
                uint score = Student.Total(math, eng, chin);
                float avg = Student.Average("平均分數", score);

                Console.WriteLine("{name} " + "總分 {score}，平均 {avg:f3}");
                count++;
            }

            Console.ReadKey();
        }
    }

    class Student
    {
        //第一個靜態方法-計算總分
        public static uint Total(uint a, uint b, uint c)
        {
            uint sum = a + b + c;//總分
            return sum;//回傳加總結果         
        }
        //第二個靜態方法-算平均分數
        public static float Average(string word, uint number)
        {
            float result = number / 3.0F;//平均
            return result;
        }
    }
}
