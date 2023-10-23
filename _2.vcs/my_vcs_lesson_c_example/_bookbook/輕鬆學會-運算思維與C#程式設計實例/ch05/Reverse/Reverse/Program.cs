using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Reverse
{
    class Program
    {
        static string reverse(string str)
        {
            char[] temp;
            string strR = "";
            int i;
            temp = str.ToCharArray();
            for (i = temp.Length - 1; i >= 0; i--)
                strR += temp[i];
            return strR;
        }

        static void Main(string[] args)
        {
            string str;
            Write("請輸入原字串內容：");
            str = ReadLine();
            WriteLine("經反轉後的字串內容：" + reverse(str));
            Read();
        }
    }
}
