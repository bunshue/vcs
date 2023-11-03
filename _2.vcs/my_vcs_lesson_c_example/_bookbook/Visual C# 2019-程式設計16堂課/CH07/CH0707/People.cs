using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0707
{
    class People
    {
        //定義靜態方法-名稱、生日、身高、性別
        static void showInfo(string name, DateTime birth,
           ushort height, bool sex_is)
        {
            TimeSpan diff;   //取得時間間隔
                             //取得目前的日期
            DateTime atonce = DateTime.Today;
            //今天的日期減去生日，再以屬性Days換算天數
            diff = atonce.Subtract(birth);
            int diff_day = diff.Days;
            //Console.WriteLine(diff_day);
            //換算年齡
            int age = diff_day / 365;
            string sex = string.Empty;   //空字串
                                         //使用條件運算子 ? : 以true表示男性
            sex = (sex_is == true) ? "帥哥" : "美女";
            WriteLine($"{sex}! {name}");
            WriteLine($"年齡 {age} 身高 {height}cm");
        }

        //主程式
        static void Main(string[] args)
        {
            ushort ht1 = 175, ht2 = 155;
            string boy = "Peter Pan", girl = "Nikki Swango";
            //設定生日的年、月、日
            DateTime bth1 = new DateTime(1996, 5, 12);
            DateTime bth2 = new DateTime(1993, 12, 15);

            //呼叫靜態方法，具名指定引數
            showInfo(height: ht1, name: boy,
               sex_is: true, birth: bth1);

            showInfo(birth: bth2, name: girl,
               height: ht2, sex_is: false);

            ReadKey();
        }
    }
}
