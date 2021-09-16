using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_4_21
{
    class Program
    {
        static void Main(string[] args)
        {
            XElement root = XElement.Parse(@"
            <根元素>
                <分類 分類號=""1""/>
                <清單>程式設計</清單>
                <Microsoft系列>
                    <分類 分類號=""2""/>
                    <notul/>
                    <分類 分類號=""3""/>
                    <清單>def</清單>
                    <分類 分類號=""4""/>
                </Microsoft系列>
                <開放源始碼系列>
                    <分類 分類號=""5""/>
                    <notul/>
                    <分類 分類號=""6""/>
                    <清單>abc</清單>
                    <分類 分類號=""7""/>
                </開放源始碼系列>
            </根元素>");

            IEnumerable<XElement> items =
                from e in root.Descendants("分類")
                let z = e.ElementsAfterSelf().FirstOrDefault()
                where z != null && z.Name.LocalName == "清單"
                select e;

            foreach (XElement e in items)
                Console.WriteLine("分類號 = {0}", (string)e.Attribute("分類號"));
        }
    }
}


