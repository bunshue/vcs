using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xCh11_6_3_21
{
    class Program
    {
        static void Main(string[] args)
        {
            string markup = @"
                <moto:Root xmlns:moto='http://www.eTesting.com.tw' xmlns:john='www.onlineTesting.com.tw'>
                  <john:元素1>電子商務</john:元素1>
                  <john:元素2>企業資源規劃</john:元素2>
                  <moto:元素3>Visual C# 2013視窗程式設計</moto:元素3>
                  <john:元素4>
                    <john:子元素1>電子商務網站</john:子元素1>
                    <moto:子元素2>ASP.NET程式設計</moto:子元素2>
                  </john:元素4>
                </moto:Root>";

            XElement xmlTree = XElement.Parse(markup);

            Console.WriteLine("位於 http://www.eTesting.com.tw 名稱空間的元素");
            var motoElements =
                from el in xmlTree.Descendants()
                where el.Name.Namespace == "http://www.eTesting.com.tw"
                select new
                {
                    x = (string)el.Name.LocalName,
                    y = (string)el.Value
                };

            foreach (var el in motoElements)
                Console.WriteLine(el.x + " 的內容是 " + el.y);
        }
    }
}


