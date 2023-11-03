using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0602
{
    class Dog
    {
        //定義欄位-不對外公開
        private string name;
        private string dogColor;

        //定義方法存取欄位name，return敘述回傳結果
        public string show(string title)
        {
            name = title;
            return name;
        }

        //定義方法-設定欄位dogColor的值
        public void display(string clor)
        {
            dogColor = clor;
        }

        //定義方法-回傳欄位dogColor的值
        public string displayInfo()
        {
            return dogColor;
        }
    }
}
