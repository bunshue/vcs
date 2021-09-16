using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleInterface3
{
     // 定義IMyComparable介面
     public interface IMyComparable
     { 
         // 宣告IMyComparable介面的MyCompareTo方法
         int MyCompareTo(object obj);  
     }

     class MyArray
     {
         public static void MySort(IMyComparable[] obj)
         {
             // 使用汽泡排序法來排序陣列
             for (int i = 0; i <= obj.Length - 2; i++)
             {
                 for (int j = i + 1; j <= obj.Length - 1; j++)
                 {
                     // 如果 obj[j] 比 obj[i] 小的話就交換
                     if (obj[j].MyCompareTo(obj[i]) < 0)
                     {
                         // 進行兩數交換
                         IMyComparable tmp = obj[j];
                         obj[j] = obj[i];
                         obj[i] = tmp;
                     }
                 }
             }
         }
     }
     // 定義一個使用 IMyComparable 介面的類別 Vector
     class Vector : IMyComparable
     {
         public int X { get; set; }  	// 定義X屬性
         public int Y { get; set; }   	// 定義Y屬性
 
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
 
         // 實作出IMyComparable介面中的MyCompareTo方法
         int IMyComparable.MyCompareTo(object obj)
         {
             Vector v = (Vector)obj;
             return (X * X + Y * Y) - (v.X * v.X + v.Y * v.Y);
         }
     }

    class Program
    {
        static void Main(string[] args)
        {
             // 建立一個內含五個向量的陣列物件vecArray       
             Vector[] vecArray = {
                new Vector(20, 10),
 				new Vector(50, 20),
 				new Vector(90, 40),
 				new Vector(10, 10),
 				new Vector(40, 30) };
             Console.WriteLine("排序前 ...");
             for (int i = 0; i <= vecArray.GetUpperBound(0); i++)
             {
                 vecArray[i].Show();
             }
             Console.WriteLine();
             Console.WriteLine();
 
             MyArray.MySort(vecArray);     //呼叫 System.Array 類別的 Sort 方法
 
             Console.WriteLine("排序後 ...");
             for (int i = 0; i <= vecArray.GetUpperBound(0); i++)
             {
                 vecArray[i].Show();
             }
             Console.Read();
        }
    }
}
