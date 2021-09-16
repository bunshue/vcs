using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleProperty2
{
    class Car       // 定義Car類別
    {
        // 宣告_speed為私有變數，表示該變數只能在Car類別內使用
        private int _speed; 
        // 宣告Speed為公開屬性
        public int Speed
        {
            get     // get存取子可傳回屬性值
            {
                return _speed;			// 傳回屬性值
            }
            set     // set存取子可設定屬性值
            {
                if (value < 0) value = 0;	    // 速度不得低於 0
                if (value > 200) value = 200;	// 速度不得高於 200
                _speed = value;			        // 設定屬性值
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Benz.Speed = 500;			// 速度值超過 200
            Console.WriteLine("Benz.Speed = {0}", Benz.Speed);
            Console.Read();
        }
    }
}
