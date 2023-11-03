using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0708
{
    class Worker
    {
        public string name { get; set; }   //自動實作屬性

        Worker(string title)   //建構函式
        {
            name = title;
        }

        //定義方法-4個參數，預設值為0
        void Salary(uint pay = 0, float tax = 0.0F,
           uint insur1 = 0, uint insur2 = 0)
        {
            uint outcome = 0; //儲存計算結果

            if (pay <= 25_200)
                outcome = pay;
            else if (pay <= 28_800)
                outcome = pay - insur1 - insur2;
            else
            {
                tax = pay * 0.08F;
                outcome = pay - (uint)tax - insur1 - insur2;
            }
            WriteLine($"{name,-11}, 實薪 {outcome:c0}");
        }
        static void Main(string[] args)
        {
            Worker wk1 = new Worker("Amanda");
            wk1.Salary(25_000);   //只有一個引數

            Worker wk2 = new Worker("Peter Pan");
            wk2.Salary(29_500, 529, 355);

            Worker wk3 = new Worker("Charles");
            wk3.Salary(35_400, 0.08F, 700, 469);

            ReadKey();
        }
    }
}
