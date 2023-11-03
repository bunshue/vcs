using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;


namespace CH0801
{
    //Subjects為子類別，繼承了父類別School
    class Subjects : School
    {
        private int Cost { get; set; }
        public int Grade { get; set; }

        public Subjects()   //建構函式
        {
            Cost = 3_500; //學分費
            Grade = 4;    //學分數
        }

        //屬性採運算式主體定義，計算學分費
        public int Amount => Cost * Grade;

        //成員方法 -- 檢查選修人數
        public void Display(int sts)
        {
            string sign = new string('-', 30);
            WriteLine(sign);
            string st1 = "選修學生", st2 = "學分";
            string st3 = "學分費", st4 = "費用";

            if (sts < 15)
                WriteLine("法定人數不足...");
            else
            {
                WriteLine($"{st1,4} {st2} {st3} {st4}");
                Write($" {sts,7}{Grade,4} ");
                WriteLine($"{Cost,7:N0}{Amount,10:c0}");
            }
        }
    }
}
