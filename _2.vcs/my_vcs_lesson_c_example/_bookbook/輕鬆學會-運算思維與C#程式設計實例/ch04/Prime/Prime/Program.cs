using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace Prime
{
    class Program
    {
        static int Is_prime(int n)
        {
            int i = 2;
            while (i <= n)
            {
                if (n % i == 0) //如果整除,i是n的因數,回傳 false
                    return 0;
                i = i + 1;
                return 1;
            }
            return 1;
        }
        static void Main(string[] args)
        {
            int n;
            Write("請輸入一個大於等於2的數字: ");
            n = int.Parse(ReadLine());
            if (n == 2)
                WriteLine(n + "是質數");
            if (Is_prime(n) == 1)
                WriteLine(n + "是質數");
            else
                WriteLine(n + "不是質數");
            ReadKey();
        }
    }
}