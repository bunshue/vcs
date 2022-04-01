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
    public partial class About : Page
    {
        public string Html = string.Empty;
        public string HtmlText = string.Empty;
        protected void Page_Load(object sender, EventArgs e)
        {
            string html = Request["Url"];
            var htmlSource =
                new JumonyParser().LoadDocument(html);
            HtmlText = htmlSource.Find(".postTitle2").FirstOrDefault().InnerText();

            Html = htmlSource.Find("#cnblogs_post_body").FirstOrDefault().InnerHtml();
        }
    }
}