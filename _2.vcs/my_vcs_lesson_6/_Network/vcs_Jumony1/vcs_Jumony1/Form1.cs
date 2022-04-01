using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Ivony;
using Ivony.Data;
using Ivony.Parser;
using Ivony.Html;
using Ivony.Fluent;

namespace vcs_Jumony1
{
    public partial class Form1 : Form
    {
        public string Html = string.Empty;//為將拼接好html字符串返回給前台代碼

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var htmlSource = new JumonyParser().LoadDocument("http://www.cnblogs.com").Find(".post_item a.titlelnk");
            int count = 0;
            foreach (var htmlElement in htmlSource)
            {
                count++;
                Html += string.Format(" <li>{2}、&nbsp;&nbsp;<a href=\"About.aspx?Url={0}\" target=\"_blank\">{1}</a></li>", htmlElement.Attribute("href").Value(), htmlElement.InnerText(), count);
            }
        }
    }
}

