using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0702
{
    class PassingByValue
    {
        //定義成員方法
        private int Arithmetic(int first, int last,
              int diff)
        {
            //nonce暫存變數，item取得項數值
            int nonce = 0, item;

            //檢查傳入的首項是否大於末項，首項小於末項則予以置換
            if (first < last)
            {
                nonce = first;
                first = last;
                last = nonce;
            }
            item = (first - last) / diff + 1;  //計算項數

            //計算差數和，回傳計算結果
            return (item * (first + last)) / 2;
        }

        static void Main(string[] args)
        {
            //建立物件，才能呼叫成員方法Arithmetic()
            PassingByValue duplicate = new PassingByValue();

            //輸入各項參數
            WriteLine("***求取等差級數和***");
            Write("輸入起始值(首項)：");
            int begin = Convert.ToInt32(ReadLine());
            Write("輸入最後值(末項)：");
            int stop = Convert.ToInt32(ReadLine());
            Write("輸入差值：");
            int diff = int.Parse(ReadLine());

            //呼叫方法成員
            int total = duplicate.Arithmetic(
               begin, stop, diff);

            //輸出等差級數和
            WriteLine($"數值 {begin} ~ {stop}" +
               $" 差數和：{total:N0}");

            ReadKey();
        }
    }
}