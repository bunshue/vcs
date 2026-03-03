using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0801
{
    class School   //父類別
    {
        //自動實作屬性分別以protected, private
        private string Subject { get; set; }
        protected int Room { get; set; }
        protected string Teacher { get; set; }

        public School()   //建構函式
        {
            Subject = "計算機概論";
            Room = 1205;
            Teacher = "Peter Wang";
        }

        //成員方法-顯示訊息
        public void ShowMsg()
        {
            string title = "科目", course = "教室";
            Console.WriteLine("{title,-9}{course,-6}老師");

            string sign = new string('*', 30);
            Console.WriteLine(sign);

            Console.WriteLine("{Subject} AB{Room} {Teacher}");
        }
    }
}
