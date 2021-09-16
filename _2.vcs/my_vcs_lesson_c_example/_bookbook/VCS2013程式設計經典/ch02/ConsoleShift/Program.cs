using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleShift
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 10;
            n = n << 1; 	//左移一位乘以2  n=n*2=10*2=20
            Console.WriteLine("n=n<<1 左移一位 : {0}", n);

            n <<= 2;  		//左移兩位乘以4  n=n*4=20*4=80
            Console.WriteLine("n=n<<2 左移兩位 : {0}", n);

            n = n >> 2;  	//右移兩位除以4  n=n/4=80/4=20
            Console.WriteLine("n=n<<1 右移兩位 : {0}", n);

            n >>= 1;  		//右移一位除以2  n=n/2=20/2=10
            Console.WriteLine("n>>=1 右移一位 : {0}", n);
            Console.WriteLine();

            char c1 = '9';
            char c2 = '2';
            char c3 = '1';
            Console.WriteLine("原編碼訊息 : " + c1 + c2 + c3);

            int key = 11;
            // c1 ^ key進行位元運算之後，再將結果轉成字元並指定給c1
            c1 = (char)(c1 ^ key);
            c2 = (char)(c2 ^ key);
            c3 = (char)(c3 ^ key);
            Console.WriteLine("編碼後訊息 : " + c1 + c2 + c3);

            c1 = (char)(c1 ^ key);
            c2 = (char)(c2 ^ key);
            c3 = (char)(c3 ^ key);
            Console.WriteLine("解碼後訊息 : " + c1 + c2 + c3);
            Console.ReadLine();
        }
    }
}
