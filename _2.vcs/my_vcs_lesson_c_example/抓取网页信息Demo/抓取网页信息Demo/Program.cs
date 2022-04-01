using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Net;
using System.Text;
using Ivony.Html;
using Ivony.Html.Parser;

namespace 抓取网页信息Demo
{
    internal class Program
    {
        private static void Main(string[] args)
        {

            foreach (
                var title in new JumonyParser().LoadDocument("http://www.cnblogs.com/").Find(".post_item a.titlelnk"))
            {
                Console.WriteLine(title.InnerText() + "==================" + title.Attribute("href").Value());
            }
            Console.ReadKey();


        }

    }
}
