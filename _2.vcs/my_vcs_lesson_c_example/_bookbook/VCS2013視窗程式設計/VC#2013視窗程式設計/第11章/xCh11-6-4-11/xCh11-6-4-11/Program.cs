using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_4_11
{
    class Program
    {
        static void Main(string[] args)
        {
            XElement root = XElement.Parse(@"
            <根元素>  
                <元素一>
                    <內容>元素一的內容</內容>
                    <類型 值=""Yes""/>
                </元素一>
                <元素二>
                    <內容>元素二的內容</內容>
                    <類型 值=""Yes""/>
                </元素二>
                <元素三>
                    <內容>元素三的內容</內容>
                    <類型 值=""No""/>
                </元素三>
                <元素四>
                    <內容>元素四的內容</內容>
                    <類型 值=""Yes""/>
                </元素四>
                <元素五>
                    <內容>元素五的內容</內容>
                </元素五>
            </根元素>");
            var cList =
                from typeElement in root.Elements().Elements("類型")
                where (string)typeElement.Attribute("值") == "Yes"
                select (string)typeElement.Parent.Element("內容");

            foreach (string str in cList)
                Console.WriteLine(str);
        }
    }
}


