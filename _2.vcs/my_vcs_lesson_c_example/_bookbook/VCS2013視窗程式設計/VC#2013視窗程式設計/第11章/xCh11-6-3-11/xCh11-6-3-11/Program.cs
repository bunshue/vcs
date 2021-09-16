using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_3_11
{
    class Program
    {
        static void Main(string[] args)
        {
            XElement root = XElement.Parse(@"
            <文章>
                <段落>
                    <第一章>
                      <主題>有些文字</主題>
                    </第一章>
                    <第二節>
                      <第一段>
                        <主題>被打散到</主題>
                      </第一段>
                    </第二節>
                    <第三節>
                      <第一段>
                        <主題>多個段落</主題>
                      </第一段>
                    </第三節>
                </段落>
            </文章>");
            IEnumerable<string> textSegs =
                from seg in root.Descendants("主題")
                select (string)seg;

            string str = textSegs.Aggregate(new StringBuilder(),
                (sb, i) => sb.Append(i),
                sp => sp.ToString()
            );

            Console.WriteLine(str);
        }
    }
}


