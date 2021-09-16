using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleSort1
{
    class Program
    {
        static void Main(string[] args)
        {
            // 建立RoleName[0]~RoleName[4]用來存放角色姓名
            string[] RoleName = new string[] { "魯夫", "喬巴", "羅賓", "香吉士", "騙人布" };
            // 建立Money[0]~Money[4] 用來存放角色的懸賞金額
            int[] Money = new int[] { 300000000, 50, 78000000, 77000000, 30000000 };
            Console.WriteLine("==草帽海賊團成員(遞增排序)==\n");
            Console.WriteLine("姓名\t懸賞金額");
            Console.WriteLine("==================");
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            int i; // 宣告 i 為for迴圈計數變數
            // 陣列的GetUpperBound()方法可用來取得某一維度的上限
            // 因此RoleName.GetUpperBound(0) 會傳回 4
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                Console.WriteLine(RoleName[i] + "\t" + Money[i].ToString("#,#"));
            }
            Console.WriteLine("\n");

            Console.WriteLine("==草帽海賊團成員(遞減排序)==\n");
            Console.WriteLine("姓名\t懸賞金額");
            Console.WriteLine("==================");
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            // 反轉Money陣列，使Money陣列變成遞減排序
            Array.Reverse(Money);
            Array.Reverse(RoleName);    // 反轉RoleName陣列
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                Console.WriteLine(RoleName[i] + "\t" + Money[i].ToString("#,#"));
            }
            Console.Read();

        }
    }
}
