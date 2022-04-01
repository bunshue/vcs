using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Ivony.Html;
using Ivony.Html.Parser;

namespace vcs_Jumony2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            foreach (var title in new JumonyParser().LoadDocument("http://www.cnblogs.com/").Find(".post_item a.titlelnk"))
            {
                //Console.WriteLine(title.InnerText() + "==================" + title.Attribute("href").Value());


                richTextBox1.Text += title.InnerText() + "==================" + title.Attribute("href").Value() + "\n";
            }

            richTextBox1.Text += "done\n";




        }
    }
}
