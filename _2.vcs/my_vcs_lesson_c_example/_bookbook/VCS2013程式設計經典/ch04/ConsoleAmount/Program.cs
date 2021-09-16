using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleAmount
{
    class Program
    {
        static void Main(string[] args)
        {
            // 建立和設定不規則陣列初值
            double[][] amt = new double[3][];
            // 建立amt[0][0]~amt[0][2]陣列元素, 存放台北分公司第一, 二, 三處的金額
            amt[0] = new double[] { 1100, 2200, 3300 };
            // 建立amt[1][0]~amt[1][1]陣列元素, 存放台中分公司第一, 二處的金額
            amt[1] = new double[] { 1500, 2500 };
            // 建立amt[2][0]~amt[2][3]陣列元素, , 存放高雄分公司第一, 二, 三, 四處的金額
            amt[2] = new double[] { 1000, 2000, 3000, 4000 };
            // 建立 company[0]~company[2]用來存放三個分公司的名稱
            string[] company = new string[] { "台北", "台中", "高雄" };
            // 建立 sum[0]~sum[2]用來存放台北, 台中, 高雄各分公司的總營業額
            double[] sum = new double[] { 0.0, 0.0, 0.0 };
            double total = 0;	//總營業額
            Console.WriteLine("\t第一處\t第二處\t第三處\t第四處  (單位：千元)");
            for (int i = 0; i < amt.Length; i++)
            {
                for (int k = 0; k < amt[i].Length; k++)
                {
                    Console.Write("\t{0}", amt[i][k]);	// 顯示各處的金額
                    sum[i] += amt[i][k];       		// 計算各公司的營業額
                }
                total += sum[i] * 1000;  		// 計算總營業額
                Console.WriteLine();
            }
            Console.WriteLine("\n");
            for (int n = 0; n < 3; n++)
            {
                sum[n] *= 1000;
                Console.WriteLine("{0}分公司營業額：{1}元\t營業率：{2:p}",
                        company[n], sum[n].ToString("c"), sum[n] / total);
            }
            Console.WriteLine("\n總營業額：{0}元", total.ToString("c"));
            Console.Read();
        }
    }
}
