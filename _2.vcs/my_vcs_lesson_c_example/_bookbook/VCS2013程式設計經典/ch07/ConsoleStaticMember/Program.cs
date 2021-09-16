using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleStaticMember
{
    public class Car
    {
        public  int No { get; set; }         // No屬性用來記錄是第幾部車
        public static int Total { get; set; }// Total靜態屬性，記錄車子總數
        // static方法
        public static void ShowTotalCars()
        {
            Console.WriteLine("現在共有 {0} 部車子", Total);
            Console.WriteLine("=========================\n");
        }
        public void ShowMe(string vCarName)
        {
            Console.WriteLine("{0} 是第 {1} 部車。", vCarName, No);
        }
        public Car()       	// Car類別建構式
        {
            Total += 1;
            No = Total;      	// 記錄車號
        }
        ~Car()                 	// Car類別解構式
        {
            Total -= 1;       	// 當物件消滅時，將Total減1，表示車子總數減1
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Car.ShowTotalCars();
            Car Benz = new Car();	// 建立第一部新車
            Console.WriteLine("Benz 是第 {0} 部車", Benz.No);
            Car.ShowTotalCars();
            Car BMW = new Car();   	// 建立第二部新車
            Car Ford = new Car();	// 建立第三部新車
            BMW.ShowMe("BMW");
            Ford.ShowMe("Ford");
            Car.ShowTotalCars();
            Car MyCar;      		// 宣告一個 Car 的參考 
            Car.ShowTotalCars();
            MyCar = BMW;    		// 將 MyCar 指向 BMW
            MyCar.ShowMe("MyCar");
            Console.Read();

        }
    }
}
