using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleInterface1
{
    interface IFly 			//定義IFly介面 
    {
        void Fly(int n); 	//宣告Fly方法
    }

    class Car : IFly    	//Car類別實作IFly介面
    {
         public void SpeedUp(int n)
         {
             Console.WriteLine("車子加速前進 {0} 公里", n);
         }
         //Car類別的Fly方法實作IFly介面的Fly方法
         public void Fly(int n)
         {
             Console.WriteLine("車子飛上天前進 {0} 公里", n);
         }
    }
 
    class Bird : IFly 		//Bird類別實作IFly介面
    {
         public void Eat(int n)
         {
             Console.WriteLine("小鳥吃了 {0} 公斤的飼料", n);
         }
         //Bird類別的Fly方法實作IFly介面的Fly方法
         public void Fly(int n)
         {
             Console.WriteLine("小鳥飛上天前進 {0} 公里", n);
         }
    }

    class Program
    {
        static void Main(string[] args)
        {
             Car BMW = new Car();    
             BMW.Fly(30);                    
             Console.WriteLine();
             Bird bird1 = new Bird();
             bird1.Fly(5);
             Console.Read();
        }
    }
}
