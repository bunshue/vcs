using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Console_4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("更改控制台窗口大小、字體顏色、獲得行號");
            //更改控制台窗口大小、字體顏色、獲得行號
            // TODO: Implement Functionality Here
            Console.WriteLine("原Console寬 : " + Console.WindowWidth);
            Console.WriteLine("原Console高 : " + Console.WindowHeight);
            Console.WriteLine("原BufferWidth : " + Console.BufferWidth);
            Console.WriteLine("原BufferHeight : " + Console.BufferHeight);
            Console.WriteLine("按鍵繼續....");
            Console.ReadKey();

            Console.Title = "Test";//設置窗口標題
            Console.WindowWidth = 150;
            Console.WindowHeight = 60;
            Console.BufferWidth = 200;
            //Console.BufferHeight = 300;
            Console.WriteLine("設置標題");
            Console.WriteLine("新Console寬 : " + Console.WindowWidth);
            Console.WriteLine("新Console高 : " + Console.WindowHeight);
            Console.WriteLine("新BufferWidth : " + Console.BufferWidth);
            Console.WriteLine("新BufferHeight : " + Console.BufferHeight);
            Console.WriteLine("按鍵繼續....");
            Console.ReadKey(true);

            Console.WriteLine("設置背景色, 設置字體顏色");
            Console.BackgroundColor = ConsoleColor.Blue; //設置背景色
            Console.ForegroundColor = ConsoleColor.White; //設置前景色，即字體顏色
            Console.WriteLine("第一行白藍.");
            Console.ResetColor(); //將控制台的前景色和背景色設為默認值
            Console.BackgroundColor = ConsoleColor.Green;
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            string str = "第三行 綠暗綠";
            Console.WriteLine(str.PadRight(Console.BufferWidth - (str.Length % Console.BufferWidth))); //設置一整行的背景色
            Console.ResetColor();
            Console.WriteLine("按鍵繼續....");
            Console.ReadKey(true);

            Console.WriteLine("計算當前光標所在的行數，針對於Console.BufferHeight的值");
            ShowColor();
            int m = Console.CursorTop;//查看當前行號Console.BufferHeight 
            Console.ReadKey();

            Console.WriteLine("按鍵繼續....");
            Console.ReadKey(true);

            Console.WriteLine("設置控制台字體顏色程序");
            String nl = Environment.NewLine;
            String[] colorNames = Enum.GetNames(typeof(ConsoleColor));
            Console.WriteLine("{0}All the foreground colors on a constant black background.", nl);
            Console.WriteLine("  (Black on black is not readable.){0}", nl);
            for (int x = 0; x < colorNames.Length; x++)
            {
                Console.Write("{0,2}: ", x);
                Console.BackgroundColor = ConsoleColor.Black;
                Console.ForegroundColor = (ConsoleColor)Enum.Parse(typeof(ConsoleColor), colorNames[x]);
                Console.Write("This is foreground color {0}.", colorNames[x]);
                Console.ResetColor();
                Console.WriteLine();
            }
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("/x01");
            Console.Write("/u0001");
            Console.Write("/001");
            Console.Write("/x10");
            Console.Write("/u0010");
            Console.Write("/020");

            Console.WriteLine();
            Console.Write("{0,-50}", "Class1.TestMethod1");
            Console.Write("{0,-2}", "/x10");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Pass");

            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("{0,-50}", "Class1.TestMethod2");
            Console.Write("{0,-2}", "/x10");
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Failed");

            Console.WriteLine("按鍵繼續....");
            Console.ReadKey(true);
        }

        //顯示出console中支持的背景色及前景色
        static void ShowColor()
        {
            Type type = typeof(ConsoleColor);
            Console.ForegroundColor = ConsoleColor.White;
            foreach (string name in Enum.GetNames(type))
            {
                Console.BackgroundColor = (ConsoleColor)Enum.Parse(type, name);
                Console.WriteLine(name);
            }

            Console.BackgroundColor = ConsoleColor.Black;
            foreach (string name in Enum.GetNames(type))
            {
                Console.ForegroundColor = (ConsoleColor)Enum.Parse(type, name);
                Console.WriteLine(name);
            }

            foreach (string bc in Enum.GetNames(type))
            {
                Console.BackgroundColor = (ConsoleColor)Enum.Parse(type, bc);
                foreach (string fc in Enum.GetNames(type))
                {
                    Console.ForegroundColor = (ConsoleColor)Enum.Parse(type, fc);
                    Console.WriteLine("bc=" + bc + ",fc=" + fc);
                }
                Console.WriteLine();
            }
        }
    }
}
