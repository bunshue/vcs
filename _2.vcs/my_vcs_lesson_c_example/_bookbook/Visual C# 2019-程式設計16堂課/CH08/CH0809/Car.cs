using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0809
{
    abstract class Car   //定義為抽象類別
    {
        private string carName;   //私有欄位
        public abstract float Pde { get; } //抽象屬性

        //建構函式
        public Car(string title)
        { Name = title; }

        //屬性Name須取得建構函式的參數值
        protected string Name
        {
            get { return carName; }
            set { carName = value; }
        }

        //抽象方法
        public abstract void Display();
    }
}
