using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0605
{
    class Program
    {
        static void Main(string[] args)
        {
            //建立物件並以new運算子實體化
            Student eric = new Student();

            Write("請輸入您的名字：");
            eric.Title = ReadLine();

            Write("請輸入您的年齡：");
            eric.Timeoflife = Convert.ToUInt16(ReadLine());
            eric.showInfo();

            ReadKey();//暫停螢幕
        }
    }
}
