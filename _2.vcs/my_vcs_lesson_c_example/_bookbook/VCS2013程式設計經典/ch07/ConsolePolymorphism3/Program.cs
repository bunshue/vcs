using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsolePolymorphism3
{
     // 定義Traffic交通工具類別
     class Traffic
     {
         protected static int _miles;  	// _miles用來記錄前進的公里數
         public virtual void SpeedUp() 	//  SpeedUp是空白，允許被子類別覆寫
         {
 
         }
     }
     // 定義Car車子類別繼承自交通工具類別
     class Car : Traffic
     {
         public override void SpeedUp()  // 覆寫父類別的SpeedUp方法
         {
             _miles += 2;
             Console.WriteLine("\n 駕駛車子, 加速中, 前進 {0} 公里 .", _miles);
             Console.WriteLine("--------------------------------------");
         }
     }
     // 定義Airplane飛機類別繼承自交通工具類別
     class Airplane : Traffic
     {
 
         public override void SpeedUp()   // 覆寫父類別的SpeedUp方法
         {
             _miles += 15;
             Console.WriteLine("\n駕駛飛機, 加速中, 前進 {0} 公里 .", _miles);
             Console.WriteLine("--------------------------------------");
         }
     }

    class Program
    {
        static void Main(string[] args)
        {
             Traffic r;			// r是Taffic類別的物件參考
             // myCar是Car類別的物件實體, 同時繼承Traffic類別
             Car myCar = new Car();
             // myAirplane是Airplane類別的物件實體, 同時繼承Traffic類別
             Airplane myAirplane = new Airplane();
             int input;
             while (true)
             {
                 Console.Write("請問要駕駛->1.車子  2.飛機  其他.離開：");
                 input = int.Parse(Console.ReadLine());
                 if (input == 1)
                 {
                     r = myCar;     //開車子,r參考指向myCar物件實體
                 }
                 else if (input == 2)
                 {
                     r = myAirplane; //開飛機,r參考指向myAirplane物件實體
                 }
                 else
                 {
                     break;
                 }
                 r.SpeedUp();	// 呼叫r參考指向物件實體的SpeedUp()方法
                 Console.WriteLine();
             }
             Console.Read();
         }
    }
}
