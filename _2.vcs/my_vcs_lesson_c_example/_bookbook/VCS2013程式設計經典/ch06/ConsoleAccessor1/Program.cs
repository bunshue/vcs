using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleAccessor1
{
    class Car
    {
        // 宣告_speed為私有變數，表示該變數只能在Car類別內使用
        private int _speed;
        // 定義GetSpeed()方法用來傳回_speed
        public int GetSpeed()
        {
            return _speed;
        }
        // 定義SetSpeed()方法用來設定_speed
        public void SetSpeed(int vSpeed)
        {
            if (vSpeed < 0) vSpeed = 0;		// 設定速度不得低於 0
            if (vSpeed > 200) vSpeed = 200;	// 設定速度不得高於 200
            _speed = vSpeed;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Car Benz = new Car();
            Benz.SetSpeed(500);			// 速度值超過 200
            Console.WriteLine("Benz.GetSpeed() = {0}",Benz.GetSpeed());	// 顯示速度最大值200
            Console.Read();
        }
    }
}
