using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0705
{
    class Grade
    {
        //定義靜態方法
        static void ScoreTotal(params int[] subject)
        {
            double avg = 0.0F;
            int total = 0, len = 0;
            len = subject.Length;//取得陣列長度
            for (int item = 0; item < len; item++)
            {
                //將陣列元素相加
                total += subject[item];
            }
            avg = total / (float)len;   //計算平均
            WriteLine($"總分 {total} 平均 {avg:f3}");
        }
        static void Main(string[] args)
        {
            int[] eric = { 96, 71, 85, 51, 67 };
            int[] judy = { 64, 91, 85 };
            WriteLine($"Eric 選修 {eric.Length} 科");
            //呼叫靜態方法以陣列為傳遞對象
            ScoreTotal(eric);
            WriteLine($"Judy 選修 {judy.Length} 科");
            ScoreTotal(judy);
            ReadKey();
        }
    }
}
