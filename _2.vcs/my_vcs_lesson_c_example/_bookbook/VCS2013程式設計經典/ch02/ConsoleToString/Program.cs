using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleToString
{
    class Program
    {
        static void Main(string[] args)
        {
            double myvar1 = 0801234567;    //輸出結果：(080)123-4567	
            Console.WriteLine("1. " +
                  myvar1.ToString("(0##) ###-####"));

            int myvar2 = -12345;   		//輸出結果：-12345
            Console.WriteLine("2. " + myvar2.ToString("######"));

            int myvar3 = -12345;	            	//輸出結果：-012345
            Console.WriteLine("3. " + myvar3.ToString("000000"));
            double myvar4 = -2.455;	    	//輸出結果：-2.46
            Console.WriteLine("4. " + myvar4.ToString("#.##"));

            double myvar5 = -2.4;		//輸出結果：-2.40
            Console.WriteLine("5. " + myvar5.ToString("0.00"));

            double myvar6 = -2.455;            //輸出結果：-02.46
            Console.WriteLine("6. " + myvar6.ToString("00.00"));

            double myvar7 = 1234567890;    	//輸出結果：1,234,567,890
            Console.WriteLine("7. " + myvar7.ToString("#,#"));

            double myvar8 = 1234567890;		//輸出結果：1234568
            Console.WriteLine("8. " + myvar8.ToString("#,"));

            double myvar9 = 1234567890;    	//輸出結果： 1235
            Console.WriteLine("9. " + myvar9.ToString("#,,"));

            double myvar10 = 1234567890;		//輸出結果：1
            Console.WriteLine("10. " + myvar10.ToString("#,,,"));

            double myvar11 = 1234567890;		//輸出結果：1,235
            Console.WriteLine("11. " + myvar11.ToString("#,##0,,"));

            double myvar12 = 0.086;		//輸出結果：8.6%
            Console.WriteLine("12. " + myvar12.ToString("#0.##%"));

            double myvar13 = 0.08647;		//輸出結果：8.65%
            Console.WriteLine("13. " + myvar13.ToString("#0.##%"));
            double myvar14 = 16800;		//輸出結果：1.68E+4
            Console.WriteLine("14. " + myvar14.ToString("0.###E+0"));

            double myvar15 = 16800;		//輸出結果：1.68E+004
            Console.WriteLine("15. " + myvar15.ToString("0.###E+000"));

            double myvar16 = 16800;		//輸出結果：1.68E004
            Console.WriteLine("16. " + myvar16.ToString("0.###E-000"));

            double myvar17 = 123456;		//輸出結果：[12-34-56]
            Console.WriteLine("17. " + myvar17.ToString("[##-##-##]"));

            int myvar18 = 1234;			//輸出結果：1234
            Console.WriteLine("18. " + myvar18.ToString("##;(##)"));

            int myvar19 = 1234;			//輸出結果：(1234)
            Console.WriteLine("19. " + myvar19.ToString("(##);##"));

            int myvar20 = -1234;			//輸出結果：(1234)
            Console.WriteLine("20. " + myvar20.ToString("##;(##)"));
            Console.Read();

        }
    }
}
