using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleDestructor1
{
    class Car  // 定義Car類別
    {
        private int _speed = 0;
        // 物件的建構式 #1        
        public Car()
        {
            _speed = 0;
            Console.WriteLine("初始化後速度 = {0}", _speed);
        }
        // 物件的建構式 #2        
        public Car(int vSpeed)
        {
            _speed = vSpeed;
            Console.WriteLine("初始化後速度 = {0}", _speed);
        }
        // 物件的解構式    
        ~Car()
        {
            Console.WriteLine("車子物件消滅了 ...");
        }
    }
   class Program
    {
       static void DoSomething()
       {
            Console.WriteLine("進入程序，並宣告 BMW 物件 ...");
            Car BMW = new Car(10);
            Console.WriteLine("BMW 物件宣告完成，準備離開方法 ...");
       }

       static void Main(string[] args)
       {
            DoSomething();
            Console.WriteLine("宣告 Benz 物件 ..");
            Car Benz = new Car();
            Console.WriteLine("Benz 物件宣告完成 ..");
            Console.WriteLine("準備執行 Benz = null ...");
            Benz = null;
            Console.WriteLine("Benz = null 執行完成 !!");
            Console.Read();
        }
    }
}
