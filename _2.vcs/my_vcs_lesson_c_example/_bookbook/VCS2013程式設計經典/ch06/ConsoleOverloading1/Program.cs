using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleOverloading1
{
   class Car   // 定義Car類別
   {
       private int _speed = 0;
       public int Speed
       {
           get
           {
                return _speed;
            }
            set
            {
                if (value < 0) value = 0;
                if (value > 200) value = 200;
                _speed = value;
            }
        }
        // 第一種加速方法
        public void Accelerate()
        {
            this.Speed++;
        }
        // 第二種加速方法
        public void Accelerate(int addSpeed)
        {
            this.Speed += addSpeed;
        }
        // 第三種加速方法
        public void Accelerate(string S)
       	{
            if (S == "STOP") this.Speed = 0;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("加速 ...");
            Benz.Accelerate();		// 執行第一種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("加速 10 ...");
            Benz.Accelerate(10);		// 執行第二種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("停車 ...");
            Benz.Accelerate("STOP");	// 執行第三種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.Read();
        }
    }
}
