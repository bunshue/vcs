using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0313
{
    //宣告列舉型別
    enum Seasons { Spring, Summer, Autumn, Winter };

    class Program
    {
        static void Main(string[] args)
        {
            //產生列舉成員
            Seasons today = Seasons.Spring;

            int seasonNum = (int)today;
            WriteLine($"{today}常數值 {seasonNum}");

            ReadKey();
        }
    }
}