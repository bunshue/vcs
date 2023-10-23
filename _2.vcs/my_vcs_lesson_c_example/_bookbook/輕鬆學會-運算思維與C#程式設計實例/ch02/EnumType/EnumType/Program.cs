using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace EnumType
{
    class Program
    {
        enum Card { spade, heart, diamond, club };
        static void Main(string[] args)
        {
            Card big_card = Card.spade;
            int cardNo = (int)big_card;
            WriteLine("{0} 的列舉值為 {1}", big_card, cardNo);
            ReadLine();
        }
    }
}
