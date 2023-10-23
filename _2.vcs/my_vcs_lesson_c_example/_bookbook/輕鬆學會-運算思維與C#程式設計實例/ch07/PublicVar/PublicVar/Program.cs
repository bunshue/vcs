using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別


namespace PublicVar
{
    class Program
    {
        class Book
        {
            public int books; //宣告books為公用變數
        }

        static void Main(string[] args)
        {
            Book eng = new Book();
            eng.books = 10;
            WriteLine("目前英文類書籍共有{0}本", eng.books);
            Read();
        }
    }
}
