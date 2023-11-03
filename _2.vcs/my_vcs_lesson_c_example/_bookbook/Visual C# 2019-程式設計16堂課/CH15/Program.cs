using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;


namespace 程式碼加入行號
{
    class Program
    {
        static void Main(string[] args)
        {
           string str;
		   int index=1;

           StreamReader sr = File.OpenText("Program.cs"); 
		   StreamWriter sw = File.AppendText("final.txt");
		   
		   while((str = sr.ReadLine ())!=null)
		   {
			   Console.WriteLine ("{0:D5} {1}",index,str);
			   sw.WriteLine ("{0:D5} {1}",index++,str);
		   }
		   sr.Close ();
		   sw.Close ();
           Console.ReadLine();
        }
    }
}
