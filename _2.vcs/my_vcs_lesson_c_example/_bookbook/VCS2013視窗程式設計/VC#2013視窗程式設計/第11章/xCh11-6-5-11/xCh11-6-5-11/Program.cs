using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_5_11
{
    class Program
    {
        static void Main(string[] args)
        {
            XElement root = XElement.Load(@"c:\價目表.xml");
            IEnumerable<decimal> prices =
                from el in root.Elements("書")
                let price = (decimal)el.Element("訂價")
                orderby price
                select price;

            Console.WriteLine("書籍價目表，依價格排序：");
            foreach (decimal el in prices)
                Console.WriteLine(el + " 元");
        }
    }
}


