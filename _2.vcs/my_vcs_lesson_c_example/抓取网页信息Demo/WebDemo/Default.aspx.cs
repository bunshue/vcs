using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Ivony.Html;
using Ivony.Html.Parser;

namespace WebDemo
{
    public partial class _Default : Page
    {
        public string Html = string.Empty;
        protected void Page_Load(object sender, EventArgs e)
        {
            string[] number = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty" };
            var htmlSource = new JumonyParser().LoadDocument("http://www.cnblogs.com").Find(".post_item a.titlelnk");
            int count = 0;
            foreach (var htmlElement in htmlSource)
            {
                count ++;
                Html += string.Format(" <li>{2}、&nbsp;&nbsp;<a href=\"About.aspx?Url={0}\" target=\"_blank\">{1}</a></li>", htmlElement.Attribute("href").Value(), htmlElement.InnerText(),count);
            }
        }
    }
}