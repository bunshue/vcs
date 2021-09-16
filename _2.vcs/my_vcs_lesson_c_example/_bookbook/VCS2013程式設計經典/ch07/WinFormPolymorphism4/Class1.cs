using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormPolymorphism4
{
    class Class1
    {
    }
     // 定義Cal抽象類別, 抽象類別無法實體化(即無法使用抽象類別建立物件)
     public abstract class Cal
     {
         public int X { get; set; }  // X屬性
         public int Y { get; set; }  // Y屬性
         // 定義Cal抽象類別的Answer抽象方法
         public abstract double Answer();
     }
     // 定義CalAdd類別繼承自Cal類別
     public class CalAdd : Cal
     {
         // 覆寫Cal父類別的Answer抽象方法，傳回X, Y兩數相加
         public override double Answer() 
         {
             return X + Y;   
         }
     }
     // 定義CalSub類別繼承自Cal類別
     public class CalSub : Cal
     {
         // 覆寫Cal父類別的Answer抽象方法，傳回X, Y兩數相減
         public override double Answer()
         {
             return X - Y;
         }
     }
     // 定義CalMul類別繼承自Cal類別
     public class CalMul : Cal
     {
         // 覆寫Cal父類別的Answer抽象方法，傳回X, Y兩數相乘
         public override double Answer()
         {
             return X * Y;
         }
     }
     // 定義CalDiv類別繼承自Cal類別
     public class CalDiv : Cal
     {
         // 覆寫Cal父類別的Answer抽象方法，傳回X, Y兩數相除
         public override double Answer()
         {
             return X / Y;
         }
    }  
}
