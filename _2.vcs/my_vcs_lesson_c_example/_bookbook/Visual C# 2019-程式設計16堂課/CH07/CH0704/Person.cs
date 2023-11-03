using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0704
{
    class Person
    {
        //自動實作屬性
        public string Name { get; set; }
        public byte Height { get; set; }

        //定義靜態方法
        public void showInfo(Person first)
        {
            //指派屬性值做物件初始化
            first = new Person()
            { Name = "林小明", Height = 172 };
        }

        //定義靜態方法
        public void display(ref Person second)
        {
            //指派屬性值做物件初始化
            second = new Person
            { Name = "江大海", Height = 168 };
        }
    }
}
