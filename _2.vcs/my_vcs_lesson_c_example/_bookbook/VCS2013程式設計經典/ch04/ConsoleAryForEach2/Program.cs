using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleAryForEach2
{
    class Program
    {
        const double PI = 3.14;
        static void Main(string[] args)
        {
            //宣告建立一維整數陣列,並設定初值
            int[] ary = new int[] { 2, 4, 6, 8 };
            //對ShowArea()方法設定一個委派(Delegate)
            //即設定 myAction 的動作為呼叫ShowArea()方法
            //ShowArea方法的虛引數為整數資料        
            Action<int> myAction = new Action<int>(ShowArea);
            // 逐一對取出的陣列元素執行myAction指定的動作
            Array.ForEach(ary, myAction);
            Console.Read();
        }
        // 對逐一傳入的陣列元素值取平方值並顯示其結果
        private static void ShowArea(int r)
        {
            Console.WriteLine(" 半徑:{0:d} 的圓面積 : {1:f}", r, PI * r * r);
        }
    }
}
