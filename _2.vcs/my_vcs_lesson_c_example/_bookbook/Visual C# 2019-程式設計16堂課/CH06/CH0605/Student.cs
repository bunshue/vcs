using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0605
{
    class Student
    {
        //宣告欄位-name, age
        private string name;
        private ushort age;

        //自動實作屬性，取得欄位name, age值
        public string Title { get; set; }
        public ushort Timeoflife { get; set; }

        //定義方法，採運算式主體來輸出屬性值
        public void showInfo() =>
           WriteLine($"Hi, {Title}, 年齡 {Timeoflife}");
    }
}