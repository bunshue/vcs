using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleMemMethod1
{
    class Car       // 定義Car類別
    {
        // 宣告私有變數_x, _y用來表示目前車子的X, Y座標位置
        private int _x, _y; 
        // 定義Movie方法，用來設定目前車子的X, Y座標位置
        public void Move(int vX, int vY)
        {
            _x = vX;
            _y = vY;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
           Car Benz = new Car();
           Benz.Move(100, 200);    

        }
    }
}
