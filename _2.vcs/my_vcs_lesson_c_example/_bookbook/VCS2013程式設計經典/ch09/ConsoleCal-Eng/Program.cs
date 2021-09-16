using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ConsoleCal_Eng
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("請輸入一個檔案路徑：");
            string fname = Console.ReadLine();
            FileInfo f = new FileInfo(fname);
            StreamReader sr;
            try
            {
                sr = f.OpenText();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                Console.ReadLine();
                return;
            }
            int[] letter = new int[26];
            int k;
            char ch;
            while (sr.Peek() >= 0)
            {
                ch = (char)sr.Read();
                if (ch >= 'A' && ch <= 'Z')
                {
                    k = (int)ch - 65;
                    letter[k]++;
                }
                else if (ch >= 'a' && ch <= 'z')
                {
                    k = (int)ch - 97;
                    letter[k]++;
                }
            }
            Console.WriteLine();
            Console.WriteLine("== 本檔案 英文字母出現的字數統計如下 : \n");
            for (int i = 0; i < 26; i=i+2)
            {
                if ((i % 2) == 0)
                {
                    Console.Write(" {0}, {1}, {2}個", (char)(65 + i), (char)(97 + i), letter[i]);
                    Console.Write("\t {0}, {1}, {2}個",(char)(65 + i+1), (char)(97 + i+1), letter[i+1]);
                }
                Console.WriteLine();
            }
            sr.Close();
            Console.ReadLine();
        }
    }
}
