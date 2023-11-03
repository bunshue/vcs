using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0809
{

    class Automobile : Car   //子類別
    {
        private float engine;   //排氣量
        public string Hue { get; set; }

        //定義建構函式– base()方法取得父類別屬性
        public Automobile(string carName, string tint,
              float engine) : base(carName)
        {
            Hue = tint;
            this.engine = engine;
        }

        //覆寫父類別所定義的唯讀屬性，將建構函式取得的參數值回傳
        public override float Pde
        { get { return engine; } }

        //覆寫父類別方法 - 要加關鍵字override
        public override void Display() =>
           Console.WriteLine($"{Name,7} {Hue}," +
              $" 排氣量 {Pde:f2}L");
    }
}
