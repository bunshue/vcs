using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0804
{
    class Worker : Person   //子類別
    {
        //利用base()方法呼叫基底類別的建構函式來使用
        public Worker(string Name, int pay)
              : base(Name, pay) { }

        public void hireTime()
        {
            DateTime startDate = DateTime.Today;
            Console.WriteLine("雇用日期：{0}",
               startDate.ToShortDateString());
        }
    }
}
