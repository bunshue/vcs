using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleEscSeq
{
    class Program
    {
        static void Main(string[] args)
        {
            string str1;
            str1 = "Everyone say：\"Hello World\"";
            Console.WriteLine("12345678901234567890123456789012345678901234567890");

            Console.Write("\t" + str1); 		//空8格再印str1字串後游標停在該行最後面
            Console.WriteLine("\t" + "Wonderful");	//由目前游標最近8的倍數處開始印字串
            //印完字串游標移到下一行最前面
            Console.Write("\nWelcome To VS 2013\n");	//空一行由最左邊開始印字串， 
            //印完游標移到下一行最前面
            Console.WriteLine("c:\\cs\\hw1.cs");	//強迫字串中使用逃脫字元顯示倒斜線
            Console.WriteLine(@"c:\cs\hw1.cs");//使用@使得字串中的逃脫字元失效
            Console.WriteLine("\n\n" + "檔名:C:\\cs\\ex1.cs"); 	//空兩行再顯示檔案路徑
            Console.WriteLine("\n" + @"檔名:C:\cs\ex1.cs");  	//空一行再顯示檔案路徑   

            Console.WriteLine("C# 2013 is Cool !");      	//字串顯示前後未加雙引號
            Console.WriteLine("\"C# 2013 is Cool !\"");  	//字串顯示前後加雙引號 
            // \u0041為字元'A'的UniCode，str2="Apple"
            string str2 = "\u0041pple";

            string str3 = "電腦";
            str2 += str3;      			//合併字串 str2="Apple電腦"
            Console.WriteLine(str2);  	//顯示 "Apple電腦" 游標移到下一行

            string str4 = "\\\u0061\n\n";  	// 倒斜線、字元a、以及跳兩行
            Console.Write(str4 + "Begin:");//先印"\a"再空一行，於下一行顯示Begin:
            Console.Read();
        }
    }
}
