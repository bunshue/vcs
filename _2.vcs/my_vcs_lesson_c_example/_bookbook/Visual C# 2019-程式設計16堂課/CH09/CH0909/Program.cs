using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0909
{
    class Program
    {
        static void Main(string[] args)
        {
            Write("請輸入體重：");
            int wt = Convert.ToInt32(ReadLine());
            Write("請輸入身高：");
            int ht = Convert.ToInt32(ReadLine());
            try
            {
                WeightHigh test = new WeightHigh();
                WriteLine(test.testWeight(wt, ht));
            }
            catch (WeightHigh e)
            {
                WriteLine(e.Message);
            }
            ReadKey();
        }
    }
}
