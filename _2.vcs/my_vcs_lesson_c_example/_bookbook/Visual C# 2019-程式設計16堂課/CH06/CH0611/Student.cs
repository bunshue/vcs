using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0611
{
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
