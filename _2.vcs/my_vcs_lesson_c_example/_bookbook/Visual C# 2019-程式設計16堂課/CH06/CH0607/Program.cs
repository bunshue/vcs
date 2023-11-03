using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0607
{
    class Program
    {
        static void Main(string[] args)
        {
            Write("請輸入名字：");
            string na = ReadLine();
            Write("請輸入月薪：");
            float payment = Convert.ToSingle(ReadLine());

            //建立一個含有參數的Student物件
            Employee ep1 = new Employee(na, payment);
            ep1.Taxmoney();//呼叫方法成員
            ReadKey();
        }
    }
}
