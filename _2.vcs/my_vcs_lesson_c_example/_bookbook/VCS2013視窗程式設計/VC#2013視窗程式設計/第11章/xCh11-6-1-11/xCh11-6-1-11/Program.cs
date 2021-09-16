using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_1_11
{
    class Program
    {
        static void Main(string[] args)
        {
            // 如何尋找其屬性具有特定值的特定項目
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            IEnumerable<XElement> address =
                from el in root.Elements("地址")
                where (string)el.Attribute("付款方式") == "貨到付款"
                select el;


            foreach (XElement el in address)
                Console.WriteLine(el);
        }
    }
}


