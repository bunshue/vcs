using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_2_11
{
    class Program
    {
        static void Main(string[] args)
        {
            // 利用特定的值尋找具有子項目的特定項目。
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            IEnumerable<XElement> tests =
                from el in root.Elements("地址")
                where (string)el.Element("城市") == "屏東市"
                select el;

            foreach (XElement el in tests)
            {
                Console.WriteLine("姓名->" + (string)el.Element(XName.Get("姓名")).Value);
                Console.WriteLine("郵遞區號->" + (string)el.Element(XName.Get("郵遞區號")).Value);
            }
        }
    }
}


