using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleInterface2
{
     // 宣告一個使用 IComparable 介面的類別 Vector
     public class Vector : IComparable
     {
         public int X { get; set; } // 定義X屬性
         public int Y { get; set; } // 定義Y屬性
 
         public Vector()
         {
             X = 0;
             Y = 0;
         }
         public Vector(int vX, int vY)
         {
             X = vX;
             Y = vY;
         }
         public void Show()			// 用來顯示向量座標 (X,Y)
         {
             Console.Write("({0},{1})  ", X, Y);
         }
         //實作IComparable介面中的CompareTo方法
         int IComparable.CompareTo(object obj)
         {
             Vector v = (Vector)obj;
             return (X * X + Y * Y) - (v.X * v.X + v.Y * v.Y);
         }
     }

    class Program
    {
        static void Main(string[] args)
        {
             // 定義一個內含五個向量的陣列        
             Vector[] vecArray = {new Vector(20, 10), 
              	new Vector(50, 20), 
              	new Vector(90, 40), 
              	new Vector(10, 10), 
              	new Vector(40, 30)};
             Console.WriteLine("排序前 ...");
             for (int i = 0; i <= vecArray.GetUpperBound(0); i++)
             {
                 vecArray[i].Show();
             }
             Console.WriteLine();
             Console.WriteLine();
 
             Array.Sort(vecArray); // 呼叫 System.Array 類別的 Sort 方法
 
             Console.WriteLine("排序後 ...");
             for (int i = 0; i <= vecArray.GetUpperBound(0); i++)
             {
                 vecArray[i].Show();
             }
             Console.Read();
        }
    }
}
