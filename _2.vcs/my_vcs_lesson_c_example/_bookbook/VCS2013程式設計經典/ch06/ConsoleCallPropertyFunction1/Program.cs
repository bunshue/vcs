using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleCallPropertyFunction1
{
    class Car   // 定義Car類別
	{
        // 宣告_speed私有變數用來存放車子的速度值
		private int _speed = 0;
        // 定義Speed速度屬性
		public int Speed
		{
			get
			{
				return _speed;  // 傳回目前的速度
			}
			set
			{
				if (value < 0) value = 0;       // 速度不可小於0
				if (value > 200) value = 200;   // 速度不可大於200
				_speed = value;                 // 設定速度
			}
		}
        // 定義Accelerate()方法，用來指定目前車子速度+1 
		public void Accelerate()
		{
			_speed ++;					// 速度 + 1
    		if (_speed > 200) _speed = 200;	// 檢查速度不可超過 200
		}
	}

    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Benz.Speed = 199;
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("加速 ...");
            Benz.Accelerate();
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("加速 ...");
            Benz.Accelerate();
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.Read();
       }
    }
}
