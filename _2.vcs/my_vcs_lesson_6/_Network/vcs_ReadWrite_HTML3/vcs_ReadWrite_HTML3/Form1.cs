using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_HTML3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button2.Enabled = false;
        }

        private void webBrowser1_Navigating(object sender, WebBrowserNavigatingEventArgs e)
        {

        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            button2.Enabled = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //將HTML檔案讀到WebBrowser裏

            //string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";
            string url = @"D:/_git/vcs/_1.data/_html/朱冶蕙老師的電腦教室.html";
            webBrowser1.Navigate(url);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //解讀一個HTML檔案

            HtmlElementCollection elemColl = null;
            HtmlDocument doc = webBrowser1.Document;
            if (doc != null)
            {
                elemColl = doc.GetElementsByTagName("HTML");
                String str = PrintDom(elemColl, new StringBuilder(), 0);
                webBrowser1.DocumentText = str;
            }
        }

        private string PrintDom(HtmlElementCollection elemColl, StringBuilder returnStr, Int32 depth)
        {
            StringBuilder str = new StringBuilder();

            foreach (HtmlElement elem in elemColl)
            {
                string elemName;

                elemName = elem.GetAttribute("ID");
                if (elemName == null || elemName.Length == 0)
                {
                    elemName = elem.GetAttribute("name");
                    if (elemName == null || elemName.Length == 0)
                    {
                        elemName = "<no name>";
                    }
                }

                str.Append(' ', depth * 4);
                str.Append(elemName + ": " + elem.TagName + "(Level " + depth + ")");
                returnStr.AppendLine(str.ToString());

                if (elem.CanHaveChildren)
                {
                    PrintDom(elem.Children, returnStr, depth + 1);
                }

                str.Remove(0, str.Length);
            }

            return (returnStr.ToString());
        }


    }
}
