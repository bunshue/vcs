using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleEvent1
{
    delegate void DangerEvent(int vSpeed);	// 宣告delegate型別

    class Car
    {
        private int _speed;
        public event DangerEvent Danger;		// 宣告事件
        public int Speed		// 定義 Speed 屬性
        {
            get
            {
                return _speed;
            }
            set
            {
                if (value > 200)
                {
                    if (Danger != null) Danger(value);	// 啟動事件
                }
                _speed = value;
            }
        }
    }
    class Program
    {
        static void TooFast(int vSpeed)
        {
            Console.WriteLine("你的目前的速度是 {0},超過 200，請減速 !!!", vSpeed);
        }

        static void Main(string[] args)
        {
            Car Benz = new Car();
            // 指定 Danger 事件由 TooFast 方法來處理
            Benz.Danger += new DangerEvent(TooFast);
            Benz.Speed = 300;
            Console.Read();
        }
    }
}
