using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //webBrowser1.GoHome();
            webBrowser1.Navigate("about:blank");
        }

        //HTML網頁顯示
        private void button1_Click(object sender, EventArgs e)
        {
            HtmlDocument doc = webBrowser1.Document;
            doc.Body.InnerHtml = textBox1.Text;
        }

    }
}
