using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_5_21
{
    class Program
    {
        static void Main(string[] args)
        {
            XElement root = XElement.Load(@"c:\價目表.xml");
            IEnumerable<decimal> costs =
                from el in root.Elements("書")
                let total = (decimal)el.Element("庫存量") * (decimal)el.Element("訂價")
                where total >= 800
                orderby total
                select total;

            foreach (decimal cost in costs)
                Console.WriteLine(cost);
        }
    }
}


