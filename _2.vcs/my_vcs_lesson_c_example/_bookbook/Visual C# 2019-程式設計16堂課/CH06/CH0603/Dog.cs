using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0603
{
    class Dog
    {
        //定義欄位-不對外公開
        private string name;
        private string dogColor;

        //設定屬性來存取欄位dogColor
        public string Tinct
        {
            get { return dogColor; }
            set { dogColor = value; }
        }

        //定義方法存取欄位name，void表示不回傳其值
        public void show(string title)
        {
            name = title;//取得輸入名稱
            WriteLine($"{name} 犬，毛色 {Tinct}");
        }
    }
}
