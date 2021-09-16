using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace GetEnumerator2
{
    class Program
    {
        static void Main(string[] args)
        {
            // 宣告並建立含有10個字元的字串陣列
            String[] myAry = new String[10];
            // 設定陣列初值
            myAry[0] = "第三次";
            myAry[1] = "工業革命";
            myAry[2] = "是";
            myAry[3] = "3D 列印";

            // 顯示陣列的內容
            int i = 0;
            //實作名稱myEnumerator列舉器, 透過GetEnumerator方法來讀取myAry陣列
            // 此時指標指到myAry陣列第一個陣列元素的前面
            IEnumerator myEnumerator = myAry.GetEnumerator();

            Console.WriteLine("\n myAry 陣列元素內容如下 :\n");
            // 依序透過MoveNext方法指標下移一個項目,current屬性讀取陣列元素
            while ((myEnumerator.MoveNext()) && (myEnumerator.Current != null))
                Console.WriteLine(" myAry[{0}] = {1}", i++, myEnumerator.Current);
            Console.Read();
        }
    }
}
