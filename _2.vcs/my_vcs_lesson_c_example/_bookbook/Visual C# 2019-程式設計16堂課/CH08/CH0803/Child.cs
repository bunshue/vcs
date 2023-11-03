using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0803
{
    class Child : Mother
    {
        public string Title { get; set; }

        //建構函式
        public Child()
        {
            Title = "Tomas";
            //關鍵字this取得父類別成員，
            this.Hair = Hair;    //使用父類別屬性
            this.Height = 172;   //設新值
        }

        //成員方法
        public void Show() => Console.WriteLine(
           $"{Title} {Surname}\n" +
           $"{Hair}, 身高 {Height}cm");
    }
}
